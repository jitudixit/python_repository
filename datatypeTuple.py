#Python data type List, Tuple, set, stritn, dictionary

'''Data type List Program'''
Tuple1 = ()
print("Initial empty Tuple : ")
print(Tuple1)
#creating t tuple with the use of Strings
Tuple1 = ("Geeks","for")
print("\n Tuple with the use fo string :")
print(Tuple1)

#creating a tuple with the using of list
list1=[1,2,3,4,5]
print("\n Tuple using LIst :")
print(tuple(list1))

#creating a tuple with the use of built in function
Tuple1 = tuple("Geeks")
print("\n Tuple with the use of function :")
print(Tuple1)

#creat Tupe with nested tuple
Tuple1 = (0,1,2,3,)
Tuple2 = ("Python ","Geek")
Tuple3 = (Tuple1,Tuple2)
print("\n Tuple with nested Tuples : ")
print(Tuple3)
