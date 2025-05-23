# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.validators import URL, Email, DataRequired
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, URLField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    style = SelectField('What is your clothing aesthetic',choices=[("2000s","2000s"),("PJs","PJs")])

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    website = StringField('Website', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')


class ReviewForm(FlaskForm):
    name = SelectField('Thrift Store Name',choices=[("Goodwill","Goodwill"),("Out of Closet","Out of Closet"), ("Thrift Town", "Thrift Town"), ("Community Thrift","Community Thrift"), ("American Cancer Society Discovery Shop", "American Cancer Society Discovery Shop"), ("Salvation Army","Salvation Army"), ("Buffalo Exchange","Buffalo Exchange"), ("Plato's Closet","Plato's Closet"), ("Value Village","Value Village"), ("Salvation Army","Salvation Army")])
    text = TextAreaField('Write your Review', validators=[DataRequired()])
    subject = SelectField('Experiences',choices=[("Price of Clothing", "Price of Clothing"), ("Customer Service","Customer Service"),("Selection","Selection"), ("Donation", "Donation"), ("Other","Other")])
    rating = IntegerField('Rate your experience: 0 is terrible, 10 is amazing', validators=[NumberRange(min=0,max=10, message="Enter a number between 0 and 10.")])
    submit = SubmitField('Post Review')

class ReplyForm(FlaskForm):
    text = TextAreaField('Reply', validators=[DataRequired()])
    submit = SubmitField('Post')