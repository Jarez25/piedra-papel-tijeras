def anagrama(letra_uno, letra_dos):
    if letra_uno.lower() == letra_dos.lower():
      return False
    return sorted(letra_uno.lower()) == sorted(letra_dos.lower())

print(anagrama('Amor','Roma'))