# Teleryum

## Description
Telegram crypto signal scanner and with live KuCoin trader.

## Design Components
### bot.py

1. listen all incoming telegram messages
2. check if the message contain a signal
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

### accounter.py
listen db and exchange api for accounting and statistics

<br>

![alt text](/docs/flowcharts/flowchart.png)


# How to Run 
Lunch 3 different terminals 
```bash
source venv/bin/activate
python3 listener.py
python3 trader.py          # incoming mid Mar 2022
python3 bookkeeper.py      # incoming mid Apr 2022
```

# Installation
1. **Telegram API**
  
   Create Telegram API at my.telegram.org, you need **api_id** and **api_hash**

<br>

2. **FTX exchange**
    1. **Create FTX account**
    2. **Deposit initial capital**
    3. **Create FTX API**

<br>

3. **Create configurations file** 

    Create .env file inside project/ and insert your credential and API keys into it 

```
USERNAME_TELEGRAM = "@username"
PHONE_NUMBER = "+111111111" 
API_ID_TELEGRAM = 123456
API_HASH_TELEGRAM = "AAAAAAAAAAAAAAAAAAAAA" 

CHANNEL_1 = 'Test1'
CHANNEL_2 = 'Test2'
# ...
CHANNEL_20 = 'KingOfCryptoVip'

API_ID_EXCHANGE_FTX = 123456789
API_HASH_EXCHANGE_FTX = "AAAAAAAAAAAAAAAAAAAAAA" 

```


3. **Install 3rd party libraries**

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
python3 -m pip install --upgrade pip 
```
```bash
pip install -r requirements.txt 
```

<br>

### Credentials

#### Telegram username and phone number
Insert your credential as follow, use full phone number including + and country code 
```
USERNAME = "@my_username"
PHONE_NUMBER = "+111111111111" 
```

#### Telegram API keys on :    _my.telegram.org_
``` python
API_ID = 123456789
API_HASH = "AAAAAAAAAAAAAAAAAAAAAA" 
```