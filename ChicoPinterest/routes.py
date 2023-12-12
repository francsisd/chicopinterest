#criar as rotas do nosso site (links)
from flask import render_template, url_for, redirect
"""render_template: para que a associação seja feita entre essa e outra página,
 é necessário que a pasta se chame "templates".
 url_for: usado para que mesmo que voçê mude o url do site, não precise trocar o caminho em todos códigos que mencionar ele."""
from ChicoPinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from ChicoPinterest.forms import Formlogin, FormCriarConta, Formfoto
from ChicoPinterest.models import Usuarios, Fotos
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = Formlogin()
    if form_login.validate_on_submit():
        usuarios = Usuarios.query.filter_by(email=form_login.email.data).first()
        if usuarios and bcrypt.check_password_hash(usuarios.senha, form_login.senha.data):
            login_user(usuarios, remember=True)
            return redirect(url_for("perfil", id_usuario=usuarios.id))
    return render_template("homepage.html", form=form_login)


#definir qual caminho voçê deseja ir, no caso somente o "/" é para ir para a homepage o "methods" vem definido com o valor padrão GET: significa que o usario vai receber informações do site. e o POST: significa que o usuario vai forecer informações pro site, utilizada em formularios
# ele ira acessar o arquivo homepage dentro da pasta templates

@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha= bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuarios(username=form_criarconta.username.data, senha=senha, email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("cadastro.html", form=form_criarconta)

@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form_foto= Formfoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            foto = Fotos(imagem=nome_seguro, id_usuario=id_usuario)
            database.session.add(foto)
            database.session.commit()
        return render_template("Perfil.html", usuario=current_user, form=form_foto)
    else:
        usuario = Usuarios.query.get(int(id_usuario))
        return render_template("Perfil.html", usuario=usuario, form=None)
# só deixa que o usuario vá para a página perfil se ele tiver logado

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    fotos=Fotos.query.order_by(Fotos.data_criacao).all()
    return render_template("feed.html", fotos=fotos)
