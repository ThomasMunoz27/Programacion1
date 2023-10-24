#Ejercicio 1
abc = "abcdefghijklmnñopqrstuvwxyz"

corr = int(input("Ingrese el corrimiento: "))
for cant_msg in range(5):
    msg = input(f"Ingrese el menasaje para el oficial {cant_msg+1} a encriptar: ")
    msg_encript = ""
    for letter in msg:
        frts_l = abc.find(letter)
        if letter == " ":
            msg_encript = msg_encript + " "
        else:
            msg_encript = msg_encript + abc[(frts_l + corr)%27]
    print(msg_encript)




#Ejercicio 2

stop = 1
total_pair = 0
total_odd = 0


while stop !=0:

    num_str = (input("Ingrese números enteros positivos. Para detenerse presione 0: "))
    parc_odd = 0
    parc_pair = 0
    for i in range(0, len(num_str)):

        num_str = int(num_str)
        if num_str == 0:
            stop = 0
        elif num_str < 0:
            print("Número ingresado inválido")
            break
        else:
            num_str = str(num_str)
            num = num_str[i]
            num = int(num)
            if num % 2 == 0:
                parc_pair = parc_pair + 1
                total_pair = total_pair + 1
            else:
                total_odd = total_odd +1 
                parc_odd = parc_odd + 1
    if num_str != 0:
        print(f"Se leyeron {parc_odd} números impares y {parc_pair} números pares")
print(f"Se leyeron un total de {total_pair} números pares y {total_odd} números impares")


