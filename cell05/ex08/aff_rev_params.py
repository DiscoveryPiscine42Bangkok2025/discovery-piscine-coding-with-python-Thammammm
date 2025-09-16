import sys

item_list = sys.argv[1:]

if len(item_list) <= 2:
    print("none")
else:
    reversed_list = item_list[::-1]
    for item in reversed_list:
        print(item)