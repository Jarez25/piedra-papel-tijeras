'''

numeros = []

for elemento in range(1, 11):
    numeros. append(elemento)

print (numeros)

numerodos = [elemento for elemento in range(1, 13)]
print(numerodos)


calculo = [i*2 for i in range (1, 100)if i % 2 == 0]
print(calculo)

'''
numeros = []

for elemento in range(1, 11):
    if  elemento % 2 == 0:
        numeros. append(elemento * 2)

print (numeros)


numerodos = [ i * 2 for i in range(1, 50) if i % 2 == 0]
print(numerodos)

