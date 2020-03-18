def firstnum():
    no = input("Enter the first number for the sequence :")
    n = input("Enter the number to be added :")
    global no
    global n
    execute()


def execute():
    while no != 0 and n != 0:
        sequence=int(no)+int(n)
        print(sequence)
        global sequence

def sequence_generator(no,n,sequence):
    print(sequence)
    execute(no,n)


firstnum()