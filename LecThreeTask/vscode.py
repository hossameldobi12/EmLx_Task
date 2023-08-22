'''

script to install clangd and testmake extensions
Name : Hossam Adel Mostafa

'''

import pyautogui
import os
import time

find = None
clangd_path = "/home/hossam/Desktop/EmLx_task/LecThreeTask/clangd.png"
# clangd_path = os.path.dirname(os.path.realpath(__file__))+ "/clangd.png"
TestMate_path = "/home/hossam/Desktop/EmLx_task/LecThreeTask/testmate.png"
pyautogui.click(89,305)
time.sleep(2)
pyautogui.write('clangd')
time.sleep(2)
while find is None :
    find = pyautogui.locateOnScreen(clangd_path,confidence=0.7)
time.sleep(2)
pyautogui.click(239,207)
time.sleep(2)
pyautogui.click(714,252)
time.sleep(2)
pyautogui.click(202,142)
time.sleep(2)
pyautogui.hotkey('ctrl','a')
time.sleep(2)
pyautogui.hotkey('backspace')
time.sleep(2)
pyautogui.write('testmate')
time.sleep(2)
while find is None :
    find = pyautogui.locateOnScreen(TestMate_path,confidence=0.7)
time.sleep(2)
pyautogui.click(239,207)
time.sleep(2)
pyautogui.click(714,252)
time.sleep(2)


# print(pyautogui.position())



