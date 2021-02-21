# A program that performs the Collatz sequence on any given positive integer

def collatz(number):

    # Collatz sequence is finished if number reaches 1
    if number == 1:
        print("Collatz Sequence finished!")
    # If number is even
    elif number % 2 == 0:
        print(int(number/2))
        return number / 2
    else:
        print(int(number * 3 + 1))
        return number * 3 + 1

try:
    collatz(int(input("Choose any integer greater than 1 for Collatz: ")))


except ValueError:
    print("This is not a number")
