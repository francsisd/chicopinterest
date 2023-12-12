# mantém as estruturas do banco de dados

from ChicoPinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuarios(id_usuarios):
    return Usuarios.query.get(int(id_usuarios))
# serve para falar que a função "load_usuarios, é a função que carrega o usuario
# Essa função recebe o id do usuario e retorna quem é o usuario

class Usuarios(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Fotos", backref="usuarios", lazy=True)

class Fotos(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False)