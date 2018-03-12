from flask import Flask
from controller import db, app
from flask_wtf import FlaskForm
from wtforms import StringField,  PasswordField, RadioField, ValidationError, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, InputRequired, DataRequired


class Tenant(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.String(60), primary_key=True,nullable=False)
    fname = db.Column('fname', db.String(60),nullable=False)
    mname = db.Column('mname', db.String(60),nullable=False)
    lname = db.Column('lname', db.String(60),nullable=False)
    sex = db.Column(db.String(6), nullable=False)
    addressHome = db.Column('addressHome', db.String(60),nullable=False)
    course = db.Column('course', db.String(60),nullable=False)
    birth_date = db.Column(db.DATE, nullable=False)




    def __init__(self, id='', fname='',mname='',lname='',sex='',addressHome='',course='',birth_date=""):
        self.id = id
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.sex = sex
        self.addressHome = addressHome
        self.course = course
        self.birth_date = birth_date


from wtforms import Form, StringField, TextAreaField, PasswordField, SubmitField, validators



class Forms(Form):
    idNew = StringField('ID Number', validators=[Length(min=9, max=9)])
    fnameNew = StringField('First Name', validators=[Length(min=1, max=60)])
    mnameNew = StringField('Middle Name', validators=[Length(min=1, max=60)])
    lnameNew = StringField('Last Name', validators=[Length(min=1, max=60)])
    sexNew = RadioField('Sex', validators=[InputRequired()], choices=[('Male', 'Male'), ('Female', 'Female')], default='M')
    addressHomeNew = StringField('Home Address', validators=[Length(min=1, max=60)])
    courseNew = StringField('Course', validators=[Length(min=1, max=60)])
    submit = SubmitField("Submit")

class UpdateForms(Form):
    fnameNew = StringField('First Name', validators=[Length(min=1, max=60)])
    mnameNew = StringField('Middle Name', validators=[Length(min=1, max=60)])
    lnameNew = StringField('Last Name', validators=[Length(min=1, max=60)])
    sexNew = RadioField('Sex', validators=[InputRequired()], choices=[('Male', 'Male'), ('Female', 'Female')], default='M')
    addressHomeNew = StringField('Home Address', validators=[Length(min=1, max=60)])
    courseNew = StringField('Course', validators=[Length(min=1, max=60)])
    submit = SubmitField("Submit")



