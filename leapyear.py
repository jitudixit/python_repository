print("Find Leep Year")

year = int(input("Enter any year : "))
#find lear year method

'''if year % 4 == 0 and year % 100 == 0:
    print("Year is leap year :",year)
elif year % 400 == 0:
    print("Year is a leep year : ",year)
else:
    print("Year is not a leep year ",year)'''

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, " is a leep year")
        else:
            print(year, " is not a leep year")
    else:
        print(year, " is a leep year")
else:
    print(year, " is a leep year")
