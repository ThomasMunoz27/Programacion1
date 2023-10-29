import sys
sys.path.append("C:/Users/sonic/OneDrive/Escritorio/GitHub/Programacion1/TPs_Ejerciciosy_Funciones/aClases")
from Persona import Person
from Cuenta import Count
from Triangulo import Triangle

#Ejercicio 1
'''
p1 = Person("Thomas", 17, 94219667)
p2 = Person()
p2.set_name("Paula")
p2.set_dni(44593085)
p2.set_age(20)
p2.set_blood_type("o+")

p1.show_info()
print()
p2.show_info()
p1.adult()
p2.adult()
'''
#Ejercicio 2
'''
c1 = Count("Thomas Muñoz", 38522.59)

c1.show_info()
c1.set_amount(2000.0)
c1.show_info()
c1.set_amount(-5000.0)
c1.show_info()
c1.entry_money(5)
c1.entry_money(-5)
c1.withdraw(6)
c1.withdraw(-6)
'''

#Ejercicio 3
t1 = Triangle("a", 10, 5, 6)

print(t1.set_tria_type("equilátero"))