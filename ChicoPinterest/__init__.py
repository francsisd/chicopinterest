# Local onde se cria o aplicativo e banco de dados
# pip install flask, flask-sqlalchemy, flask-login, flask-bcrypt, flask-wtf, email_validator
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__) # definir o nome do site
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "5587ecc388f2d95c3248e1f2a38da3f6"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"
#defini a linguagem do banco de dados, nesse caso "SQLite"
#Chave de segurança

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager =LoginManager (app)
login_manager.login_view = "homepage"


from ChicoPinterest import routes
# no arquivo init deve se fazer as importações no final do código
