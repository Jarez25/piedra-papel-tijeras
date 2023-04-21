import random

def advina_el_numero(x):
    
    
    print("============================")
    print("====welcome to the games====")
    print("============================")
    print("adivina el numero o muere")
    
    
    numer_random = random.randint(1, x)
    predecir = 0
    
    while predecir != numer_random:
        predecir = int(input(f"Adiviana un numero entre 1 y {x}: \n"))
        if predecir < numer_random:
            print("este numero es menor puedes probar de nuevo")
        elif predecir > numer_random:
            print("este numero es muy grande puedes probar de nuevo")
    print(f"Feliciadades adivinaste el numero {numer_random} correctamente.")
    
advina_el_numero(1000)