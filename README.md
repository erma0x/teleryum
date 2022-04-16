# Teleryum
### Description
Telegram message scanner and automated trader  <br>

 1. Scan incoming messages from telegram
 2. Find out if the new message is a signal
 3. If it is a signal, parse it and send it as operation to okex.com or ftx.com with ccxt open source library

### How to Run 

```ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=2 $HOSTNAME```

```source ./venv/bin/activate```

a. ```nohup python3 -u teleryum.py 1> log.out 2> log.err &```

b. ```python3 teleryum.py```

### Installation
1. #### Insert Telegram signal channels on params.py (example)
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

2. #### Install environment
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
3. #### Create .env file

Create .env file inside the project root folder and insert all your credential and API keys into it 

    TELEGRAM_USERNAME = "@username"
    TELEGRAM_ID = 12345678
    TELEGRAM_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_READONLY = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_READONLY_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_API_MAIN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
    FTX_API_MAIN_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"

<br>

# Documents
EXCHANGEs
1. kucoin
2. kraken
3. ftx

CHANNELS
INITIAL CAP
2k
1m 4k
2m 6k

## How to get credentials
### FTX exchange
1) Create an account on https://www.ftx.com and deposit capital (min 100$)
2) Create default and readonly API keys and save in into .env 

### Telegram
Get api ID and api HASH on  https://my.telegram.org