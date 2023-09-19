def most(a, b):
    if (a > b):
        return a
    else:
        return b
    
def least(a, b):
    if (a < b):
        return a
    else:
        return b
    
#PROGRAMA PRIMCIPAL

x = int(input("Un número: "))
y = int(input("Otro número: "))

print(most(x-3, least(x+2, y-5)))