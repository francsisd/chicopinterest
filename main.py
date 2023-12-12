# um projeto flask precisa que tenha um arquivo fora do projeto para que se possa inicia-lo, esse é o main.py
from ChicoPinterest import app


if __name__ == "__main__":
    app.run(debug=True)
# para que as alterações feitas no código já apareçam no site