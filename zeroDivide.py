def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Division by 0 dummy.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print("It worked :D")