#modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Animal:
    __legs=4

    def _walk(self):
        print("Animal is walkiny")

class Dog (Animal):
    def bark(self):
        print("woolf!")

d=Dog()
print(d.__legs)
d._walk                