# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result *= i
        
#     return result    
# num=int(input("enter a number")) 
# print(f"Factorial of {num} is {factorial(num)}")       



# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n * factorial(n-1)

# num=int(input("enter a number")) 
# print(f"Factorial of {num} is {factorial(num)}")       




# import math
# num = int(input("enter a number"))
# print(f"sqrt of {num} is {math.sqrt(num)}")


#print of first all number sum

# def sum_of_natural(n):
#     total=0
#     for i in range(1,n+1):
#         total += i
#     return total 
# n=10
# result = sum_of_natural(n)
# print(result)    


# n =int(input("enter a numver"))
# sum_of_n = n * (n + 1) // 2
# print(f"The sum of the first {n} natural numbers is {sum_of_n}")

#print all natural numbers upto N


# def print_natural_number(N):
#     for i in range(1, N+1):
#         print(i, end=" ")
# N = int(input("enter a number"))   
# print(f" natural numbers up to {N} are:")
# print_natural_number (N)    

# #reverse an array
# def reverse_array(arr):
#     return arr[::-1]

# arr=[1,2,3,4,5,5]
# reversed_array=reverse_array(arr)
# print("Reversed array:", reversed_array)


# arr=[1,2,3,4,5,6]
# arr.reverse()
# print(arr)


# #find the area of circle
# import math
# def circle_area(radius):
#     return math.pi * radius**2
# radius=float(input("enter the radius of the circle" ))
# area=circle_area(radius)
# print(area)

#LCM of two numbers
# import math
# def find_lcm(a,b):
#     return abs (a*b)//math.gcd(a,b)

# num1=int(input("Enter first number: "))
# num2=int(input("Enter first number: "))

# print(f"lcm of {num1} and {num2} is {find_lcm(num1, num2)}")


# find all the roots of a quardratic equation
# import math
# def find_roots(a,b,c):
#     discriminant =  b**2 - 4*a*c
#     if discriminant > 0:
#         root1=(-b + math.sqrt(discriminant) / (2*a))
#         root2=(-b + math.sqrt(discriminant) / (2*a))
        
        
#         print(f" Two real and distinct roots: {root1}, {root2}")
        
#     elif discriminant==0:
#         root = -b/(2*a)
#         print(f"one real and qual root:{root}")
#     else:
#         real_part=-b/(2*a) 
#         imaginary_part=math.sqrt(abs(discriminant))/ (2*a)
#         print(f"complex roots: {real_part} +- {imaginary_part} i ")      
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))    

# find_roots(a,b,c)



#palindrom numbers
# def is_palindrom(num):
#     return str(num) == str(num)[::-1]
# num = int(input("enter a number"))
# if is_palindrom(num):
#     print(num, " is a palindrom number")
    
# else:
#     print(num,  " is not a palindrom number")    
    
    
#armstrong  number
# def is_armstrong(num):
#     num_str= str(num)
#     num_digits=len(num_str) 
#     sum_of_powers=sum (int(digit)** num_digits for digit in num_str)
#     return num == sum_of_powers


# num =int(input("enter a number"))
# if is_armstrong(num):
#     print(num, "is an Armstrong:")
# else:
#     print(num, "is not an armstrong")    

# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact*=i
#     return fact
# num =int(input("enter a number")) 
# print(f" Fcatorial of {num} is {factorial(num)}")   


#leap year or not
# def is_leap_year(year):
#     if (year % 4==0 and year % 100 != 0) or (year% 400==0):
#         return True
    
#     else:
#         return False
    
# year=int(input("enter a number"))   

# if is_leap_year(year):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year") 
    
# def binary_to_decimal(binary):
#     decimal=0
#     for digit in binary:
#         decimal=decimal*2 +int(digit)
        
#         return decimal    
# binary="1010"
# print("Decimal number:",binary_to_decimal(binary))        

# n=5
# for i in range(1, n+1):
#     print(" " * (n-i) + "*" *(2*i-1))
    
    
# n=5 
# for i in range(1, n+1):
#     print("*" *i)    
    
# n=5
# for i in range(n, 0, -1):
#    print("*" * i)    
   
#pyramid pattern
# n=5
# for i in range(1, n+1):
#     print(" "* (n-i) + "+" *(2*i-1) )   
    
# print("hello world")
    
# class student():
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod    #decorator 
#     def hello():
#         print("hello  world")
        
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+= val 
#         print("hii", self.name, "your avg score is:", sum/3)      
# s1=student("pratibha",[99,98,97])        
# s1.get_avg( )            
# s1.hello()




#create a Account class with 2 attributes- balance and account no.
#create methods for debit, credit and prtinting the balance.
# class Account():
#     def __init__(self, bal, acc):
#         self.bal=bal
#         self.acc=acc
        
#     def dabit(self, amount):
#         self.bal -=amount
#         print("Rs.", amount,"was debited from your account")    
#         print("total balance =",self.get_balance())
#     def credit(self, amount):
#         self.bal +=amount
#         print("Rs.", amount,"was credited to your account")
#         print("total balance =",self.get_balance())

#     def get_balance(self):
#         return self.bal   
# acc1=Account(1000, 1234)
# acc1.dabit(100)
# acc1.credit (2000)   
# acc1.credit (200)





# class Student():
#     def __init__(self, name):
#         self.name=name
# s1=Student("pratibha")
# print(s1.name)
# del s1.name#delete the name attribute
# print(s1.name) #error will come because name attribute is deleted


class Person():
    __name="anonymous"
    
    def __hello(self):#__is a private method we can not accesss it outside the class
        print("hello Person")
        
    def welcome(self):#but we can access it outside the class
        self.__hello()  #calss ke ander isko access kar sakte hai
          
p1=Person()
print(p1.welcome())                