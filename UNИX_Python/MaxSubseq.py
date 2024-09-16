pred = int(input())
if pred == 0:
    print(0)
else:
    max_len = 1
    cur_len = 1
    while cur := int(input()):
        if cur >= pred:
            cur_len += 1
        else: 
            cur_len = 1
        pred = cur
        max_len = max(max_len, cur_len)

    print(max_len)




