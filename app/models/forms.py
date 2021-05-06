from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import Numeric
from wtforms import StringField, PasswordField, BooleanField,FileField, DateField,FloatField,HiddenField,RadioField
from wtforms.validators import DataRequired,ValidationError
from flask_wtf.file import FileAllowed, FileRequired
from .forms_validate import validate_cpf
from app.models.tables import DadosPacienteGlicemia, DadosPacientePressao

class LoginForm(FlaskForm):
    password = PasswordField("password", validators=[DataRequired()])

def ValidFloat():
    def ValidFloat_validator(form, field):
        try:
            field.data = field.data.replace(",",".")
            float(field.data.replace(",","."))
        except:
            raise ValidationError(f'Valor inválido, digite um valor conforme exemplo -> 23,2 ou 23')
    return ValidFloat_validator

class PrecadastroForm(FlaskForm):
    procedimento    = StringField("procedimento", validators=[DataRequired()])
    nome            = StringField("nome", validators=[DataRequired()])
    cpf             = StringField("cpf", validators=[DataRequired(),validate_cpf])
    pdf             = StringField("pdf", validators=[DataRequired()])
    video           = StringField("video", validators=[DataRequired()])
    data            = DateField('Start Date', format='%d/%m/%Y', validators=[DataRequired()])

class DadosPacienteFormPressao(FlaskForm):
    cpf                         = HiddenField("cpf")
    pressao_sistolica           = StringField("pressao_sistolica", validators=[ValidFloat()])
    pressao_diastolica          = StringField("pressao_diastolica", validators=[ValidFloat()])
    pulso                       = StringField("pulso", validators=[ValidFloat()])

    def save(self):
        obj = DadosPacientePressao(self.cpf.data,self.pressao_sistolica.data,self.pressao_diastolica.data,self.pulso.data)
        obj.save()

class DadosPacienteFormGlicemia(FlaskForm):
    cpf                         = HiddenField("cpf")
    glicemia                    = StringField("glicemia", validators=[ValidFloat()])
    dado                        = RadioField("CAJ",choices=[('cafe','2h após o café da manhã'),('almoco','2h após o almoço'),('janta','2h após a janta')])

    def save(self):
        cafe,almoco,janta = (x == self.dado.data for x in ['cafe','almoco','janta'])
        obj = DadosPacienteGlicemia(self.cpf.data,self.glicemia.data,cafe,almoco,janta)
        obj.save()


