# Teleryum
Telegram automated trader with ftx.com and kucoin.com <br>

![](docs/Teleryum.png)

## Workflow
 1. Scan incoming messages from telegram
 2. Find out if the new message is a trading signal
 3. If it is a signal, parse it and send it as a trading operation to kucoin.com with ccxt or ftx.com with native python api.

## Features
- It is possible to execute trading operations starting from any text format.
- It is possible to have an Entry number N. Each Entry can have an X number of Take Profit and a Y number of Stop Loss. The maximum number of pending orders is dictated by the exchange to which we are connected. 
- The operations are performed in less than 5 seconds from the arrival of the telegram message to the actual placement of the operation in the trading platform.

## How to Run 

1. Connect to server via ssh and express connecting rules
    `ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=2 $HOSTNAME`

2. Activate the virtual enviroenment
    `source ./venv/bin/activate`

3. Start demon trader with python3 and nohup <br>
       LIVE MODE -> `nohup python3 -u teleryum.py 1> log.out 2> log.err &` <br>
       TEST MODE -> `python3 teleryum.py` <br>



## Installation


1. Insert Telegram signal channels on **params.py**

(This is an example)
```python
CHANNEL_1 = 'free_crypto_signals'
CHANNEL_2 = 'my_crypto_signals_vip'
```

2. ### Install environment
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
3. ### Create .env file

Create .env file inside the project root folder and insert all your credential and API keys into it 

    TELEGRAM_USERNAME = "@username"
    TELEGRAM_ID = 12345678
    TELEGRAM_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    TRADING_API_READONLY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    TRADING_API_READONLY_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    TRADING_API_MAIN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    TRADING_API_MAIN_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"

<br>

## How to get credentials
### FTX exchange
1) Create an account on https://www.ftx.com and deposit capital (min 100$)
2) Create default and readonly API keys and save in into .env 

### Telegram
Get api ID and api HASH on  https://my.telegram.org
