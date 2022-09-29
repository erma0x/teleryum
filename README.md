# Teleryum
### Telegram message scanner and automated trader with ftx.com and kucoin.com <br>

![](docs/Teleryum.png)

## Workflow
 1. Scan incoming messages from telegram
 2. Find out if the new message is a signal
 3. If it is a signal, parse it and send it as operation to okex.com or ftx.com with ccxt open source library



## How to Run 

1. Connect to server via ssh and express connecting rules

    ```ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=2 $HOSTNAME```

2. activate virtual enviroenment

    ```source ./venv/bin/activate```

3. lunch demon trader with python3 and nohup

       a. ```nohup python3 -u teleryum.py 1> log.out 2> log.err &```

       b. ```python3 teleryum.py```



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
