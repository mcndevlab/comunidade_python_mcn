#Arquivo para inicializar o programa
#Da linha 02 a linha 12 migrou do main.py para __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

#Aula 11 Criando os Usuarios
app.config['SECRET_KEY'] = '75a5e191f27e56ab0e53ae19d10d2bec'

#O código abaixo seleciona o BD tanto para qdo estiver no ambiente local como para qdo estiver em rede
#O DATABASE_URL é uma variável presente do BD postgreSQL do railway, estando presente esta variável o python
#Utilizara ela, não estando vai procurar o BD local.
#if os.getenv("DATABASE_URL"):
#    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
#else:
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:chuTAKuLIKUdaKTVOiFzqGJpbvsmSrdb@roundhouse.proxy.rlwy.net:54955/railway'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspect = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados criada")
else:
    print("Base de dados já existente")


from comunidadeimpressionadora import routes
