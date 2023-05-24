# CC6409-Flask
Deploy de un modelo de IA, usando PyTorch y FLask.\
El modelo utilizado está contenido en [HuggingFace](https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization)
Se divide la app en 2:
* web: se encarga de la página web: renderizar el template HTML, enviar la POST con el texto a procesar y recibir la respuesta.
* AI-model: contiene la instancia del modelo y se encarga de procesar el texto que recibe en `server:5001/summ`
---
### Para utilizarlo:
* Instalar PyTorch: `pip install torch`
* Instalar Flask: `pip install flask`
* Instalar transformers: `pip install transformers`
* Utilizar dos terminales para navegar hasta `\...\web` y `...\AI-model` y encada una lanzar la app con `python main.py`
* Para acceder local desde el navegador, simplemente ir a `127.0.0.1:5000` en el navegador que utilice.
---
### Recomendaciones:
* Fijarse bien en qué recibe como input y retorna cada función, en el caso de texto el modelo (CNN, transformer, BETO, etc.) *no* recibe un String, 
hay que preprocesarlo con `Tokenizer`
* Cargar sólo una vez el modelo: tanto si lo descargan (como en este ejemplo), como si lo cargan de un archivo (ej: `torch.load('mi_modelo.bin')`), la idea
es que cada vez que tengan que procesar información (en este caso recibida por un `POST` que contiene el texto que sube el/la/le user) utilicen el mismo modelo,
no que tengan que cargarlo cada vez.
* Entrenar en GPU, para lo cual recomiendo crear un notebook en [Colab](https://colab.research.google.com/) si no tienen una GPU o no es tan potente 
(si lo usan cambien el entorno de ejecución a GPU). Después al momento de correr el modelo no es necesario que sea en GPU, puesto que correrlo (en este caso con 
`model.generate()`, pero también puede ser `mi_modelo.forward()` u otros) es menos pesado y en CPU entrega tiempos razonables.
* Usar modelos que ya conozcan o de los que puedan encontrar una referencia de cómo se comportan y cómo implementarlo, 
no es necesario que tengan modelos ultra complejos, LLM, generativos, con boosting, etc., pues puede que ni quepan en GPU.
