from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import Email, DataRequired, Length


class report_form(FlaskForm):
    hora_de = DateTimeField("De",validators=[
        DataRequired("Campo obrigatório!")
    ])
    submit = SubmitField("Cadastrar")

class RegisterForm(FlaskForm):
    name = StringField("Nome", validators=[
        DataRequired("Campo obrigatório!"),
        Length(5, 100, "O campo deve possuir entre 5 e 100 caracteres")
    ])
    email = StringField("E-mail", validators=[
        DataRequired("Campo obrigatório!"),
        Email('não é um e-mail válido'),
        Length(5, 100, "O campo deve possuir entre 5 e 100 caracteres")
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("Campo obrigatório!")
    ])
    submit = SubmitField("Cadastrar")

class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[
        DataRequired("Campo obrigatório!"),
        Email('não é um e-mail válido')
    ])
    password = PasswordField("Senha", validators=[
        DataRequired("Campo obrigatório!")
    ])
    submit = SubmitField("Cadastrar")