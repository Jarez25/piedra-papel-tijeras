
suma = lambda numero_uno, numero_dos: numero_uno + numero_dos

print(suma(10, 25))



mul = lambda numero_uno, numero_dos: numero_uno *  numero_dos
print(mul(3,12))

def normas(valores):
    return lambda v_1, v_2,: v_1 + v_2 + valores


print(normas(5)(2, 4))