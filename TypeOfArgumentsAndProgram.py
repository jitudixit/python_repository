#Type of arguments

#Opsitionsl Arguments

def add (a,b):
    return a + b
print(add(3,4)) #give two value because of we definge two peremeters in functin if we give one argument the run time error occure
print(add)
#Default argument in this case we provide a argumet when we define the perameters

def add (a, b = 7):
    return a + b

add(4,5)
print(add)
add(55)#here we give one argument but add funtion need two argument so we defined b argumetn in the initilizing time in b, b = 7
print(add)
