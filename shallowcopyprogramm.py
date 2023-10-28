#Shallow copy Program

from copy import copy
a = [1,[2,3]]
b = copy(a)
a[1].append(4)
print(a)
print(b)
