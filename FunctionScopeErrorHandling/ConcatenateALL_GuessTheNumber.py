#This is a Guess the Number game to guess the number in 6 guesses
import random

name = input("Enter your Name : ")
print("Hello "+name+", I am thinking of a number between 1 to 20")
secretNumber = random.randint(1,20)

for guessTaken in range(6):
    guess = int(input("Take a guess : "))
    print(guess)
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break #This condition is for correct guess
if guess == secretNumber:
    print("Good job "+name+", you guessed correctly in "+str(guessTaken)+" guesses.")
else:
    print("Nope. The number I was thinking is of was "+str(secretNumber))
        
