
from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route("/admi")
def hola_admi():
    return "Xopa Admi"


@app.route("/mortal/<mortal>")
def hola_mortal(mortal):
    return "Larga de aqui mortal, %s" %mortal

@app.route("/usuario/<nombre>")
def hola_usuario(nombre):
    if nombre == "admin":
        return redirect(url_for("hola_admi"))
    else:
        return redirect(url_for("hola_mortal",mortal=nombre))

if __name__ == "__main__":
    app.run()