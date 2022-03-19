### Description
Telegram crypto signal scanner and with live KuCoin trader.


## Components
### **trader.py**

1. listen db changes
2. read all messages 
3. operations not placed and if same group
4. exctract operation_data
5. place order

use this function for place orders 

``` python
for operation in get_all_messages(NAME_DB):
  if operation = 'not placed' and sender == 'cryptosignalsfree':
      parse and lunch operations
```
output
``` python
operation_data = {
    'symbol':'BTC/USDT',
    'side':'buy',
    'leverage':2,
    'buy': {1:float,2: ...},
    'sell':{1:float,2: ...}
    'stoploss':{1:float,2: ...}
  }
```

### **scanner.py**
listen tg and write db
### **accounter.py**
listen db and exchange api for accounting

<br>

![alt text](/docs/flowcharts/teleryum_flowchart.jpg)


# How to Run 
Lunch 3 different terminals 
```bash
source venv/bin/activate
python3 listener.py
python3 trader.py          # incoming mid Mar 2022
python3 bookkeeper.py      # incoming mid Apr 2022
```

# Installation
1. **Create Telegram API** at my.telegram.org, you need API_ID and API_HASH
2. **Create *.env* file** and insert your credential and telegram API keys into it 

``` python
GROUP_NAME = 'groupName' 
MY_USERNAME = "@username"
PHONE_NUMBER = "+111111111" 
API_ID = 123456
API_HASH = "AAAAAAAAAAAAAAAAAAAAA" 
```

3. **Install packages**

```bash 
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip 
pip install -r requirements.txt 
```

<br>

# Credentials configurations
**.env file** is a configuration where you can add all your personal
information at once without exposing it.

``` python
GROUP_NAME_1 = 'groupName1'
GROUP_NAME_2 = 'groupName2' 

MY_USERNAME = "@username"
PHONE_NUMBER = "+111111111" 
API_ID = 123456
API_HASH = "AAAAAAAAAAAAAAAAAAAAA" 
```
**Telegram group names**
Telegram group that I need to scan for my trading operations
``` python
GROUP_NAME_1 = 'Test1'
GROUP_NAME_2 = 'Test2'
# ...
GROUP_NAME_N = 'KingOfCryptoVip'
```
**Credentials**
Insert your credential as follow, use full phone number including + and country code 
```
USERNAME = "@my_username"
PHONE_NUMBER = "+111111111111" 
```


**Telegram API keys**
Use API id and API hash from =>  my.telegram.org <br>
``` python
API_ID = 123456789
API_HASH = "AAAAAAAAAAAAAAAAAAAAAA" 
```

<br>

# CCXT python trading library

## Github repository link
- https://github.com/ccxt/ccxt

## Order data structure
``` javascript
  {
      'info':         { ... },                    // the original decoded JSON as is
      'id':           '12345-67890:09876/54321',  // string trade id
      'timestamp':    1502962946216,              // Unix timestamp in milliseconds
      'datetime':     '2017-08-17 12:42:48.000',  // ISO8601 datetime with milliseconds
      'symbol':       'ETH/BTC',                  // symbol
      'order':        '12345-67890:09876/54321',  // string order id or undefined/None/null
      'type':         'limit',                    // order type, 'market', 'limit' or undefined/None/null
      'side':         'buy',                      // direction of the trade, 'buy' or 'sell'
      'takerOrMaker': 'taker',                    // string, 'taker' or 'maker'
      'price':        0.06917684,                 // float price in quote currency
      'amount':       1.5,                        // amount of base currency
      'cost':         0.10376526,                 // total cost, `price * amount`,
      'fee':          {                           // provided by exchange or calculated by ccxt
          'cost':  0.0015,                        // float
          'currency': 'ETH',                      // usually base currency for buys, quote currency for sells
          'rate': 0.002,                          // the fee rate (if available)
      },
  }
```
   

* The work on ``'fee'`` info is still in progress, fee info may be missing partially or entirely, depending on the exchange capabilities.
* The ``fee`` currency may be different from both traded currencies (for example, an ETH/BTC order with fees in USD).
* The ``cost`` of the trade means ``amount * price``. It is the total *quote* volume of the trade (whereas ``amount`` is the *base* volume). The cost field itself is there mostly for convenience and can be deduced from other fields.
* The ``cost`` of the trade is a *"gross"* value. That is the value pre-fee, and the fee has to be applied afterwards.

