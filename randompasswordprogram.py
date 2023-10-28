#GENERATE PASSWARD WHICH IS TOUGH TO BREAKK FOR HACCKER

import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
supper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

use_for = lower_case + supper_case + number + symbols
length_for_pass = 8
password = "".join(random.sample(use_for,length_for_pass))
print("Genrate your password : ",password )
