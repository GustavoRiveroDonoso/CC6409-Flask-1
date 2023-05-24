# CC6409-Flask
Deploy de un modelo de IA, usando PyTorch y FLask.
Se divide el modelo en 2 directorios:
* web: se encarga de la página web: renderizar el template HTML, enviar la POST con el texto a procesar y recibir la respuesta.
* AI-model: contiene la instancia del modelo y se encarga de procesar el texto que recibe en `server:5001/summ`
Para utilizarlo:
* Instalar PyTorch: `pip install torch`
* Instalar Flask: `pip install flask`
* Instalar transformers: `pip install transformers`
