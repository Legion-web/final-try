try:
    def binary():
        final_binary_output = 0
        global final_binary_output
        sequence_dictionary = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k",12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u",22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
        binary_input1 = str(input("Enter the first bit of the binary bit :"))
        if binary_input1 == "1":
            final_binary_output += 16
            print(final_binary_output)
        else:
            final_binary_output = final_binary_output
        binary_input2 = str(input("Enter the second bit of the binary bit :"))
         if binary_input2 == "1":
            final_binary_output += 8
         else:
            final_binary_output = final_binary_output
        binary_input3 = str(input("Enter the third bit of the binary bit :"))

        binary_input4 = str(input("Enter the fourth bit of the binary bit :"))
        binary_input5 = str(input("Enter the final bit of the binary bit :"))
                if binary_input3 == "1":
                    final_binary_output += 4
                else:
                    final_binary_output = final_binary_output
                    if binary_input4 == "1":
                        final_binary_output += 2
                    else:
                        final_binary_output=final_binary_output
                        if binary_input5 == "1":
                            final_binary_output+=1
                        else:
                            final_binary_output = final_binary_output
                            print(final_binary_output)
                            if final_binary_output==0:
                                print("Wrong set of bits net result =0")
                            else:
                                print(sequence_dictionary[final_binary_output])
except ValueError:
    print("Value Error")

binary()