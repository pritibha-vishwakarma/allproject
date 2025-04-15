#find all positive numbers.
# numbers=[1,-2,3,-4,5,-6,7,-8,9,-10]
# count_positive_number=0
# for num in numbers:
#     if num > 0:
#         count_positive_number += 1
# print("final number is positive",count_positive_number)        




# sum of even number

# n=int(input("given a number"))
# sum_even=0
# for i in range (1, n+1):
#     if i%2 == 0:
#         sum_even +=1
# print("number is even ", sum_even)        


# print the multiplication table for a given up to 10. but skip the fifth iteration.
# number= 8

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print (number,'x', i,'=', number*i)


#reverse string using a loop.
# input_str="pratibha"
# reversed_str=""

# for char in input_str:
#     reversed_str=char+reversed_str

# print(reversed_str)    
    

#find the first non repeated character
# input_str="aabbccdgvv"
# for char in input_str:
#     print(char)
#     if input_str.count(char) ==1:
        
#         print("char is", char)
        # break



#compute the factorial on a number using a while loop.
# number=int(input("input a number"))
# factorial=1
# while number > 0:
#         factorial *= number
#         number = number -1
# print("factorial:", factorial)


# check if all elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate.
# item = ["apple", "banana","banana","orange","apple","mango","mango"]
# unique_item=set()

# for item in item:
#         if item in unique_item:
#                 print("Duplicate:",item)
#                 break
#         unique_item.add(item)


# implement an exponetial backoff strategy that doubles the wait time btw retries,starting from 1 second, but stops after 5 retries.
# import time
# wait_time=1
# max_retries=5
# attempts=0
# while attempts< max_retries:
#         print("Attempt",attempts +1, "- wait time", wait_time)
#         time.sleep(wait_time)
#         wait_time *= 2
#         attempts += 1

# n=110
# for i in range(1,n):
#         print(i)


#Python program to print all the even numbers within the given range.
# given_range=100
# for i in range(given_range):
#         if i%2 == 0:
#                 print(i)


#Python program to calculate the sum of all numbers from 1 to a given number.

# given_number=10
# sum=0
# for i in range(1, given_number):
#         sum+=i
# print(sum)        