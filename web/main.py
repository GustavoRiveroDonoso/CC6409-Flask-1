# -*- coding: utf-8 -*-s
import os
import json
from app import app, API_URL, DEBUG
import requests
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from utils import allowed_file
import secrets
import codecs


@app.route('/')
def index_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_image():
    text = request.form
    if text== '':
        error = 'No se seleccionó ningún texto'
        return render_template('index.html', error=error)
    
    else:
        #   Guardaremos los textos
        #   hash para evitar sobreescribir
        filename = secrets.token_hex(nbytes=8)+'.txt' #+ '_' + secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file = open(filepath, 'w+')
        file.write(text['text'])
        file.close()

        #   Creamos la POST request, con el texto a procesar, para enviarla a server:5001/summ
        files = {'texto': codecs.open(filepath, 'rb')}
        if DEBUG:
            print(files['texto'])
        apicall = requests.post(API_URL, files=files)

        #   Recibimos la respuesta
        if apicall.status_code == 200:
            summary = apicall.content.decode()
            error = None
            result = summary
        else:
            error = 'Error al procesar el texto'
            result = None
        
        #   Mostramos la respuesta
        return render_template('index.html', result=result, error=error)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(port=5000)
