
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


print(f'El nombre de tu ordenador es .{hostname}')

print(f'el op de tu ordenador es. {ip}') 