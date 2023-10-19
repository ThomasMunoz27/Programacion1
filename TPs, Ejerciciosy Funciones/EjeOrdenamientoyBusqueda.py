import aFunciones as funcion
nums = [5,7,6,44,2,3,8,9,4444,6,1,10,96,69]
large = len(nums)
print(nums[0:large//2])
print(nums[large//2::])

print("Burbuja")
print(funcion.bubble_sort(nums))

print("Seleccion")
print(funcion.selection_sort(nums))

print("Insercion")
print(funcion.selection_sort(nums))