
import pyautogui
import time
import webbrowser

# print(pyautogui.position())

#Open your inbox
webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

#Wait 4s for the email to be opened 
time.sleep(10)

#Click on the position of (Select all) check box
pyautogui.click(1630,188)

#Wait 2s to load
time.sleep(4)

#Click on the position of (Mark as read) check box
pyautogui.click(1445,179)









