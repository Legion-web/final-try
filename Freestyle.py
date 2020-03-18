#ABCD number position finder
def sequence_finder():
    try:
        sequence_dictionary={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
        Position=input("Enter a position :")
        Alphabet=sequence_dictionary[int(Position)]
        print("The Alphabet in this position would be "+"'"+Alphabet.capitalize()+"'")
    except ValueError:
        print("Invalid input value !")
sequence_finder()