from array import *
a = []
n = int(input("Number of element id array : "))
for i in range(0,n):
    l = int(input())
    a.append(l)
print(a)
print(type(a))

arr = array('i',[])
a = int(input("Enter the size of array : "))
for i in range(a):
    b = int(input("Enter the elements in the array : "))
    arr.append(b)
print("array is : ",arr)
sum = sum(arr[0:3])
print("Sum is first three array : ",sum)
print(type(arr))

def display(a):
    for i in a:
        print(i)
arr = array('i',[86,82,87,88,89])
display(arr)
