import random
print("Hi welcome to the game, This is a number guessing game. \nyou got 7 chances to guess the number. Let's start the game.")
number_to_guess=random.randrange(100)
chance=7
guess_counter=0

while guess_counter < chance:
    guess_counter +=1
    my_guess=int(input("Enter a number"))
    if my_guess==number_to_guess:
        print(f'the number is{number_to_guess} and you found it right !! in the {guess_counter} attempt')
        break
    elif guess_counter >=chance and my_guess != number_to_guess:
        print(f'oops sorry ,The number is {number_to_guess} better luck next time')
        