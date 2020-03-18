secrert_number="3"
guess=""
count=0
countlimit=3
Out_of_guesses=False
while guess != secrert_number and not Out_of_guesses:
    if count<countlimit:
        guess=input("Enter a number :")
        count += 1
    else:
        Out_of_guesses=True
if Out_of_guesses:
    print("Sorry you have run out of guesses !")
else:
    print("You win !")