list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 3, 5, 7]
index = 0

while index < len(list1):
    if list2[index] != list1[index]:
        list2.insert(index,'...')

    index = index + 1

print(*list2)