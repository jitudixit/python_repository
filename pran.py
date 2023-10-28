import pyautogui as gui
import time
import random, string

number = int(input('Enter the number : '))
message = ("Kaha ho phone nhi kiyai kal hum intijar hi kar rahe the ")

time.sleep(5)

for i in range(int(number)):
    stri = string.ascii_lowercase
    #05message = "".join(random.sample(stri, 10))
    gui.typewrite(message)
    gui.press('enter')
    