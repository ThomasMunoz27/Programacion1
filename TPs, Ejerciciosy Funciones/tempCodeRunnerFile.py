import aFunciones as funcion
size = int(input("Ingrese la medida de la hoja A(N): "))
print(f"El tamaño de la hoja A{size} es :")
final_size = funcion.calc_size(size)
print(f"{final_size[0]}mm x {final_size[1]}mm")