![alt text](/docs/img/header.png)

<br>

# Teleryum
### Description

Telegram crypto signal scanner and live automated trader. <br>

 Scan incoming  messages from telegram crypto signal channels. Find out if the new message is a signal. If it is a signal, parse it and send it to trading with CCXT and FTX exchange. 

<br>

### Operation data structure
``` python
operation_data = {
    'symbol':'',
    'side':'',
    'leverage':'',
    'entry_prices': [],
    'take_profits': [],
    'stop_losses':[]
  }

operation_data = {
    'symbol':'BTC-PERP',
    'side':'buy',
    'leverage':2,
    'buy': ['1300','1400'],
    'sell':['1700','1800','1900']
    'stoploss':['1000'] }           
```
<br>

### Telegram crypto signal channels
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


<br>


## How to Run 
Lunch 2 different terminals 
```bash
source ./venv/bin/activate
python3 teleryum.py            
python3 accounter.py     
```

<br>

## Installation
1. #### **Select Telegram channels to follow on params.py**

```
CHANNEL_1 = 'crypto_VIP_channel'
...
CHANNEL_50 = 'crypto_signal_channel'
```

2. ### **Install environment**

```bash
# generate base virtual environment
python3 -m venv venv
# activate the virtual environment
source ./venv/bin/activate
# install python package manager
python3 -m pip install --upgrade pip 
# install 3rd party libraries
pip install -r requirements.txt 
```
3. #### **Create .env file** 

Create .env file inside the project root folder and insert all your credential and API keys into it 


    TELEGRAM_USERNAME = "@username"
    TELEGRAM_ID = 12345678
    TELEGRAM_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_READONLY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_READONLY_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_API_MAIN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_API_MAIN_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"

<br>

## How to get credentials
  
### FTX exchange
1) Create FTX account on https://www.ftx.com
2) Deposit initial capital
3) Create default and readonly API keys and save in into .env 


### Telegram
Insert your credential as follow. Get telegram API keys on the following website: https://my.telegram.org

    TELEGRAM_USERNAME = "@username"
    TELEGRAM_ID = 12345678
    TELEGRAM_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"