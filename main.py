import requests
import json
import time
import trade
import decimal
# get_alltokens()
f = open('data.json')  
# returns JSON object as 
# a dictionary
list_all_token = json.load(f)['data']
# print(data)

def get_alltokens():
    try:
        x = requests.get('https://api.huobi.pro/v1/common/currencys')
        list_o_new = x.json()['data']
        difference_1 = list(set(list_o_new).difference(set(list_all_token)))
        print(difference_1)
        for data in difference_1:
            url_string = 'https://api.huobi.pro/market/history/kline?symbol='+data+'usdt&period=1min&size=1'
            currency_details = requests.get(url_string)
            print(currency_details.json())
            if currency_details.json()['status'] == 'ok':
                current_trade_value = currency_details.json()['data'][0]['open']
                # print(float(str(current_trade_value)))
                current_trade_value_float = decimal.Decimal(str(current_trade_value))
                ten_d_val = round(10.5/current_trade_value,0)
                print(ten_d_val,current_trade_value_float)
                # print(currency_details.json())
                # print(data+'usdt',round(ten_d_val,6),current_trade_value)
                trade.trade_new_order(data+'usdt',round(ten_d_val,4),current_trade_value_float)
                list_all_token.append(data)
                
                # with open('data.json','w+') as file:
                #     file_data = json.load(file)
                #     file_data["data"].append(data)
                #     # Sets file's current position at offset.
                #     file.seek(0)
                #     # convert back to json.
                #     json.dump(file_data, file, indent = 4)
    except Exception as e:
        print("error during trade",str(e))

# get_alltokens()

while True:
    get_alltokens()
    time.sleep(5)
    

