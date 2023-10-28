#Deep copy Program
from copy import deepcopy
a=[1,[2,3]]
b=deepcopy(a)
a[1].append(4)
print(a)
print(b)
b[1].append(5)
print(a)
print(b)
