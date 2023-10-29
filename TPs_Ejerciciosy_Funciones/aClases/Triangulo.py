class Triangle:

    def __init__(self, tria_type = "", side1=0.0, side2=0.0, side3=0.0):
        self.tria_type = tria_type
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    #Definicion de getters
    @property
    def get_tria_type(self):
        return self.tria_type
    
    @property
    def get_side1(self):
        return self.side1
    @property
    def get_side2(self):
        return self.side2
    @property
    def get_side3(self):
        return self.side3
    
    #Definiendo setters
    def set_tria_type(self, new_type):
        new_type = new_type.lower()
        if new_type != "equilátero" or new_type != "isósceles" or new_type != "escaleno":
            self.tria_type = new_type

    @side1.setter
    def side1(self, new_side):
        self.side1 = new_side
    
    @side2.setter
    def side2(self, new_side):
        self.side2 = new_side

    @side3.setter
    def side3(self, new_side):
        self.side3 = new_side

    ### Metodos ###
    #Mostrar el tipo de triángulo


    #Mostrar el lado mas largo
    def show_larger_side(self):
        larger = self.side1
        if self.side2 > larger:
            larger = self.side2
        if self.side3 > larger:
            larger = self.side3
        print(f"El lado mas largo del triangulo {self.tria_type} es de: {larger}")
