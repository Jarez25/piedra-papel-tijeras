import random

paises = ['col', 'mex', 'bol', 'nic']
pueblo = {}

for pais in paises:
  pueblo[pais] = random.randint(1, 100)

print(pueblo)

pueblodos = {pais: random.randint(1, 100) for pais in paises}
print (pueblodos) 


names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]  

print(list(zip(names ,ages)))

newDict = {name: age for (name, age)in zip(names, ages)}
print(newDict)

{
    'nico':12,
    'zule':56,
    'santi':98
}
'''

dict = {}

for i in range (1, 5):
    dict[i] = i * 2
    
    
print(dict)

dictdos = {i: i * 2 for i in range(1, 5)}
print(dictdos)

'''

