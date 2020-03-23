def bit_reader():
    binary_points = 0
    sequence_dictionary = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
    binary_input1 = str(input("Enter the first bit of the binary bit :"))
    binary_input2 = str(input("Enter the second bit of the binary bit :"))
    binary_input3 = str(input("Enter the third bit of the binary bit :"))
    binary_input4 = str(input("Enter the fourth bit of the binary bit :"))
    binary_input5 = str(input("Enter the final bit of the binary bit :"))
    if binary_input1 == "1":
        binary_points += 16
    if binary_input2 == "1":
        binary_points += 8
    if binary_input3 == "1":
        binary_points += 4
    if binary_input4 == "1":
        binary_points += 2
    if binary_input5 == "1":
        binary_points += 1
    elif binary_input1 == "0" or binary_input2 == "0" or binary_input3 == "0" or binary_input4 == "0" or binary_input5 == "0":
        binary_points += 0
     #elif KeyError:
       #print("Key error , wrong input keys (The input must only be one number at a time and no characters or alphabets are allowed )")
    if binary_points >= 27:
        print("The values you have entered seem to be wrong ,please try again !")
    elif binary_points <= 27:
        binary_final_output = int(binary_points)
        print("The position of the alphabet is "+str(binary_final_output)+" and the letter would be "+"'"+sequence_dictionary[binary_final_output].capitalize()+"'")
    else:
        something_went_wrong = input("It seems like something went wrong , press 'r' to run the programme again or press 'e' to exit")
        if something_went_wrong == "r" or "R":
            bit_reader()
        else:
            exit()


bit_reader()
