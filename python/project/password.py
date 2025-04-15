import random
import string

def password(minlength, numbers=True, special_symbol=True):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    characters = s1
    if numbers:
        characters +=s2
    if special_symbol:
        characters +=3

    pwd =""
    meets_criteria =False 
    has_number=False 
    has_special=False

    while not meets_criteria or len(pwd) < minlength:
        new_char =random.choice(characters)
        pwd += new_char 

        if new_char in s2:
            has_number=True

        elif new_char in s3:
            has_special=True

    meets_criteria=True
    if numbers:
        if special_symbol:
            meets_criteria=meets_criteria and has_special 


    return pwd

minlenght = int(input("Enter password lenght:")) 
has_number=input("Do you want numbers (y/n)?").lower() == "y"
has_special=input("Do you want to have special character (y/n)?").lower() == "y"
pwd = password(minlenght, has_number, has_special) 
print*("your password is :", pwd)                     