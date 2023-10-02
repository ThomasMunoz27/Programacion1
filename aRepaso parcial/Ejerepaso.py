

#Metodo de pago
payment_validation = 0
freight_cost = 2500
#este sub total lo declaré aqui para que funcione la porción de código
sub_total = 15000
while payment_validation == 0:
    payment_method = input(f"¿Cuál va a ser el método de pago? \n Efectivo/Tarjeta \n ").lower()
    #validación de método de pago
    if payment_method == "efectivo" :
        if sub_total > 10000:
            total = sub_total - freight_cost
            break
        else:
            total = sub_total
    elif payment_method == "tarjeta":
        total = sub_total + (sub_total * 0.15)
        break
    else:
        print("Método ingresado inválido \n Intente otra vez. \n")

print(total)



print(10 % 3)