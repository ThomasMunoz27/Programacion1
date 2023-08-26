sex = input("Ingrese su sexo(Hombre/Mujer: ")
sex = sex.lower()
name = input("Ingrese su nombre: ")
name_inicial = name[0]

if name_inicial < "m" and sex == "mujer":
    print("Usted pertenece al grupo A")
elif name_inicial > "m" and sex == "mujer":
    print("Usted pertenece al grupo B")
elif name_inicial > "n" and sex == "hombre":
    print("Usted pertenece al grupo A")
elif name_inicial < "n" and sex == "hombre":
    print("Usted pertenece al grupo B")
else:
    print("Usted no pertenece a ningún grupo")