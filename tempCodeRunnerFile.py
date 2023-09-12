x = 0
while x < 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print(f"Se saltó el valor {x} de x")
    elif x < 15:
        print(x)
    else:
        break
print(f"Se rompió la ejecución del bucle cuando x valía: {x}")
