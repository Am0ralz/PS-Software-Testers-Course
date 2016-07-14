import random

counter = 0
answer = random.randrange(1, 10)
InvalidInput = True


while InvalidInput:
    try:
        while counter < 3:
            guess = int(input("Guess a number from 1-10: "))
            if guess in range(0, 11):
                if guess == answer:
                    print("Congratulations!!! You guessed the right number")
                    InvalidInput = False
                    break
                elif (guess == answer - 1) or (guess == answer + 2):
                    print("Hot")
                elif (guess == answer - 2) or (guess == answer + 2):
                    print("Warm")
                else:
                    print("Cold")

            else:
                raise IOError
            counter += 1
            InvalidInput = False
    except ValueError:
        print("You didn't enter a numerical number")
    except IOError:
        print("Your number was not in range 1-10")

if counter == 3:
    print("You didn't guess the correct number")
