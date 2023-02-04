import random

paises = ['col', 'mex', 'bol', 'nic']

pueblo = { pais: random.randint(1, 100) for pais in paises }
print(pueblo)

resultado = {pais: poblacion for(pais, poblacion) in pueblo.items() if poblacion > 20}
print(resultado)

text = 'hola soy jarez'

unique = {caracter: caracter.upper() for caracter in text if  caracter in 'aeiou'}
print(unique)