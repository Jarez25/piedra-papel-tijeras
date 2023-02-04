import socket
import tkinter as tk

def find_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    hostname_label.config(text=f'El nombre de tu ordenador es {hostname}')
    ip_label.config(text=f'La dirección IP de tu ordenador es {ip}')

root = tk.Tk()
root.title("IP Finder")

hostname_label = tk.Label(root, text="")
hostname_label.pack()

ip_label = tk.Label(root, text="")
ip_label.pack()

find_ip_button = tk.Button(root, text="Find IP", command=find_ip)
find_ip_button.pack()

root.mainloop()