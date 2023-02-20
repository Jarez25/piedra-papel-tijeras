lista = list()
lista_v2 = []
lista_original = [35, 24, 62, 52, 62, 30, 30, 17]
lista_original_v2 = [1, 2, 3, 4, 5, 6, 7]

other_lista = [i*i for i in range(10)]

print(type(lista))
print(type(lista_v2))
print(len(lista_original_v2))
print(lista_original_v2)
print(other_lista)
print(len(other_lista))


def suma (numero):
    return numero +5

other_lista = [suma(i) for i in range(10)]

print(other_lista)