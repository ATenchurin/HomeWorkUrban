my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
s = 0
while s < len(my_list):
    if my_list[s]  >=0:
        if my_list[s] != 0:
            print(my_list[s])
        s = s + 1
        continue
    else:
        break