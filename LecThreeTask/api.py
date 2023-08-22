'''

request for api
Name : Hossam Adel Mostafa

'''
import requests
link = requests.get("https://api.ipify.org/?format=json")
print(link.text)