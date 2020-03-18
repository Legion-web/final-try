def firstnum():
    global no
    global n
    no = int(input("Enter the first number for the sequence :"))
    n = int(input("Enter the number to be added :"))
    no+=n
    print(no)
    finder()


def finder():
    if no!=0:
        sequence()
    else:
        exit()

def sequence():
    no+=n
    print(no)

firstnum()