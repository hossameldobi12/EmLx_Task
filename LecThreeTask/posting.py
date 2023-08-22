'''

script to publish post on facebook
Name : Hossam Adel Mostafa

'''

import pyautogui
import time
import webbrowser

link = "https://www.facebook.com/hossam.adel.3781995/"
webbrowser.open_new_tab(link)
time.sleep(20)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("what's on your mind?")
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('escape')
pyautogui.press('enter')
time.sleep(20)
pyautogui.write('Hi I am not hossam , i am a script')
time.sleep(15)
pyautogui.click(990, 750)