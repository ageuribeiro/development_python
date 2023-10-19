from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from config import *

app =  Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkeysissecretkeys'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

#homepage
@app.route("/")
@app.route("/home")
def home():
    title='Bem-vindos'
    return render_template('index.html', title=title)

#aboutpage
@app.route("/about")
def about():
    title='Bem-vindos'
    return render_template('about.html', title=title)

#aboutpage
@app.route("/vitrine")
def vitrine():
    title='Bem-vindos'
    return render_template('vitrine.html', title=title)

#aboutpage
@app.route("/contatos")
def contatos():
    title='Bem-vindos'
    return render_template('contatos.html', title=title)

#aboutpage
@app.route("/login")
def login():
    title='Acesso ao Sistema'
    loja = nome_loja
    return render_template('sistema/index.html', title=title, loja=loja)

#aboutpage
@app.route("/register")
def register():
    title='Create new account'
    return render_template('sistema/register.html', title=title)

db.create_all()
if __name__=='__main__':
    app.run(debug=True, port=9000)