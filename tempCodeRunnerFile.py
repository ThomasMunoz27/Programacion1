abc = "abcdefghijklmnñopqrstuvwxyz"

corr = int(input("Ingrese el corrimiento: "))
for cant_msg in range(5):
    msg = input(f"Ingrese el menasaje para el oficial {cant_msg+1} a encriptar: ")
    msg_encript = ""
    for letter in msg:
        frts_l = (abc.find(letter))
        if letter == " ":
            msg_encript = msg_encript + " "
        else:
            msg_encript = msg_encript + abc[(frts_l + corr)%27]
    print(msg_encript)

