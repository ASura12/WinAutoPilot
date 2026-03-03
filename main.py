import pyautogui as s
import time


s.press("win")
time.sleep(1)

s.write("notepad", interval=0.2)
s.press("enter")

time.sleep(1)


s.write("Hi, I am Ashish", interval=0.2)
s.press("enter")

s.write("How are you", interval=0.2)
s.press("enter")
