import socket

def ip_to_binary(ip_address):
    # Convierte la dirección IP a un número decimal
    decimal = int(socket.inet_aton(ip_address).hex(), 16)
    # Utiliza la función bin() para convertir el número decimal a binario
    return bin(decimal)[2:]

# Prueba del programa
ip = "10.101.99.228"
binary = ip_to_binary(ip)
print("La dirección IP", ip, "es equivalente a", binary, "en binario.")
