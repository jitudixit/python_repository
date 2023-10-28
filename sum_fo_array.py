import array as arr

# array =array('i',[1,2,3])
# print(type(array))

a = arr.array('i',[1,2,3])
#print(len(a))
print('Array before instertion: ',end = " ")
for i in range(0, 3):
    print(a[i], end = " ")
