#number of attempts
attempts=10

#secret word
word="secret"

#previous guesses
guesses=""


while attempts>0:

    #get user guess input
    guess=input("Enter your guessing word: ")

    guesses+=guess

    #string contain correct guesses in order of word
    newword=""
    
    for char in word:
        # TODO: write code...
        if char in guesses:
            print(char)
            newword+=char
        
        else:
            print("_")
    
    if newword==word:
        print("You won")
        break
    
    if guess not in word:
        print("Wrong guess")
        attempts-=1
        print("You have only ", attempts," attempts")
        print("Try again!")
        print()
        
if attempts==0:
    print("You Lose")
