from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Novos Testes"

if __name__ == '__main__':
    app.run()