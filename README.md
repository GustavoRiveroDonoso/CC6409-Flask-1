# CC6409-Flask
Deploy de un modelo de IA, usando PyTorch y FLask.\
El modelo utilizado está contenido en [HuggingFace](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization)
Se divide la app en 2:
* web: se encarga de la página web: renderizar el template HTML, enviar la POST con el texto a procesar y recibir la respuesta.
* AI-model: contiene la instancia del modelo y se encarga de procesar el texto que recibe en `server:5001/summ`
\
Para utilizarlo:
* Instalar PyTorch: `pip install torch`
* Instalar Flask: `pip install flask`
* Instalar transformers: `pip install transformers`
* Utilizar dos terminales para navegar hasta `\...\web` y `...\AI-model` y encada una lanzar la app con `python main.py`
* Para acceder local desde el navegador, simplemente ir a `127.0.0.1:5000` en el navegador que utilice.
