def choice():
    choice_input = input("Enter 'sg' to run sequence generator or enter 'sf' to run sequence number finder or enter any other key to exit :")
    if choice_input == "sg":
        sequence_generator()
    elif choice_input == "sf":
        sequence_number_finder()
    else:
        exit()


def agn():
    play_again=input("Would you like to find or generate a different number series (Y/N):")
    if play_again =="Y":
        choice()
    elif play_again=="N":
        exit()

def sequence_generator():
    n = int(input("Enter a range to generate the sequence :"))
    while n in range(1, n+1):
        print(int(n*(n+1)/2))
    else:
        agn()


def sequence_number_finder():
    s = int(input("Enter the position of the number to be found :"))
    while s ==int(""):
        print(int(s*(s+1)/2))
    else:
        agn()


choice()
