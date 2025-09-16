import sys
item_list = sys.argv
item_list.pop(0)
i = len(sys.argv)
if i == 0:
    print("none")
else:
    sentence = sys.argv[0]
    count_z = sentence.count("z")
    if count_z <= 0:
        print("none")
    else:    
        print("z"*count_z)