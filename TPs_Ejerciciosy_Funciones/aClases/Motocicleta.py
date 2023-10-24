class Motorcycle:
    
    estado = "Nueva"
    engine = False

    def __init__(self, color = "", patent = "", wheels = 0,fuel_ltrs = 0, mark = "", model = "", creation_date = "", weight = 0, ortip_speed = 0):
        self.color = color
        self.patent = patent
        self.fuel_ltrs = fuel_ltrs
        self.mark = mark
        self.model = model
        self.creation_date = creation_date
        self.weight = weight
        self.ortip_speed = ortip_speed
    

    #Getter?
    


    #Métodos inteligentes
    #Arrancar
    def turn_on(self):
        if self.engine == True:
            print(f"La moto de color {self.color} ya está encendida")
            print()
        else:
            self.engine = True
            print(f"Se encendió el motor de la moto color {self.color}")
            print()

    def turn_off(self):
        if self.engine == False:
            print(f"La moto de color {self.color} ya está apagada")
            print()
        else:
            self.engine = False
            print(f"Se apagó el motor de la moto color {self.color}")
            print()

    def consult_price(self):
        print(f"El precio de la moto {self.color}, marca {self.mark} y {self.model} es de : ${self.price}")