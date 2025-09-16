import sys

item_list = sys.argv[1:]

if len(item_list) <= 1:
    print("none")
else:
    word = item_list[0]
    count = item_list.count(word)
    print(count)