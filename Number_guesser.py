#Number guesser game
secret_guess="3"
guess=""
guesscount=0
guesslimit=3
Out_of_guesses=False

while guess !=secret_guess and not Out_of_guesses:
    if guesscount<guesslimit:
        guess=input("Enter your guess :")
        guesscount+=1
    else:
        Out_of_guesses=True
if Out_of_guesses:
    print("Sorry but you ran out of guesses")
else:
    print("You win !")