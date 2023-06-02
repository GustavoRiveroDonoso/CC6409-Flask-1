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


"""
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/call_openai', methods=['POST'])
def call_openai():
    if request.method == 'POST':
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer YOUR_API_KEY'  # Reemplaza YOUR_API_KEY con tu clave de API de OpenAI
        }
        data = {
            'model': 'text-davinci-003',
            'prompt': '..<prompt>..',
            'temperature': 0.5,
            'max_tokens': 200
        }
        response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
        return response.json()

if __name__ == '__main__':
    app.run()
"""


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
        headers = {
            "MiEncabezado": "PongaAquiSuHeader"
        }
        apicall = requests.post(API_URL, files=files, headers=headers)
        #   Recibimos la respuesta
        if apicall.status_code == 200:
            summary = apicall.content.decode()
            error = None
            result = summary
        else:
            error = 'Error al procesar el texto'
            result = None
        
        #   Mostramos la respuesta
        prompt = "Resume esto pero sin comenzar con la frase en resumen: " + text['text']
        print("Este es nuestro prompt: " + prompt)
        data = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 200
        }
        # Configurar la autenticación con la clave de la API
        headersOpenIA = {
            "Authorization": "Bearer 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",
            "OpenAI-Organization": "org-hui8j2DuRQmRs8U1VJY11A4Q"

        }
        # Realizar la solicitud POST a la API de OpenAI
        response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headersOpenIA)
        # Obtener la respuesta generada por ChatGPT
        print("Aqui viene el response: ")
        print(response)
        if response.status_code == 401:
            error = 'Error de autenticación. Verifica tu clave de API.'
            return render_template('index.html', error=error)
        reply = response.json()["choices"][0]["text"]
        return render_template('index.html', result=result, result2=reply, error=error)
        #return render_template('index.html', result=result, error=error)
    


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(port=5000)
