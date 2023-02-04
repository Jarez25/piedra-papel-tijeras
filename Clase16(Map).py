ingredientes = ('carne', 'maiz', 'aguacate')
ingredientes_2 = ('molida', 'tacos', 'guacamole')
menu = list(map(lambda a, b: a + ' es a ' + b, ingredientes, ingredientes_2))
print(menu)


paginas = ('html', 'css', 'javascript')
tecnologias = ('primero', 'segundo', 'tercero')

aprender = list(map(lambda curso, logica: curso + ' es tu nivel ' + logica, paginas, tecnologias))
print(aprender)


numero = [1, 2, 3, 4]
numerodos = []
for i in numero:
       if numero == numerodos:
           print('hola mundo')
numerodos.append(i * 2)

listUno = [1, 2, 3, 4]
listaDos = [ 5, 6, 7, 8]

listaResul = list(map(lambda x, y : x + y, listUno, listaDos))


numeroTres = list(map(lambda i: i * 2 , numero))
print(numero)
print(numerodos)
print(numeroTres)
print(listaResul)