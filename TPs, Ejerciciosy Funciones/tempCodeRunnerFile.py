import aOrdenamientos as orden
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
authors = []
for i in range(0, len(books)):
    for keys in books[i]:
        if keys == "autor":
            authors.append(books[i][keys])
print(authors)
print(orden.bubble_sort(authors, books))
