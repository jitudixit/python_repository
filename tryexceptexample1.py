def divide(x,y):
    try:
        result = x//y
        print("Yeah! It is your answer :",result)
    except ZeroDivisionError:
        print("yes! Your dividing by zero")
        
divide(3,2)
divide(3,0)

