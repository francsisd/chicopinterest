from ChicoPinterest import database, app
from ChicoPinterest.models import Usuarios, Fotos

with app.app_context():
    database.create_all()