#Seconds calculator
#Days in a year =365(excluding leap year)
#No. of years * 365*24(hours)*60
try:
    def Seconds_calculator():
        year=input("Enter the number of years :")
        hour=input("Enter the number of hours:")
        seconds=int(year)*365*int(hour)*60
        print("The number of seconds in "+str(year)+" years"+" with "+str(hour)+" hours a day "+" is "+str(seconds))
except ValueError:
    print("Value Error , Wrong input value")


Seconds_calculator()