#create a electricCar class that inherit from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    
  

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

my_tesla=ElectricCar("tesla","nikki","20rh")        
print(my_tesla.model)

