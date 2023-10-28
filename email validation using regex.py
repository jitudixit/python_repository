# Email validation ushing regex() function
import re


email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input('Enter your Eamil : ')

if re.search(email_condition,user_email):
    print("Right email")
else:
    print("Invalid Email")
