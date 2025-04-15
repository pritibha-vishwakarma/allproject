# base=int(input("Enter a base"))
# height=int(input("Enter a height"))


# area=1/2*base*height
# print(f"the area of triangle is :{area}")



#swap two number
# a=int(input("Enter 1st number"))
# b=int(input("Enter 2nd number"))

# print(f"original  value:a={a}, b={b}")

# temp=a
# a=b
# b=temp


# print(f"after swap: a={a}, b={b}")



#to generate a random number

# import random
# print(f"random number:{random.randint(1,100)}")



#convert killometers to miles
# kilometer=int(input("enter kilometer distance"))
# conversion_factor=0.621371
# miles=kilometer*conversion_factor
# print(f"{kilometer} kilometer is equal to {miles} mile")




# #convert celcius to fornehight
# celsius=int(input("enter tempreture in celcius:"))
# fahrenheite=(celsius*9/5) +32
# print(f"{celsius} degress calcius is equal to {fahrenheite} degree ")



#display calender
# import calendar
# year=int(input("enter year: "))
# month=int(input("enter month: "))

# cal=calendar.month(year, month)
# print(cal)

#solve the qudratic equation
# import math 
# def euationroots(a,b,c,i):
#     dis = b*b -4 *a*c
#     sqrt_val=math.sqrt(abs(dis))
    
#     if dis>0:
#         print("real and different roots")
#         print((-b + sqrt_val)/(2*a))
#         print((-b - sqrt_val)/(2*a))
        
        
#     elif dis ==0:
#         print("real and same roots") 
#         print(-b/(2*a))
        
        
#     else:
#         print("complex roots")       
#         print(-b /(2*a),  sqrt_val / (2*a))
#         print(-b /(2*a), sqrt_val / (2*a))
# a =1
# b=10
# c=-24

# if a==0:
#     print("Inpur correct quadratic equation ")
    
    
# # else:
#     euationroots(a, b, c,0)   
    
# if a  number is possitive , negative or zero

# num=    float(int(input("enter a number")))

# if num>0:
#     print("positive number")
# elif num==0:
#     print("Zero")
# else:
#     print("negative number")        
    
    
# y=int(input("enter a year"))


# if y % 4 ==0:
#     if y % 100 ==0:
#         if y % 400 ==0:
#             print("Leap year")

#         else:
#             print("not a leap year") 
            
#     else:
#         print("leap year") 
# else:
#     print("not a leap year")                      
    
#check prime number
 