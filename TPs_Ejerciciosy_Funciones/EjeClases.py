import sys
sys.path.append("C:/Users/sonic/OneDrive/Escritorio/GitHub/Programacion1/TPs_Ejerciciosy_Funciones/aClases")
from Motocicleta import Motorcycle


moto1 = Motorcycle("Rojo", "S3X666", 2, 10, "Honda", "AX-100", "2022/12/25", 60, 150)

moto2 = Motorcycle("Negro", "S3X777", 2, 10, "Honda", "AX-100", "2022/12/25", 60, 150)

moto3 = Motorcycle("Aqua", "DSR456", 2, 10, "Vespa", "GTS Super 125", "2019/12/25", 144, 120)

moto1.turn_on()
moto1.turn_on()

moto1.turn_off()
moto3.turn_off()

moto1.price = 79999

print(f"El precio de la moto {moto1.color}, marca {moto1.mark} y {moto1.model} es de : ${moto1.price}")

moto1.consult_price()
moto2.consult_price()