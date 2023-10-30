
class Count:

#constructor
    def __init__(self, owner, amount = 0.0):
        self.owner = owner
        self.amount = amount


    #Definicion de getters
    @property
    def get_owner(self):
        return self.owner

    @property
    def get_amount(self):
        return self.amount


#Definiendo setters
    
    def set_owner(self, new_owner):
        self.owner = new_owner

    def set_amount(self, pre_balance):
        self.amount += pre_balance 



    ###   Métodos   ###

    #Mostrar los datos de la cuenta
    def show_info(self):
        print(f"Titular de la cuenta: {self.owner}.\nCantidad: {self.amount}")

    #Ingresar dinero
    def entry_money(self, quanty):
        if quanty >= 0:
            self.amount += quanty
            print(f"Saldo actual: {self.amount}")
        else:
            print("Ingreso de dinero inválido")

            
    #Retirar dinero
    def withdraw(self, quanty):
        if quanty >= 0:
            self.amount -= quanty
            print(f"Saldo actual: {self.amount}")
        else:
            print("Retiro de dinero inválido")