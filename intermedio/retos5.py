def invertir(text):
    texto_len = len(text)
    texto_invertido = ''
    for texto in range(0, len(text)):
        texto_invertido  += text[texto_len - texto -1]
    return texto_invertido
    

print(invertir('hola mundo'))