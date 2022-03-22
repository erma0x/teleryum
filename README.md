![alt text](/docs/img/header.png)


Telegram crypto signal scanner and with live FTX exchange. Scan incoming telegram messages from crypto channels, find out if the new message is a signal, and if it's a signal, parse it and send to trade with FTX REST API. 

## Design Components
### Workflow of bot.py 
1. Listen all incoming telegram messages
2. check if the message contain a signal
4. if it is, exctract operation_data
5. FTX client place order with operation_data 

### Workflow of accounter.py
listen db and exchange api for accounting and statistics

### Data structures
``` python
message_data = {
    'symbol':'BTC/USDT',
    'side':'buy',
    'leverage':2,
    'buy': {1:float,2: ...},
    'sell':{1:float,2: ...}
    'stoploss':{1:float,2: ...}
  }

operations_data={{
        'side':'buy',
        'symbol':'EGLD-USDT',
        'buy':{1 : '144.20' },
        'sell':{1:'144.78',2:'145.35',3:'146.22'},
        'stoploss':'139.87'
        'leverage': 10 
        }
```

<br>

## Telegram Channels
```python
CHANNEL_1 = 'freecrypto_signals'
CHANNEL_2 = 'cryptosignals0rg'
CHANNEL_3 = 'fatpigsignals'
CHANNEL_4 = 'BinanceKillersVipOfficial'
CHANNEL_5 = 'CryptoTrades'
CHANNEL_6 = 'Coin_Signals'
CHANNEL_7 = 'HIRN_CRYPTO'
CHANNEL_8 = 'cryptohopperofficial'
CHANNEL_9 = 'altsignals'
CHANNEL_10 = 'SignalsBlueChannel'
```

## FTX REST API python

### place order

``` python
    place_order(

[input]
    market: str,
    side: str,
    price: float,
    size: float, 
    type: str = 'limit',
    reduce_only: bool = False,
    ioc: bool = False,
    post_only: bool = False,
    client_id: str = None,
    reject_after_ts: float = None
    ) -> dict:

[output dict]
    'market': market,
    'side': side,
    'price': price,
    'size': size,
    'type': type,
    'reduceOnly': reduce_only,
    'ioc': ioc,
    'postOnly': post_only,
    'clientId': client_id,
    'rejectAfterTs': reject_after_ts
```

### place conditional order

``` python

place_conditional_order()

[input]
    market: str,
    side: str,
    size: float,
    type: str = 'stop',
    limit_price: float = None,
    reduce_only: bool = False, 
    cancel: bool = True,
    trigger_price: float = None,
    trail_value: float = None

[output dict]
    'market': market,
    'side': side,
    'triggerPrice': trigger_price,
    'size': size,
    'reduceOnly': reduce_only,
    'type': 'stop',
    'cancelLimitOnTrigger': cancel,
    'orderPrice': limit_price
```

![alt text](/docs/img/flowchart.png)


## How to Run 
Lunch 2 different terminals 
```bash
source ./venv/bin/activate
python3 bot.py            # incoming end March 2022
python3 accounter.py      # incoming mid April 2022
```

## Installation
1. **Generate Telegram API keys**
  
   Create Telegram API on the following website: my.telegram.org
   <br> you need to generate **api_id** and **api_hash**

<br>

2. **Generate FTX exchange API keys**
    1) **Create FTX account**
    2) **Deposit initial capital**
    3) **Create FTX API**

<br>

3. **Select Telegram channels to follow on params.py**

```
CHANNEL_1 = 'Test1'
CHANNEL_2 = 'Test2'
#
CHANNEL_20 = 'CryptoChannelBros'
```

4. **Create configurations file .env** 

    Create .env file inside the project root folder <br> and insert your credential and API keys into it 

```
USERNAME_TELEGRAM = "@username"
PHONE_NUMBER = "+111111111" 
API_ID_TELEGRAM = 123456
API_HASH_TELEGRAM = "AAAAAAAAAAAAAAAAAAAAA" 
API_ID_FTX = 123456789
API_HASH_FTX = "AAAAAAAAAAAAAAAAAAAAAA" 
```


5. **Install 3rd party libraries**

Install vitrual environment
```bash
python3 -m venv venv
```
Activate the virtual environment
```bash
source ./venv/bin/activate
```
Install python package manager
```bash
python3 -m pip install --upgrade pip 
```
Install 3rd party libraries
```bash
pip install -r requirements.txt 
```

<br>

## Telegram credentials
### Telegram username and phone number
Insert your credential as follow, use full phone number including + and country code. 
```
USERNAME = "@my_username"
PHONE_NUMBER = "+111111111111" 
```

### Telegram API keys on:    
Visit the following website : my.telegram.org
``` python
API_ID = 123456789
API_HASH = "AAAAAAAAAAAAAAAAAAAAAA" 
```
