def rand():
    import random
    random_no = random.randint(1, 10)
    print(random_no)


def randconf():
    confirm = input("Enter 'yes' to generate numbers or 'no' to exit :")
    while confirm == "yes" or confirm == "y" or confirm == "Yes" or confirm == "Y" or confirm == "YES":
        rand()
    if confirm == "no" or confirm == "n" or confirm == "N" or confirm == "NO":
        print("Exiting code ")
        exit()
    else:
        print("Wrong input please try running the programme again with valid input ")
        exit()


randconf()