#create a empty list
# """list = []
# n = int(input('Enter number of elements : '))
# for i in range(0,n):
#     ele = int(input())
#     list.append(ele)
# print(list)"""

# list1 = []
# list2 = []
# list1 = [int(item) for item in input('Enter the list items : ').split()]
# list2 = [item for item in input('Enter the list item : ').split()]
# print(list1)
# print(list2)


#create a empty list
list = []
n = int(input('Enter number of elements : '))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
print(list)
sum = sum(list[0:3])
print(sum)


