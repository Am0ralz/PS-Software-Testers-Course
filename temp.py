
option = "y"
while option != "n":
    temp1 = int(input("Enter temperature in Fahrenheit: "))
    temp2 = (temp1-32)*(5/9)
    print(temp1, "F")
    print(temp2, "C")
    option = input("Continue : yes: y or no: n ")
