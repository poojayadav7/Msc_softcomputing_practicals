def overlapping(list1, list2):
    for x in list1:
        if x not in list2:
            continue
        else:
            return 1
    return 0

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

if overlapping(list1, list2):
    print("overlapping")
else:
    print("not overlapping")
