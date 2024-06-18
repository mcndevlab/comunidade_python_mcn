#Arquivo com todas as bases e tabelas do banco de dados
from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, )
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True) #conexão com POST Relacionamento entre classes
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)




class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
#id_usuario = id da Class Usuario, mas não pode repetir o nome, dentrp do "()" da chave estrangeira só pode colocar
#letra minuscula, por isso está como('usuario.id') mas se reporta a Classe Usuário tabela id.
#A chave estrangeira precisa obrigatoriamenet ser o 2° item, dentro do parentesis. Primeiro argumentos de posição
#e por ultimo argumentos de Key word
