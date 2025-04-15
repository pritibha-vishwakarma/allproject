import random
name=input("enter a name?")
print("Good Luck!", name)

words=['rainbow','computer','science','programming','python','java','javascript','html','css','c++','c#']
word=random.choice(words)
print("Guess the charactre")

guess=''
turns=12

while turns>0:
    failed=0
    
    for char in word:
        if char in guess:
            print(char, end="")
        else:
            print("_")
            failed +=1
    if failed==0:
        print("You Win")
        print("The word is:", word)
        break
    print()
    guess=input("guess a character:") 
    
    guess+=guess
    if guess not in word:
        turns -=1
        print("Wrong")
        print("You have", + turns, 'more guessess')
        
        if turns ==0:
            print("you loose")            





