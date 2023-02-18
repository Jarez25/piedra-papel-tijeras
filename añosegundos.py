segundos = 60
minutos = 60
hora = 60
dia = 24
semana = 7
año = 365
año_bisiesto = 366
añosemana = 52.1429
resul = segundos * minutos 
resulDia = resul * dia
resulSemana = resulDia * semana
semanahora = dia * semana
horaño = semanahora * añosemana
horaño = round(horaño)


print(resul)
print(resulDia)
print(resulSemana)
print(semanahora)
print(horaño)


