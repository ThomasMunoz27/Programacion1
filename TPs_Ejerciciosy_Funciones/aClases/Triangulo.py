class Triangle:

    def __init__(self, tria_type = "", side1 = 0.0, side2 = 0.0, side3 = 0.0):
        self.tria_type = tria_type
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Definición de getters
    @property
    def tria_type(self):
        return self._tria_type

    @property
    def side_1(self):
        return self._side1

    @property
    def side_2(self):
        return self._side2

    @property
    def side_3(self):
        return self._side3
    
    # Definición de setters
    @tria_type.setter
    def tria_type(self, new_type):
        new_type = new_type.lower()
        if new_type in ["equilátero", "isósceles", "escaleno"]:
            self._tria_type = new_type
        else:
            print("No es un tipo de triángulo válido")

    @side_1.setter
    def set_side1(self, new_side):
        self._side1 = new_side

    @side_2.setter
    def set_side2(self, new_side):
        self._side2 = new_side

    @side_3.setter
    def set_side3(self, new_side):
        self._side3 = new_side

    # Métodos
    # Mostrar datos del triángulo
    def show_info(self):
        print(f"Los lados del triángulo {self.tria_type} son {self.side1}, {self.side2}, {self.side3}")

    # Mostrar el lado más largo
    def show_larger_side(self):
        larger = max(self.side1, self.side2, self.side3)
        print(f"El lado más largo del triángulo {self.tria_type} es de: {larger}")
