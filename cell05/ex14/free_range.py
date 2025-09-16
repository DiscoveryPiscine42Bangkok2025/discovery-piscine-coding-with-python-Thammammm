import sys
if len(sys.argv) == 1:
    print("none")
else:
    first_number = int(sys.argv[1])
    second_number = int(sys.argv[2])
    x = range((first_number),(second_number)+1)
    array = list(x)
    print(array)