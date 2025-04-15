def is_palindrom(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
user_input = input("Enter a string to check if its's a plalindrom")
if is_palindrom(user_input):
    print(f'"{user_input}is a plaindrom')
else:
   print(f'"{user_input}is  not a plaindrom')

    





















