def incremento(x):
    return x + 1


def highOrdFunc(x, funcion):
    return x + funcion(x)

auto = lambda x: x + 1

orden = lambda x, funcion : x + funcion(x)
valor = orden(5, auto)

print(valor)

resul = highOrdFunc(5, incremento)

print(resul)


