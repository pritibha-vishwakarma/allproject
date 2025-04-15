# import numpy as np
# import array as A

# def set_min(A):
#     mini=float('inf')
#     for num in A:
#         if num < mini:
#             mini=num 
#     return mini
# def set_max(A):
#     maxi=float('-inf')
    
#     for num in A:
#         if num>maxi:
#             maxi=num
#     return maxi
        
# if __name__ == "__main__":
#             A=[4,9,6,5,3,2]
#             N = len(A)
#             print("Minimum element is:", set_min(A))  
#             print("Minimum element is:", set_max(A))  

# string1=input('enter the string ')
# string2 =string1[::-1]
# if string1==string2:
#     print("given number is palindrom")
# else:
#     print("given number is not palindrom") 
    
    
    
string=input("Enter the string")
character=input("Enter the character")

frequency=0
frequency = string.count(character)
print(str(frequency) + ' is the freequency of given string')    



def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n > 1 and a[0] == '*' and m == 0:
        return False
    if (n > 1 and a[0] == '?') or (n != 0 and m !=0 and a[0] == b[0]):
        return solve(a[1:],b[1:]);
    if n !=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False   

