# -*- coding: utf-8 -*- 
from app import model, tokenizer, device
import io

DEBUG = False

def summarize(text):
    if DEBUG:
        print('/////////////////////////////////')
        print(text)
        print('/////////////////////////////////')

    #   tokenizer recibe el texto (String) y entrega inputs_ids y attention_mask, que son Tensor, el tipo que usa Pytorch para los vectores / tensores
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    #   Llamamos al modelo, este nos entrega tensores, no texto
    output = model.generate(input_ids, attention_mask=attention_mask)

    #   Entonces decodificamos este resultado con el tokenizer
    summary =  tokenizer.decode(output[0], skip_special_tokens=True)
    return summary
    