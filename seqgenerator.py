def firstnum():
    global no
    global n
    no = int(input("Enter the first number for the sequence :"))
    n = int(input("Enter the number to be added :"))

    while no != 0 and n != 0:
        for i in range(100):
            sequence = no*i+n
            print(sequence)

firstnum()