def divisible_by_2(my_list=[]):
    neww = []
    for i in my_list:
        if i % 2 == 0:
            i = True
            neww.append(i)
        else:
            i = False
            neww.append(i)
    return neww


my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
