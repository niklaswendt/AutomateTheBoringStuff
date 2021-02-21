import time, sys
indent = 0 # Number of space indents
indentIncreasing = True # Wether indent is increasing or nottry:

try:
    while True: # main Loop
        print(" " * indent, end="")
        print("********")
        time.sleep(0.25) # Pause for a quarter second

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Shrink indent size
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Grow indent size
                indentIncreasing = True

except KeyboardInterrupt:
    print("Afk for a while")
    sys.exit()

