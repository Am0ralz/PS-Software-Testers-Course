def size_total(s):
    total = 0
    if s == 't':
        return total + 20
    elif s == 'm':
        return total + 40
    else:
        return total + 80


def car_total(c):
    total = 0
    if c == 's':
        return total + 5
    elif c == 'h':
        return total + 10
    else:
        return total + 15


def total(a, b):
    total1=(size_total(a)+ car_total(b))
    tax = total1 * .0875

    print("You chosen ", b, "and ", a, "your total is", total1+tax)


wash = (input("what type of wash? s = self service, h = Hand-washed Service, and ac = Automated Car Wash "))
size = (input("What type of car? t = small, m = medium and l = large "))

total(size, wash)
