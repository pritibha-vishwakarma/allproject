# num =int(input("enter the number:"))
# temp=num
# reverse=0
# while  num > 0:
#     ramainder=num%10
#     reverse = (reverse*10) + ramainder
#     num=num//10
    
# print("The Given Number is {} and Reverse is{}".format(temp, reverse))    



# num = int(input("Enter a number"))
# n1, n2=0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range (2, num):
#     n3= n1+n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")
    
# print()        
    



# Function to calculate GCD
# def gcdFunction(num1, num2):
#     while num2 != 0:
#         num1, num2 = num2, num1 % num2  # Update num1 and num2
#     return num1

# # Input two numbers from the user
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))

# # Calculate and print the GCD
# gcd = gcdFunction(num1, num2)
# print(f"The GCD of {num1} and {num2} is: {gcd}")




# n= int(input("enter any number:"))
# sump=0
# for i in range(1, n):
#     if (n% i == 0):
#         sump=sump+i
# if(sum==n):
#    print("The number is perfect number")   
   
# else:        
#    print("The number is  not perfect number")        



# find the non reapting characters in string.
# string="rrttyy"
# for i in string:
#    count=0
#    for j in string:
#       if i==j:
#          count+=1
#       if count>1:
#          break
#    if count==1:
#          print(i,end=" ") 

#Write a code to replace a substring in a string.           
# string=input("Enter a string:\n")
# str1=input("enter a substring which to be replace")
# str2=input("Enter substring with wchic str1 has ")
# string=string.replace(str1, str2)
# print("string after replacement ")
# print(string)

#. Write a code to replace each element in an array by its rank in the array.
# def changeArr(input1):
#    newArray=input1.copy()
#    newArray.sort()
   
#    for i in range(len(input1)):
#       for j in range(len(newArray)):
#          if input1[i]==newArray[j]:
#             input1[i] =j+1
#             break
# arr =[100,2,60,12,90]
# changeArr(arr)
# print(arr)     

#----- Write a code to find circular rotation of an array by K positions.-----#
# def rotateArray(arr,n,d):
#    temp=[]
#    i=0
#    while(i<d):
#         temp.append(arr[i])
#         i = i+1
#    i=0
#    while(d<n):
#       arr[i] = arr[d]
#       i=i+1
#       d=d+1
      
#    arr[:] =arr[: i]+temp
#    return arr     


# write a code to fnd non-repeating elemnts in an array.
def count(arr,n):
   visited = [False for i in range(n)]
   
   for i in range(n):
      if (visited[i==True]):
         continue
      
      count=1
      for j in range(i+1, n, 1):
         if (arr[i] == arr[j]):
            visited [j]=True
            count+=1
         if count == 1:
            print(arr[i])
arr = [10,30,40,20,10,20,50,10]   
n = len(arr)
count(arr, n)               

#Write a code to check for the longest palindrome in an array.

