def suma_retona(min, max):
    suma = 0
    for x in range(min, max):
        suma += x
    return suma
    
resul = suma_retona(1, 10)
resul1 = suma_retona(20, 30)
resul2 =suma_retona(resul, resul + 10)

print(resul)
print(resul) 
print(resul2)