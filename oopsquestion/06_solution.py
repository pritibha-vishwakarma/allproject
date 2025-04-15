# programme to create a class representing a Circle. include metons to calculate area and parameter.
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius=radius

#     def calcutate_circle_area(self):
#         return math.pi * self.radius**2

#     def calculate_circle_perimeter(self):
#         return 2* math.pi *self.radius

# radius = float(input("input rhe radius of the circle:"))

# circle=Circle(radius)

# area=circle.calcutate_circle_area()

# perimeter=circle.calculate_circle_perimeter()

# print("Area of circle:", area)

# print("perimeter of hte circle:", perimeter)


#wap to create a person class. include attributes like name, counter and date of birth. implement a method to determine the person's age.
# from datetime import date
# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth

#     def calculate_age(self):
#         today=date.today()
#         age=today.year - self.date_of_birth.year

#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age
# person1 = Person("Ferdi odila ","france", date(1343,5,8))
# person2 = Person("shweata ","canada", date(1343,5,8))      
# person3 = Person("eligherland ","india", date(1343,5,8))


# print("Person 1:")
# print("Name:", person1.name)
# print("Counrtry",person1.counrty)
# print("Date of Birth:",person1.date_of_birth)
# print("Age:",person1.calculate_age())


# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Counrtry",person2.counrty)
# print("Date of Birth:",person2.date_of_birth)
# print("Age:",person2.calculate_age())


# print("Person 3:")
# print("Name:", person3.name)
# print("Counrtry",person3.counrty)
# print("Date of Birth:",person3.date_of_birth)
# print("Age:",person3.calculate_age())

#wap a python programe to create a calculator class. include methods for basic aritimatic operations.
# class Calculator:
#     def add(self,x,y ):
#         return x+y

#     def subtract(self, x,y):
#         return x-y

#     def multiply(self,x,y):
#         return x*y

#     def divide(self,x,y):
#         if y !=0:
#            return x/y 
#         else:
#             return("Cannot divide by Zero.")


# calculate=Calculator()

# result = calculate.add(7,5)
# print("7+5", result)

# result = calculate.subtract(7,5)
# print("7-5", result)

# result = calculate.multiply(7,5)
# print("7*8", result)

# result = calculate.divide(7,5)
# print("7/2", result)

# result = calculate.divide(7,0)
# print("7/0", result)


#program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math
class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def calculate_area(self):
         return math.pi * self.radius**2

    def calculate_perimeter(self):
         return math.pi * self.radius**2      

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width

    def calculate_perimeter(self):
        return 2* (self.length+self.width)  

class Triangle(Shape):
    def __init__(self,base,height,side1,side2,side3):
        self,base=base        
        self.height=height
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def calculate_area(self):
       return 0.5 * self.base * self.height

    def calculate_perimeter(self):
       return self.side1 + self.side2 + self.side3
r=7
circle=Circle()
circle_area=circle.calculate_area()
circle_perimeter=circle.calculate_perimeter()

print("Radius of the circle",r)
print("circle area", circle_area)
print("circle perimeter", circle_perimeter)

l=5
w=7

rectangle = Rectangle(l, w)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()


print("\nRectangle: Length =", l, " Width =", w)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)