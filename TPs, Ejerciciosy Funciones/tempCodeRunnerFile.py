import aFunciones as funcion
num = int(input("Ingrse un número para saber si es par o impar: "))
val_par = funcion.par(num)
val_imp = funcion.impar(num)
print(f"¿El número {num} es par?:{val_par}")
print(f"¿El número {num} es impar?: {val_imp}")
