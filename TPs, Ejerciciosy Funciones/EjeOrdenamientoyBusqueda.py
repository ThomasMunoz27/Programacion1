import aOrdenamientos as orden
nums = [5,7,6,44,2,3,8,9,4444,6,1,10,96,69]

print("Burbuja")
print(orden.bubble_sort(nums))

print("Seleccion")
print(orden.selection_sort(nums))

print("Insercion")
print(orden.insert_sort(nums))

print("Merge")
print(orden.merge_sort(nums))