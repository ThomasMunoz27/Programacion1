"""Es un programa de una tienda mayorista de ropa para armar pedidos. Va a contener: 
    Lista de ropa con el stock dsopinible que puede ver el usuario con los precios
    preguntar quien hace el pedido.
    preguntar ¿Cuantos tipos de articulos va a comprar? (para armar un for)
    Preguntar el articlulo y la cantidad del articulo que va a comprar
    (cada caja tiene un máximo de 10 articulos)
    +
    Al final tiene que mostrar la cantidad total de articulos y la cantidad de cajas que se armaron.

    Preguntar el método de pago y hacer un recago del 15% si se paga con tarjeta.
    Si la compra es en efectivo y supera los $100000 pesos el envío es gratis.
    """


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



