

total = 0
counter = int(input("How many numbers would you like to input? "))

for a in range(0, counter):
    num = int(input("Input numbers "))
    print(num)
    total += num


average = total/counter

print("average is: ", average)
