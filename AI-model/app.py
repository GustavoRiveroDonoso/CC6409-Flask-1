# -*- coding: utf-8 -*- 
import json
from transformers import BertTokenizerFast, EncoderDecoderModel
from flask import Flask

app = Flask(__name__)

#
#   App contiene el modelo de IA, en este cargo se descarga, pero tambien se puede abrir el binario de un modelo (ej: mi_modelo.bin) 
#   desde PyTorch
#

#   Opcional: device = 'cuda' if torch.cuda.is_available() else 'cpu'
device = 'cpu'

#   El tokenizer preprocesa el texto, recibe un texto (String) y entrega un diccionario con los inputs_ids y mascaras de atencion,
#   que se entregan posteriormente al modelo 
tokenizer = BertTokenizerFast.from_pretrained('mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization')
model = EncoderDecoderModel.from_pretrained('mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization').to(device)

DEBUG = True