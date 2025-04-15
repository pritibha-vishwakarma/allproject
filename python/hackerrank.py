# Create an empty list to store student details
# students = []

# # Read the number of students
# n = int(input("enter a num"))

# # Get student names and grades
# for _ in range(n):
#     name = input().strip()  # Read name
#     grade = float(input())  # Read grade
#     students.append([name, grade])  # Store in list

# # Find the unique grades and sort them
# grades = sorted(set(grade for _, grade in students))

# # Get the second lowest grade
# second_lowest = grades[1]

# # Find names of students with the second lowest grade
# names = sorted([name for name, grade in students if grade == second_lowest])

# # Print the names, each on a new line
# for name in names:
#     print(name)


# num=int(input("enter a number"))
# # if num%2==0:
#     print("Even")
# else:
#     print("Odd")    

num=int(input("enter a number"))

if num>1:
    for i in range(2, num):
        if num%i==0:
            break    
    else:
        print("Prime")