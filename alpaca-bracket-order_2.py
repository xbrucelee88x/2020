#https://github.com/hackingthemarkets/alpaca-bracket-order/blob/master/bracket_order.py




import requests, json
#from config import *
from sample_config import *


#BASE_URL = "https://api.alpaca.markets"
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
#HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

HEADERS = {'PK8MY64THIAWNGEU9JOT': API_KEY, 'DOmXxP0ncku/Lbj6DgHc4BKq6AtFEXWq4mkFuwt3': SECRET_KEY}


def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)

    return json.loads(r.content)

response = create_order("AAPL", 100, "buy", "market", "gtc")

#response = create_order("AAPL", 100, "buy", "market", "gtc")
#response = create_order("MSFT", 1000, "buy", "market", "gtc")

#orders = get_orders()

#print(orders)


data = {
    "symbol": "AAPL",
    "qty": 1,
    "side": "buy",
    "type": "market",
    "time_in_force": "gtc",
    "order_class": "bracket",
    "take_profit": {
        "limit_price": "320"
    },
    "stop_loss": {
        "stop_price": "314",
    }
}

r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

response = json.loads(r.content)

print(response)