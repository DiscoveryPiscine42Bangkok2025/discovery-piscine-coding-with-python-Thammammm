import sys
item_list = sys.argv[1:]
i = len(item_list)

if i == 1:
    first_w = sys.argv[1]
    second_w = input("What was the parameter?")
    if first_w == second_w:
        print("Good jobs!")
    else:
        print("Nope, sorry...")
else:
    print("none")