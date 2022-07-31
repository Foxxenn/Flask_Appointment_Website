from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
#from wtforms import DateField
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import Length, DataRequired, EqualTo, Email


class RegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=10)])
    fname= StringField(label='First Name', validators= [DataRequired(), Length(max=20)])
    lname= StringField(label='Last Name', validators= [DataRequired(), Length(max=20)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label= 'Sign Up')

class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=6, max=10)])
    submit = SubmitField(label= 'Login')


class DateForm(FlaskForm):
    #username= StringField(label= 'Username' )
    #lawyer1= StringField(label='lusername' )
    startdate= DateField(label='Start Date',format='%Y-%m-%d',validators=(validators.DataRequired(),))
    #enddate= DateField(label='End Date',format='%Y-%m-%d',validators=(validators.DataRequired(),))
    #datetime = DateField(label='DateTime',format='%Y-%m-%d',validators=(validators.DataRequired(),))

    submit= SubmitField(label= 'Submit')
   # email = SubmitField(label = 'Reach out to Us!')

class AppointmentForm(FlaskForm):
  #  username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=10)])
    delete = StringField(label= 'Enter an ID to Delete:',validators=[Length(min=1, max=10)])
    submit = SubmitField(label= 'Submit')

class emailForm(FlaskForm):
    submit = SubmitField(label = 'Submit Email')

class adminForm(FlaskForm):
    #username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=40)])
    delete = StringField(label='Delete an appointment', validators=[DataRequired(), Length(min=1, max=10)])
    add= StringField(label='Add an appointment', validators=[DataRequired(), Length(min=1, max=10)])
    submit= SubmitField(label= 'Submit')

class addLawyer(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=10)])
    fname= StringField(label='First Name', validators= [DataRequired(), Length(max=20)])
    lname= StringField(label='Last Name', validators= [DataRequired(), Length(max=20)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label= 'Sign Up')
