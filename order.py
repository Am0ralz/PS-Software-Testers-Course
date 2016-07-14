def maxi(a):
    maxi1 = a[0]
    for num in a:
        if maxi1 < num:
            maxi1 = num
    return maxi1


def mini(b):
    mini1 = b[0]
    for num in b:
        if mini1 > num:
            mini1 = num
    return mini1


option = "y"
num_list = []
while option != "n":
    temp1 = int(input("Enter your numbers: "))
    num_list.append(temp1)
    option = input("Continue : yes: y or no: n ")

maximum = maxi(num_list)
minimum = mini(num_list)

print(maximum)
print(minimum)



