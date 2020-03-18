#ABCD number position finder
def sequence_finder():
    try:
        sequence_dictionary = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
        alphabet_to_number={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
        choice=input("Do you want to enter a position (1-26) and check for the alphabet if yes enter 'a';else if you want you can enter an alphabet and check for it's position by entering 'p' (a/p) :")
        if choice == "a" or choice == "A":
            Position = input("Enter a position :")
            Alphabet = sequence_dictionary[int(Position)]
            print("The Alphabet in this position would be "+"'"+Alphabet.capitalize()+"'")
        elif choice == "p" or choice == "P":
            alphabet_input=input("Enter an alphabet :")
            number_output=alphabet_to_number[alphabet_input]
            print(number_output)
        else:
            print("Wrong input , please try again ")
            exit()
    except ValueError:
        print("Invalid input value !")
    except KeyError:
        print("The number you have entered is not in the range of 1-26 please try again ")


sequence_finder()