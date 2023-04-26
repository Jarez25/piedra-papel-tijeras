import hashlib 


encontrar = 0
entradas = input("ingresa la pass \n")
pass_dicc = input("ingresa el diccionario \n")

try:
    pass_files = open(pass_dicc, 'r')
except:
    print("error" + pass_dicc + "no ha sido encontrada")
    
for palabra in pass_files:
    palabra_cifrada = palabra.encode('utf-8') 
    palabra_encontrada = hashlib.md5(palabra_cifrada.strip())
    digest == palabra_encontrada.hexdigest()
    
    if digest == entradas:
        print("password encontrada \n la password es" + palabra)
        encontrar = 1
        break

if not encontrar:
    print("pasword no encontrada en el archivo " + palabra)