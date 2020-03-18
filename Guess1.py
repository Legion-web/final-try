secret_word = "Ambidextrous"
secret_word2 = "ambidextrous"
guess = ""
guess_count = 0
guess_limit = 3
Out_of_guesses = False
while guess != secret_word and guess != secret_word2 and not Out_of_guesses:
    if guess_count < guess_limit:
        guess_count += 1
        guess = input("Enter a word :")
    else:
        Out_of_guesses = True
if Out_of_guesses:
    print("You've run out of guesses")
else:
    print("You win !")
