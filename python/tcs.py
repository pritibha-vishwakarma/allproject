# def max_card_score(cards, K):
#     N = len(cards)
#     left_sum = sum(cards[:K])
#     max_score = left_sum

#     for i in range(1, K + 1):
#         left_sum -= cards[K - i]  
#         right_sum = sum(cards[-i:])  
#         max_score = max(max_score, left_sum + right_sum)

#     return max_score

# # Hardcoded test values
# N = 7  # Number of cards
# cards = [1, 2, 3, 4, 5, 6, 1]  # Points on each card
# K = 3  # Number of cards to pick

# # Run the function and print result
# result = max_card_score(cards, K)
# print(result)


# def encrypt_string(s):
#     compressed=[]
#     i=0
#     while i < len(s):
#         count=1
#         while i + 1<len(s) and s[i] == s[i+1]:
#             i+=1
#             count+=1
#         compressed.append(s[i]+str(count))
#         i+=1
        
#         encryted_string=''.join(compressed)[::-1]
#         return encryted_string
# s="aabc"
# output=encrypt_string(s)      
# print(output)


# n=int(input("enter a num"))
# j=0
# L=[0 for i in range(n)]
# for i in range(n):
#     a=int(input())
#     if a!=0:
#         L[j]=a
#         j+=1
# for i in L:
#     print(i,end=" ")

# import math
# n=int(input("enter a num"  ))
# k=(1<< int(math.log2(n))+1) -1
# print(n^k)


# n=int(input("enter a num"))
# arr=[]
# for i in range(n):
#     arr.append (int(input()))
# for i in sorted(arr):
#     print(i, end=" ")    



student=[]
n=int(input("enter a num"))

for _ in range(n):
    name=input().strip()
    grade=float(input("enter a num"))
    student.append([name,grade])
grades=sorted(set(grade for _, grade in student))

second_lowest=grades[1]
name=sorted([name for name, grade in student if grade == second_lowest])
    
for names in name:
    print(name)