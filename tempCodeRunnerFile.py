#Ejercicio 1
abc = "abcdefghijklmnñopqrstuvwxyz"

corr = int(input("Ingrese el corrimiento: "))
for cant_msg in range(5):
    msg = input(f"Ingrese el menasaje {cant_msg+1} a encriptar: ")
    msg_encriptado = ""
    for letra in msg:
        indice = (abc.find(letra))
        if letra == " ":
            msg_encriptado = msg_encriptado + " "
        else:
            msg_encriptado = msg_encriptado + abc[(indice + corr)%27]
    print(msg_encriptado)
