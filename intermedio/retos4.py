
def prima():

    for numero in range(1, 101):

        if numero >= 2:

            div = False

            for index in range(2, numero):
                if numero % index == 0:
                    div = True
                    break

            if not div:
                print(numero)


prima()