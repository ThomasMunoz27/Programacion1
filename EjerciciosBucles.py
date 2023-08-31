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




#Ejercicio while

parar = 1
pares = 0
impares = 0
while parar !=0:
    num = int(input("Ingrese números enteros positivos. Para detenerse presione 0"))
    if num == 0:
        parar = 0
    elif num < 0:
        print("Número ingresado inválido")
    else:
        if num % 2 == 0:
            pares = pares +1
        else:
            impares = impares + 1

print(f"Se han ingresado {pares} números pares y {impares} números impares")