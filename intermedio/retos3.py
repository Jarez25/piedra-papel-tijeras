def finonacci():
    empiesa = 0
    siguiente = 1
    
    for numero in range(0, 51):
        print(empiesa)
        
        fibo = empiesa + siguiente
        empiesa = siguiente
        siguiente = fibo

finonacci()