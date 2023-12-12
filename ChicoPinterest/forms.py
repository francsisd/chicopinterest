# Criar os formulários do projeto
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, FileField
#importa a estrutura que permite criar um formulario
"""Importa os campos que serão utilizados no formulário, sendo os utilizados:
String: texto
Password: senha (coloca asteristo ou bolinha invés de mostrar a senha
submit: botão que envia os dados"""
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
"""Importa os validadores que serão utilizados para validação de um campo, sendo os utilizados: 
Data: não permite que o campo fique vazio
Email: verifica se é um email válido
Equalto: verifica se um campo é igual ao outro
Lenght: limita um nº de caracteres para o campo
ValidationError: defini a mensagem que sera visualizada quando ocorrer um erro"""
from ChicoPinterest.models import Usuarios

class Formlogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome do Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirma_senha = PasswordField("Confirma senha", validators=[DataRequired(),EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar conta")

    def validate_email(self, email):
        usuarios = Usuarios.query.filter_by(email=email.data).first()
        if usuarios:
            return ValidationError("E-mail já cadastrado, faça login para continuar")

#obrigatorio ter a função "validate_" junto com o campo a ser verificado "email"
#está filtrando a classe "usuarios" no arquivo modelsverifica se o campo de email do sql, tem dados iguais a os dados inseridos no campo email do formulario(email.data)"""
# se o filtro encontrar o email inserido vai aparecer essa mensagem de erro

class Formfoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar foto")
