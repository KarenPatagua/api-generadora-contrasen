from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

@app.route('/', methods=['GET', 'POST'])
def index():
    contrasena = ""
    if request.method == 'POST':
        longitud = int(request.form.get("longitud", 12))
        contrasena = generar_contrasena(longitud)
    return render_template('index.html', contrasena=contrasena)

if __name__ == '__main__':
    app.run(debug=True)
