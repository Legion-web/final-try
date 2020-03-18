def firstnum():
    global no
    global n
    global no1
    no = int(input("Enter the first number for the sequence :"))
    n = int(input("Enter the number to be added :"))
    no1= no+n
    print(no1)
    execute()


def execute():
    global no2
    if no1!=0:
        no2=int(no1)+int(n)
        print(no2)
        seqcont()
    else:
        exit()


def seqcont():
    global no3
    if no2!=0:
        no3=int(no2)+int(n)
        print(no3)
        continuation()


def continuation():
    global no4
    while no3!=0:
        no4=int(no3)+int(n)
        print(no4)



firstnum()
execute()
seqcont()
continuation()