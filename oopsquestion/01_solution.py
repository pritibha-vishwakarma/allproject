#Create a car Class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model

my_car=Car("toyota","corolla")
print(my_car.brand)
print(my_car.model)      


    
