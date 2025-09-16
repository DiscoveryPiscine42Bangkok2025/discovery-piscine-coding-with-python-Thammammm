import sys
if len(sys.argv) == 1:
    print("none")
elif len(sys.argv) == 2:
    letter = sys.argv[1].lower()
    print(letter)
else:
    print("none")
    