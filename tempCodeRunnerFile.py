num_list = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
find_num = int(input("Ingrese el número que desea buscar: "))
for i in num_list:
    if find_num == num_list[i]:
        print(f"Se encontró el número {num_list[i]}")
        break

print("Fin del programa")