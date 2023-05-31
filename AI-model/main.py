from app import app, DEBUG
from utils import summarize
from flask import Flask, jsonify, request, abort

#   En servidor:5001/summ esta app recibe los POST con los textos para procesar
@app.route('/summ', methods=['POST'])
def submit():
    mi_encabezado = request.headers.get('MiEncabezado')
    if (mi_encabezado != "PongaAquiSuHeader"):
        # Hacer algo aqui
        print("Header equivocado")
        print(mi_encabezado)
        abort(401)
    else:
        print("Header correcto")
        #   request contiene la informacion entregada en la request
        file = request.files['texto']
        #   en este caso request.files['texto'] contiene el texto
        text =  (file.read()).decode()
        #   se usa la funcion summarize definida en utils
        if DEBUG:
            print(text)
        result = summarize(text)
        return result

if __name__ == "__main__":
    app.run(port=5001)
