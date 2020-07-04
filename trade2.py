
#https://www.youtube.com/watch?v=GsGeLHTOGAg

import requests
#from config import *
from sample_config import *

#ENDPOINT_URL = "https://paper-api.alpaca.markets"
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY,'APCA-API-SECRET-KEY': SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    #r = requests.post(ORDERS_URL, headers=HEADERS)

   return json.loads(r.content)

response = create_order("APPL", 100, "buy", "market", "gtc")

orders = get_orders()

#r = request.get(ENDPOINT_URL)
#r = requests.get(BASE_URL, headers={'PK8MY64THIAWNGEU9JOT': API_KEY,'DOmXxP0ncku/Lbj6DgHc4BKq6AtFEXWq4mkFuwt3': SECRET_KEY})
#r = requests.get(ACCOUNT_URL, headers={'PK8MY64THIAWNGEU9JOT': API_KEY,'DOmXxP0ncku/Lbj6DgHc4BKq6AtFEXWq4mkFuwt3': SECRET_KEY})
#r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': API_KEY,'APCA-API-SECRET-KEY': SECRET_KEY})

#print(r.content)
print(orders)


