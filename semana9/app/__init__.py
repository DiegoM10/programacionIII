
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route("/exito/<nombre>")
def exito(nombre):
    return "Bienvenido, %s" % nombre

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usuario = request.form["nm"]
        return redirect(url_for("exito", nombre=usuario))
    else:
        usuario = request.args.get("nm")
        return redirect(url_for("exito", nombre=usuario))

if __name__ == "__main__":
    app.run(port=5051)





#from flask import Flask
#app = Flask(__name__)

#@app.route("/")   #app.route = decorador,resume algo.
#def hola_mundo():
 #   return "Xopa laope!"
#@app.route("/hola/<nombre>/") #<nombre>= variable tipo cadena
#def hola_laope(nombre):
 #   return "Hola laope, %s!" % nombre

#@app.route("/blog/<int:idEntrada>") #<nombre>= variable tipo cadena
#def mostrar_blog(idEntrada):
 #   return "Entrada #%d" % idEntrada

#@app.route("/itbms/<float:subtotal>") #<nombre>= variable tipo cadena
#def calcular_itbms(subtotal):
 #   return "Impuesto de  $%.2f, es $%.2f!"% (subtotal,subtotal*0.007)

#if __name__ == "__main__":
    #app.run()