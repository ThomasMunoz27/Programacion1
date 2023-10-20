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
