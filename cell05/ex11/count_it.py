import sys
item_list = sys.argv
item_list.pop(0)
i = len(sys.argv)
x = 0
print("parameters:",i)
for x in range(i):
    print(f"{sys.argv[x]}: {len(sys.argv[x])}")