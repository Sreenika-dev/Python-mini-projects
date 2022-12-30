import random

#welcome message
nameUser =  input("What's your name? ")
print(f"Hey {nameUser} lets play a  Fun Number Guessing Game, \n Shall we?")     

#computer generates random number b/w 1-10
computerGuess = random.randint(1,10)
count = 0

#guessing starts here
while count < 5:
 userGuess =  int(input("What's your Guess? "))
 count += 1
 if userGuess<computerGuess:
    print("Your guess is too low")
 elif userGuess>computerGuess:
    print("Your guess is too high")
 elif userGuess==computerGuess:
     break
if userGuess==computerGuess:
     print(f"You guessed it right and it took you {count} attempts to win")
else:
     print("Sorry you have lost, attempts dead") 

