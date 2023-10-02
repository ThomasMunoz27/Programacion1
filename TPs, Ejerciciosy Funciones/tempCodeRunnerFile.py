import aFunciones as funcion
try:
    frecuency = 0
    num = int(input("Ingrese un número entero: "))
    #separar el número
    num = funcion.separate_num(num)
    while True:
        digit = (input("Ingrese un dígito: "))
        if len(digit) > 1:
            print("Ingrese solamente un dígito")
        else:
            break
    frecuency = funcion.determ_frec(digit, frecuency, num)
    print(f"El número {digit} aparece {frecuency} veces en el número {('').join(num)}")
except ValueError:
    print("Ingrese solamente números")
