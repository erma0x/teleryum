![alt text](/docs/header.png)


## Description
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
operation_data = {
    'symbol':'BTC/USDT',
    'side':'buy',
    'leverage':2,
    'buy': {1:float,2: ...},
    'sell':{1:float,2: ...}
    'stoploss':{1:float,2: ...}
  }

operation_data={
        'side':'buy',
        'symbol':'EGLD-USDT',
        'buy':{1 : '144.20' },
        'sell':{1:'144.78',2:'145.35',3:'146.22'},
        'stoploss':'139.87'
        'leverage': 10 
        }


```


<br>

### UML workflow
![alt text](/docs/flowcharts/flowchart.png)


## How to Run 
Lunch 3 different terminals 
```bash
source ./venv/bin/activate
python3 bot.py
python3 accounter.py      # incoming mid Apr 2022
```

## Installation
1. **Telegram API**
  
   Create Telegram API from my.telegram.org
   <br> you need **api_id** and **api_hash**

<br>

2. **FTX exchange**
    1) **Create FTX account**
    2) **Deposit initial capital**
    3) **Create FTX API**

<br>

3. **Select Telegram channels to follow on params.py**

```
CHANNEL_1 = 'Test1'
CHANNEL_2 = 'Test2'
# ...
CHANNEL_20 = 'KingOfCryptoVip'
```

4. **Create configurations file .env** 

    Create .env file inside project/ and insert your credential and API keys into it 

```
USERNAME_TELEGRAM = "@username"
PHONE_NUMBER = "+111111111" 
API_ID_TELEGRAM = 123456
API_HASH_TELEGRAM = "AAAAAAAAAAAAAAAAAAAAA" 
API_ID_EXCHANGE_FTX = 123456789
API_HASH_EXCHANGE_FTX = "AAAAAAAAAAAAAAAAAAAAAA" 

```


5. **Install 3rd party libraries**


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

## Telegram credentials

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