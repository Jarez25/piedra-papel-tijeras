class MyPersona:
    pass

print('hola')

print(MyPersona)
print(MyPersona())


class Persona:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
    
Per = Persona('jarez', 'medina')
print(Per.name)


class gente:
    def __init__(self, nombre, apellido):
        self.total = f'{nombre} {apellido}'
        
    def walk (self):    
        print(f'{self.total} esta cantando')
        
gen = gente('jose', 'medina')
print(gen.total)
gen.walk()
