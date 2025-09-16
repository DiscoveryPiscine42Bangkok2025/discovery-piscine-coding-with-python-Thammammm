ori_a = [2,8,9,48,8,22,-12,2]
ori_n = []
for i in ori_a:
    if i > 5 and i+2 not in ori_n:
        ori_n.append(i + 2)
    else:
        pass
print(ori_a)
print(ori_n)