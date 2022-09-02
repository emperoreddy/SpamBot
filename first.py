# import modules
import pyautogui
import time

def spam(message, spamTimes):
    count = 0
    while (count < spamTimes):
        # write message (Virtual keyb)
        pyautogui.write(message)
        pyautogui.press('enter')
        count += 1

#---main---

# get the message and how many times
message = input("Choose the message to spam: ")
spamTimes = int(input("How many times to spam: "))
print("The software will start in: ")

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

spam(message, spamTimes) 

# ---------


