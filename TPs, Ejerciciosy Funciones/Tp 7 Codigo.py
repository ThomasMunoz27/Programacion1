import aOrdenamientos as orden

#Ejercicio 1
nums = [9,8,7,6,5,4,3,21,1]
print(orden.bubble_sort(nums))


#Ejercicio 2
import aOrdenamientos as orden
letters = ["f","a","y","o","A","h","c","b"]
print(orden.selection_sort(letters))


#Ejercicio 3
import aFunciones as funcion
books = [{
    "titulo":"libro 1",
    "fecha":1998,
    "autor": "Pepe"
},
{
    "titulo":"Mordida",
    "fecha":1987,
    "autor": "Scot"
},
{
    "titulo":"JoJo SBR",
    "fecha":2004,
    "autor": "Araki"
}]
print("Ordenados por autor")
authors = []
for i in range(0, len(books)):
    for keys in books[i]:
        if keys == "autor":
            authors.append(books[i][keys])
print(authors)
print(funcion.order_books(authors, books))


#Ejercicio 4
import aFunciones as funcion
sentences_list = ["Manzana", "manzana","Vaca muerta", "palanca", "Pablo falleció", "Uva", "America no existe", "Spiderman", "España", "Se ha quemado mi casa", "Baul"]

print(funcion.insertion_sort_large(sentences_list))


#Ejercicio 5
import aFunciones as funcion
nums = [3,-2,9,77,654,12,8,7,6,5,4,3,21,1]
print(funcion.bubble_sort_inv(nums))


#Ejercicio 6
import aOrdenamientos as orden
new_nums = [4, 2, 2, 8, 3, 3, 1]
print(orden.counting_sort(new_nums))


#Ejercicio 7
import aOrdenamientos as orden
mix_list = [9,"z", 6, "h", 8, "k", "l", 88, 5, 1, "a", "A"]
print(orden.mix_sort(mix_list))


#Ejercicio 8
import aOrdenamientos as orden
num_list = [5,8,9,3,1,4,5,8,7,5,5,185,5,15,16,5163,4658,463,516,84]

print(orden.merge_sort(num_list))