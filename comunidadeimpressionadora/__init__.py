#Arquivo para inicializar o programa
#Da linha 02 a linha 12 migrou do main.py para __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#Aula 11 Criando os Usuarios
app.config['SECRET_KEY'] = '75a5e191f27e56ab0e53ae19d10d2bec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes