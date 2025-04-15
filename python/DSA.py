# Function to check whether any pair exists
# whose sum is equal to the given target value
# def twosum(arr,target):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] + arr[j]==target:
#               return True
#     return False
# if __name__=="main":
#     arr=[0,-1,2,-3,1]
#     target=-2
    
#     if twosum(arr,target):
#         print("true")
    # else:
    #     print("false")              
          
# Function to check whether any pair exists
# whose sum is equal to the given target value
# def twoSum(arr, target):
#     n = len(arr)

#     # Iterate through each element in the array
#     for i in range(n):
      
#         # For each element arr[i], check every
        # other element arr[j] that comes after it
        # for j in range(i + 1, n):
          
        #     # Check if the sum of the current pair
        #     # equals the target
        #     if arr[i] + arr[j] == target:
        #         return True
              
    # If no pair is found after checking
    # all possibilities
#     return False

# if __name__ == "__main__":
#     arr = [0, -1, 2, -3, 1]
#     target = -2

#     if twoSum(arr, target):
#         print("true")
#     else:
#         print("false")
#some question of python for practice
# 1. What is the output of the following code?
# def f1():
#     print("This is f1")
#     def f2():
#         print("This is f2")       
#     f2()
# f1()
# A. This is f1
# B. This is f2
# C. This is f1 This is f2
# D. This is f2 This is f1
# import sys
# def creter():
#     list=[]
#     i=1
#     while i<=200:
#         list.append(i)
#         i += 1
#     return list
# print(creter())
# z=sys.getsizeof(creter())
# print(z)

# numbers =[0,1,2,3,4,5,6,7,8,9]
# print(numbers[2:6]) slice is used to get the elements from the list
# print(numbers[2:9])
# print(numbers[:4])
# print(numbers[4:])
# print(numbers[:])
# print(numbers[-3:])
# print(numbers[-4:-1])
# print(numbers[-5:-2])
# print(numbers[-1:-5]) #empty list  will be printed because the starting index is greater than the ending index
# print(numbers[9:4]) # [5,6,7,8]
# print(numbers[1:8:2]) #[1,3,5,7]
# print(numbers[::3]) #[0,3,6,9]
# print(numbers[::-2]) #[9,7,5,3,1]
# print(numbers[::-1]) #[9,8,7,6,5,4,3,2,1,0] reverse the list


# class Car:
#     @staticmethod
#     def start():
#         print("car started:")
        
    # @staticmethod
#     def stop():
#         print("car stopped:") 
# class Toyotacar(Car):
#     def __init__(self, name):
#         self.name=name
# car1=Toyotacar("fortuner")
# car2=Toyotacar("prius") 
# print(car1.start())                  

#multilevel inheritance in python 
# class A:
#     VarA="welcome to class A"
    
# class B:
#     VarB="welcome to class B"
    
# class C(A,B): 
#     VarC="welcome to class C"
# c1=C()
# print(c1.VarC)
# print(c1.VarB)
# print(c1.VarA)           


# class Car:
    
#     def __init__(self, type):#constructor is a special method in python which is used to initialize the object
#         self.type=type
#     @staticmethod
#     def start():
#         print("car started:")
        
#     @staticmethod
#     def stop():
#         print("car stopped:")
         
# class Toyotacar(Car):
#     def __init__(self, name,type):
#         super().__init__(type)#supermethod is used to call the constructor of the parent class
#         #__init__ is a constructor of the parent class 
#         self.name=name
#         super().start()
# car1=Toyotacar("prius","electric")
# print(car1.type)


#classmethod is used to access the class variable and class method and static 
# #instance is a variable which is used to access the instance variable and instance method this a an object of the class
# class Student:
#     def __init__(self, phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentagr=str(self.phy+self.chem+self.math)/3 +"%"
        
#     # def calcPercentage(self):
#     #    self.percentage= str(self.phy+self.chem+self.math)/3 +"%"  
#     @property
#     def percentage(self):
#         return str(self.phy+self.chem+self.math)/3 +"%"  
# stu1=Student(98,97,99)
# print(stu1.percentagr)

# stu1.phy=100
# print(stu1.percentagr)       



#dunder function in python
# class Complex:
#     def __init__(self, real, img):
#         self.real=real
#         self.img=img 
        
#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")
        
#     def add(self, num2):
#         newReal=self.real+ num2. real
#         numImg=self.img+num2.img
#         return Complex(newReal, numImg)
    
# num1=Complex(3,4)  
# num1.showNumber()

# num2=Complex(5,6)
# num2.showNumber()

# num3=num1.add(num2)
# num3.showNumber()  #dunder function is used to add the two complex number
            
            #@property is used to access the instance variable and instance method
            #getter and setter is used to access the instance variable and instance method
            #getter is used to access the instance variable
            #setter is used to set the instance variable
            #deleter is used to delete the instance variable
            #staticmethod is used to access the class variable and class method
            #classmethod is used to access the class variable and class method and static
            #instance is a variable which is used to access the instance variable and instance method this a an object of the class
            #supermethod is used to call the constructor of the parent class
            #__init__ is a constructor of the parent class
            #constructor is a special method in python which is used to initialize the object
            #multilevel inheritance in python
            #single inheritance in python
            #multiple inheritance in python
            #hierarchical inheritance in python
            #hybrid inheritance in python
            #inheritance is a concept in which one class inherits the properties of another class
            #class is a blueprint of the object
            #object is an instance of the class
            #class is a collection of objects
            #object is a real-world entity
            #class is a logical entity
            #class is a template
            #object is a physical entity
            #object is a runtime entity
            #class is a static entity
            #class is a user-defined data type
            #object is a dynamic entity
            #object is a built-in data type
            #class is a reference type
            #object is a value type
# define a circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a perimeter() method of the calss which allows you to calculate the primeter of the circle.
# import math
# class Circle:
#     def __init__(self, radius):
#          self.radius=radius 
     
#     def Area(self):
#         return  (22/7) * self.radius ** 2 # pi*r^2
    
#     def Perimeter(self):
#         return 2* (22/7)* self.radius #2*pi*r 
# c1=Circle(21)   
# print(c1.Area())
# print(c1.Perimeter())      
                    
             