import sys
sys.path.insert(0,sys.path[0].replace('ccxt','') )
import os
from datetime import datetime
from dotenv import load_dotenv
from pprint import pprint
from channels import *
load_dotenv()
RRFTID = os.getenv('RRFTID')
RRFTSEC = os.getenv('RRFTSEC')
import ccxt

exchange = ccxt.ftx({
                'apiKey': RRFTID,
                'secret': RRFTSEC,
                'enableRateLimit': True,
                })

# freecrypto_signals

message = """
#ETH 
Buy 3360-3380
Sell 3600-3700-3800-3900
StopLoss 2800
By (@SN_crypto)
"""
messages = [message]
op_data={'side':'','market':'','take_profits':{},'sell':{},'stop_losses':{}}

def bot_freecrypto_signals(text_message):

    TEXT_PATTERNS = ('Sell','Buy','#')

    for pattern in TEXT_PATTERNS:
        if pattern not in text_message:
            return False

    date = str(datetime.now())
    #print('NEW SIGNAL from : ',colored(CHANNEL_1,'green'),'\t', date[:-6],text_message)

    for row in text_message.split('\n'): # TEXT MESSAGE ROWS 
        if '#' in row:
            op_data['market'] = row[1:].split(' ')[0]#.replace(' ','').replace('#','')

        if row.find('Buy') < row.find('Sell'):
            op_data['side']='sell'
        else:
            op_data['side']='buy'

        if 'Buy' in row:
            if '-' in row.split()[1]:
                temp = row.split()[1].split('-')
                for n in range(len(temp)):
                    op_data['take_profits'][n] = temp[n]
            else:
                op_data['buy'] = row.split()[1]
        if 'Sell' in row:
            if '-' in row.split()[1]:
                temp=row.split()[1].split('-')
                for n in range(len(temp)):
                    op_data['stop_losses'][n] = temp[n]
            else:
                op_data['Sell'] = row.split()[1]

        if 'StopLoss' in row or 'Stoploss' in row :
            op_data['stoploss'] = row.split()[1]

    print('op ',op_data,'\n')
    # ENTRY
    amount_ = 0.01

    if op_data['side'] == 'buy':
        order = exchange.create_limit_order(op_data['market']+'-PERP', side=op_data['side'], amount=amount_, price=3360.00)
        print(order)

        for i in op_data['take_profits']:
            TP_order = exchange.create_order(symbol=op_data['market']+'-PERP', type='takeProfit', side='sell', amount=round(amount_/len(op_data['stop_losses']),4), price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True })
            print(TP_order)

        for j in op_data['stop_losses']:
            SL_order = exchange.create_order(symbol=op_data['market']+'-PERP', type='stop', side='sell', amount=round(amount_/len(op_data['stop_losses']),4), price=3000.00, params={'triggerPrice':3100.00,'reduceOnly':True })
            print(SL_order)

for message in messages:
    bot_freecrypto_signals(text_message=message)

### THE MESSAGE IS TRANSLETED IN THE FOLLOWING ORDERS

# order = exchange.create_limit_buy_order('ETH-PERP', 0.01, 3360.00)
# print(order)

# SL_buy = exchange.create_order(symbol='ETH-PERP', type='stop', side='sell', amount=0.01, price=3280.00, params={'triggerPrice':3380.00,'reduceOnly':True })
# print(SL_buy)

# TP1_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3600.00, params={'triggerPrice':3500.00,'reduceOnly':True })
# print(TP1_buy)

# TP2_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3700.00, params={'triggerPrice':3500.00,'reduceOnly':True })
# print(TP2_buy)

# TP3_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3800.00, params={'triggerPrice':3500.00,'reduceOnly':True })
# print(TP3_buy)

# TP4_buy = exchange.create_order(symbol='ETH-PERP', type='takeProfit', side='sell', amount=0.025, price=3900.00, params={'triggerPrice':3500.00,'reduceOnly':True })
# print(TP4_buy)