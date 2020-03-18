def rand():
    import random
    random_no = random.randint(1, 10)
    print(random_no)


def randconf():
    confirm = input("Enter yes or no :")
    while confirm != "no" and confirm != "n":
        rand()
    if confirm == "no" or confirm == "n":
        print("Exiting code ")
        exit()


randconf()