from functools import reduce

def suma_uno(valor):
    return valor + 1

def suma_dos(valor):
    return valor + 5

def suma_dos_y_uno(valor_1, valor_2, f_suma):
    return f_suma(valor_1 + valor_2)


print(suma_dos_y_uno(5, 10, suma_uno))
print(suma_dos_y_uno(20, 50, suma_dos))
print(suma_dos_y_uno(5, 10, suma_uno))


def suma_tr(original):
    def add(numero):
        return numero + 10 + original
    return add

valorv = suma_tr(1)

print((valorv(5)))
print((suma_tr(5)(5)))


numero = [2, 5, 8, 10, 21]


def mul(numero):
    return numero * 2

print(list(map(mul, numero)))
print(list(map(lambda numero: numero * 2, numero)))


def filtro_todos(numero):
    if numero > 10:
        return True
    return False


print(list(filter(filtro_todos, numero)))
print(list(filter(lambda numero: numero > 10, numero)))


def dos_valores(valor_uno, valor_dos):
    print(valor_uno)
    print(valor_dos)
    return valor_uno + valor_dos


print(reduce(dos_valores, numero))
