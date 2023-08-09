'''
write a python program to access the environment  variable 
Name : Hossam Adel Mostafa

'''

import os

#set
os.environ["variable"] = "123456"

#get 
var = os.getenv("variable")
print(var)