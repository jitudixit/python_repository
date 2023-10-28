#Find largest number where provided list by users
lis = []
count = int(input("How many numbers?"))

for i in range(count):
    number = int(input("Enter number: "))
    lis.append(number)
print("Largest Elemnt of the list is : ",max(lis))
