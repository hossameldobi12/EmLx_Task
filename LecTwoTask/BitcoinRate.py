import requests

key  = "https://api.coindesk.com/v1/bpi/currentprice.json"
data = requests.get(key)

print(data.json()['bpi']['USD'])