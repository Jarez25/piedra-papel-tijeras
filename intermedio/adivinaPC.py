import random as rd

def advina_el_numero_pc(x):
    
    
    print("============================")
    print("====welcome to the games====")
    print("============================")
    print(f"adivina el numero entre 1 y {x} la pc podra adivinarlo....?" )
    
    limit = 1 # limite superio
    limit_v2 = x # limite inferior
    
    resul = ""
    
    while resul != "c":
        if limit != limit_v2:
            prediccion = rd.randint(limit, limit_v2)
        else:
            prediccion = limit
        
        resul = input(f"Mi prediccion es{prediccion}. Si es muy alta ingresa: (A). Si es muy alta ingresa(B). Si es correcta ingresa (C) \n").lower()
        
        if resul == "a":
            limit = prediccion -1
        elif resul == "b":
            limit_v2 = prediccion + 1
    print(f"Felicidades  el ordenaro adivino tu numero: {prediccion}")
    
advina_el_numero_pc(100)