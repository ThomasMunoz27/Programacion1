print("Ingresar los coeficientes de una ecuacion de primer grado ax + b = 0")
a=int(input("a="))
b=input("b=")


if a==0 and b!=0:
    print("No hay solución")
elif a!=0 and b== "-x":
    print("infinitas soluciones")
elif a!=0 :
    b=int(b)
    x=-b/a
    print("la solución es x= ", x)