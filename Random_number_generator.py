def rand():
    import random
    random_no = random.randint(1, 10)
    random_guess = input("Enter a random digit between 1 and 10 :")
    if random_guess != str(random_no):
        print("Wrong guess")
        print("The right guess answer was", +random_no)
    else:
        print("Correct guess")
        print("You win !")
        play_again = input("Would you like to play again (y/n):")
        if play_again != "y" and play_again != "yes":
            exit()
        elif play_again == "y" or play_again == "yes":
            rand()


def random_confirmation():
    confirm = input("Enter yes or no :")
    while confirm != "no" and confirm != "n":
        rand()
    if confirm == "no" or confirm == "n":
        print("Exiting code ")
        exit()


random_confirmation()
