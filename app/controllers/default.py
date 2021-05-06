from flask import render_template,flash
from flask.helpers import url_for
from flask.wrappers import Request
from app import app
from app.models.tables import DadosPacienteGlicemia, DadosPacientePressao, Exame
from app.models.forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import url_for
from app.models.forms import PrecadastroForm,DadosPacienteFormPressao, DadosPacienteFormGlicemia
from flask import Flask, request, url_for, redirect, render_template
from datetime import datetime
import json


@app.route("/cadastro",methods=['GET','POST'])
def index():
    form = PrecadastroForm()
    if form.validate_on_submit():
        senha = form.cpf.data[0:3]
        data = datetime.combine(form.data.data, datetime.min.time()) # converte pada datetime
        pc = Exame(form.video.data,form.nome.data,form.cpf.data,senha,form.pdf.data,form.procedimento.data,data)
        pc.save()
    
        flash("Cadastro realizado com sucesso","success")
        print(Exame.query.all())
     
    return render_template('cadastro.html',form=form)


@app.route("/paciente/<string:cpf>",methods=['GET','POST'])
def login(cpf):
    ex = Exame.query.filter_by(cpf=cpf).all()
    form = LoginForm()
    if form.validate_on_submit():
        senha = form.password.data
        if ex[0].password == senha:
            return render_template('lista.html',pessoa=ex)
        else:
            flash("Senha nao confere! caso tenha esquecido contate-nos!")

    if not ex:
        flash("Usuario nao encontrado");

    return render_template('exames.html',pessoa=ex,form = form)



@app.route("/formulario_pressao/<string:cpf>",methods=['GET','POST'])
def formulario_pressao(cpf):
    form = DadosPacienteFormPressao()
    form.cpf.data = cpf
    if form.validate_on_submit():
        form.save()
        flash("Dados enviados com sucesso!","success")
    else:
        print(form.errors)

    
    # show the form, it wasn't submitted
    return render_template('formulario_pressao.html',form = form,cpf=cpf)

@app.route("/formulario_glicemia/<string:cpf>",methods=['GET','POST'])
def formulario_glicemia(cpf):
    form = DadosPacienteFormGlicemia()
    form.cpf.data = cpf
    if form.validate_on_submit():
        form.save()
        flash("Dados enviados com sucesso!","success")
    else:
        print(form.errors)

    
    # show the form, it wasn't submitted
    return render_template('formulario_glicemia.html',form = form,cpf=cpf)

@app.route('/')
def hello_world():
    return render_template('exemplo.html')