import sys
item_list = sys.argv
item_list.pop(0)
i = len(sys.argv)
if i == 0:
    print("none")
else:
    for item in item_list:
        if item.endswith("ism"):
            pass
        else:
            print(f"{item}ism")