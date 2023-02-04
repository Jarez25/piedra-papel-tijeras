hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minutos = float(hour +  mins + dura % 60)
horas = minutos % 60

print({})