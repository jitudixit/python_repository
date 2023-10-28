# Creation of array

# importing "array" for array creation

import array as arr

# Creating array with integer type

a = arr.array("i",[1,2,3,4,5])


#Printing original array

print("The new created array is : ", end = " ")
for i in range (0,5):
    print(a[i], end = " ")
print()


print(a)
# Creating an array with float type

b = arr.array('d',[3.5,3.6,3.7,3.8,3.9])

# Printing original array

print("The new created array is : ", end = " ")
for i in range(0,5):
    print(b[i], end = " ")
print()
