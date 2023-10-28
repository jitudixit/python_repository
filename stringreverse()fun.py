def reverse(str):
    s = " "
    for ch in str:
        s = ch + s
    return s
mystr = "Beginners Book"
print("Given string :",mystr)
print("Revers string :",reverse(mystr))
