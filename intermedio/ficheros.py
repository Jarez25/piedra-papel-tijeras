import os

txt = open("intermedio/my_file.txt", "w+")


for line in txt.readlines():
    print(line)


txt.write('\n prueba de añadir codigo')

txt.close()


##os.remove("intermedio\my_file.txt")