from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import *
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from controller import app, db, bootstrap


@app.route('/')
def index():
    db.create_all()
    return render_template("home.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/updatesuccess')
def updatesuccess():
    return render_template("updatesuccess.html")

@app.route('/add', methods = ['POST', 'GET'])
def add():
    form = Forms(request.form)
    if request.method == 'POST':
        idNew = form.idNew.data
        fnameNew = form.fnameNew.data
        mnameNew = form.mnameNew.data
        lnameNew = form.lnameNew.data
        sexNew = form.sexNew.data
        addressHomeNew = form.addressHomeNew.data
        courseNew = form.courseNew.data
        birth_dateNew = request.form['birthdate']
        if form.validate():
            tenant = Tenant(idNew,fnameNew,mnameNew,lnameNew,addressHomeNew,courseNew,birth_dateNew)
            db.session.add(tenant)
            db.session.commit()
            flash('Tenant successfully added', 'success')
            return redirect(url_for('success'))

        elif not form.validate():
            flash("Please don't leave any blank", 'error')
            return render_template("add.html", form=form)
        else:
            return render_template("add.html", form=form)


    else:
        return render_template("add.html", form=form)

@app.route('/view/<int:page_num>')
def view(page_num):
    pags = Tenant.query.paginate(per_page= 6, page=page_num, error_out=True)
    tents = Tenant.query.all()
    return render_template("print.html",tents = tents, pags = pags)

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    deleteStore = request.form['Store']
    if request.method == 'POST':
        Tenant.query.filter_by(id=deleteStore).delete()
        db.session.commit()
        return redirect(url_for('view', page_num=1))

    else:
        return redirect(url_for('index'))

@app.route('/updateGet', methods = ['POST', 'GET'])
def updateGet():
    updateStore = request.form['Store']
    session['idNew'] = updateStore
    return redirect(url_for('update'))

@app.route('/update', methods = ['POST', 'GET'])
def update():
    form = UpdateForms(request.form)
    idNew = session['idNew']
    pags = Tenant.query.filter(Tenant.id==idNew).first()


    if request.method == 'POST':
        fnameNew = form.fnameNew.data
        mnameNew = form.mnameNew.data
        lnameNew = form.lnameNew.data
        sexNew = form.sexNew.data
        addressHomeNew = form.addressHomeNew.data
        courseNew = form.courseNew.data
        birth_dateNew = request.form['birthdate']


        if form.validate():
            updateNew = Tenant.query.filter_by(id = idNew).first()

            updateNew.fname = fnameNew
            updateNew.mname = mnameNew
            updateNew.lname = lnameNew
            updateNew.sex = sexNew
            updateNew.addressHome = addressHomeNew
            updateNew.course = courseNew
            updateNew.birth_date =birth_dateNew
            db.session.commit()
            pags = Tenant.query.filter(Tenant.id==idNew).first()
            return redirect(url_for('updatesuccess'))

        elif not form.validate():
            flash('Please fill up each of the following', 'error')
            pags = Tenant.query.filter(Tenant.id==idNew).first()
            return render_template("update.html", form = form,pags=pags)

        else:
            pags = Tenant.query.filter(Tenant.id==idNew).first()
            return render_template("update.html", form = form,pags=pags)


    else:
        return render_template("update.html", form=form, pags=pags)


@app.route('/searchGet/<int:page_num>', methods = ['POST', 'GET'])
def searchGet(page_num):

    search = request.form['search']
    if request.method == 'POST':
        search1 = "%"+search+"%"
        pags = Tenant.query.filter((Tenant.id.like(search1)) | (Tenant.fname.like(search1)) | (Tenant.mname.like(search1)) | (Tenant.lname.like(search1)) | (Tenant.course.like(search1)) | (Tenant.sex.like(search1))).paginate(page_num,6)



        return render_template("search.html", pags = pags)

    else:
        return redirect(url_for('print.html', page_num=1))



if __name__=="__main__":
    app.secret_key = 'somesecret'
    app.run(debug=True)



