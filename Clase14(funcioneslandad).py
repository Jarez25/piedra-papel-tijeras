def imcrementar(valor):
    return valor + 1


resul = imcrementar(10)
print(resul)

t = lambda var : var + 1

resul = t(20)
print(resul)

fullName = lambda name, lastName: f'full name is {name.title()} {lastName.title()}'
name = fullName('jarez', 'medina suarez')
print(name)


suma = lambda x, y: x + y
print(suma(3, 4)) # 7

lista = [("anna", 20), ("jose", 18), ("pedro", 25)]
lista.sort(key=lambda x: x[1])
print(lista) # [("jose", 18), ("anna", 20), ("pedro", 25)]

cuadrado = lambda x: x ** 2
print(cuadrado(5)) # 25

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtrado = filter(lambda x: x%2 == 0, lista)
print(list(filtrado)) # [2, 4, 6, 8, 10]

lista = [1, 2, 3, 4, 5]
resultado = map(lambda x: x*2, lista)
print(list(resultado)) # [2, 4, 6, 8, 10]

from functools import reduce
lista = [1, 2, 3, 4, 5 ,6 ,7]
resultado = reduce(lambda x, y: x+y, lista)
print(resultado) # 15

validacion = lambda x: len(x) > 6 and x.isalnum()
print(validacion("contraseña123")) # True
print(validacion("123456")) # False


mul = lambda multi: multi * 2
print(mul(20))



