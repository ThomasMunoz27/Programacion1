
class Person:


    def __init__(self, name = "", age = 0, dni = 0):
        self.name = name
        self.age = age
        self.dni = dni
        self.__blood_type = "o+"


#Definicion de getters
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_age(self):
        return self.age
    
    @property
    def get_dni(self):
        return self.dni
    
    @property
    def get_blood_type(self):
        return self.__blood_type
    

    #Definicion de setters

    def set_name(self, new_name):
        if type(new_name) == str:
            self.name = new_name
        else:
            print("El valor debe ser una cadena de texto")

    def set_age(self, new_age):
        if type(new_age) == int:
            self.age = new_age
        else:
            print("El valor debe ser un número")

    def set_dni(self, new_dni):
        if type(new_dni) == int:
            self.dni = new_dni
        else:
            print("El valor debe ser un número")

    def set_blood_type(self, new_blood):
        if type(new_blood) == str:
            self.__blood_type =new_blood
        else:
            print("El valor debe ser una cadena de texto")


#Mostrar informacion de la persona
    def show_info(self):
        print(self.name)
        print(self.age)
        print(self.dni)
        print(self.__blood_type)

#Validar si es mayor de edad
    def adult(self):
        if self.age < 18:
            print(f"{self.name} es menor de edad")
        else:
            print(f"{self.name} es mayor de edad")

