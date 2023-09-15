salary = 20000
aux = 0
conf_asist = input("¿Asistió todo el més? \n (Si/No): ").lower
if conf_asist == "si":
    
        extra_hours = int(input("¿Cuantas horas trabajó los domingos? (min:3 Max:10)"))
        if extra_hours < 3 or extra_hours > 10: 
            print("Cantidad de horas extra ingresadas inválido. Ingrese de vuelta. \n")
        elif extra_hours >=3 or extra_hours <= 5:
            salary += salary * 0.03
            
        elif extra_hours >=6 or extra_hours <= 10:
            salary += salary * 0.1
            

elif conf_asist == "no":
        extra_hours = int(input("¿Cuantas horas trabajó los domingos?(Min:3 Max:10)"))
        if extra_hours < 3 or extra_hours > 10: 
                print("Cantidad de horas extra ingresadas inválido. Ingrese de vuelta. \n")
        else:
            salary += salary * 0.02
            


print(f"Su salario final es de {salary}")
