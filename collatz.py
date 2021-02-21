# A program that performs the Collatz sequence on any given positive integer

import time

def collatz(number):

    # Collatz sequence is finished if number reaches 1
    if number == 1:
        print("Collatz Sequence finished!")
    # If number is even 
    elif number % 2 == 0:
        print(int(number/2))
        return number / 2
    # If number is odd
    else:
        print(int(number * 3 + 1))
        return number * 3 + 1

try:
    number = int(input("Choose any integer greater than 1 for Collatz: "))
    ops = 0
    if number < 1:
        print("This number is too small for the Collatz sequence")
    elif number == 1:
        print("Collatz sequence done.")
    else:
        result = collatz(number)
        while result != 1:
            result = collatz(result)
            time.sleep(0.1)
            ops = ops + 1
        collatz(result)
    print(f"Collatz sequence took {ops} operations.")

except ValueError:
    print("This is not a number")
