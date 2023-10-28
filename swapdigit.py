#newList = input(12, 34, 35, 36, 38)
def swapList(newList):
    size = len(newList)


    #Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList
newList = [ 12, 34, 35, 36, 38]

print(swapList(newList))
