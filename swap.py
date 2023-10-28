#Swap the first and last element using pop operation

def swapList(newList):

    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)


    return newList
newList[12, 35, 36, 9, 24]

print(swapList)
