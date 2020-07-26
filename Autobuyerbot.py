import time
import requests
import sys


class UserException(Exception):
    def __init__(self,text,dicription=''):
        self.text = text
        self.dicription = dicription


def balance_check():
    r = requests.get("https://market.csgo.com/api/v2/get-money?key=[your_secret_key]")
    try:
        r_dict = eval(r.text.replace('true','True'))
    except:
        time.sleep(3)
    if r_dict['money'] < 11000:
        sys.exit()
        

def resale_test():
    r = requests.get("https://market.csgo.com/api/v2/test?key=[your_secret_key]")
    try:
        r_dict = eval(r.text.replace('true','True'))
    except:
        time.sleep(3)
    if r_dict['success']:
        for key,value in r_dict['status'].items():
            if value ==  False:
                return False
        print("Connection available")
        return True
    return False
    

def time_time(last_time):
    if time.time() - last_time > 300:
        if resale_test():
            return True
        else:
            time.sleep(150)
            
    

def Start():
    while True:
        last_time = time.time()   
        time_time(last_time)
        r = requests.get("https://market.csgo.com/api/v2/search-item-by-hash-name?key=[your_secret_key]&hash_name=[market_hash_name]")
        try:
            r_dict = eval(r.text.replace('true','True'))
        except:
            time.sleep(3)
            continue
        if r_dict['data'][0]['price'] < 11000:
            r = requests.get("https://market.csgo.com/api/v2/buy?key=[your_secret_key]&hash_name=[market_hash_name]&price=[price]")
            print(r.text)
            balance_check()
            
        time.sleep(15)  #waiting nexn request
Start()





