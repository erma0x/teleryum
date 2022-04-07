![alt text](/docs/img/header.png)

<br>

Telegram crypto signal scanner and with live FTX exchange. Scan incoming telegram messages  <br>
from crypto channels, find out if the new message is a signal, and if it's a signal,  <br>
parse it and send to trade with FTX REST API. 

<br>
<br>

## Design Components
### Workflow of bot.py 
1. Listen all incoming telegram messages
2. check if the message contain a signal
4. if it is, exctract operation_data
5. FTX client place order with operation_data 

## Done
🆗 capire come fare 1 OP con 1TP e 1SL

    guarda tests/ccxt per gli esempi

🆗 capire come fare 1 OP con 3TP e 1SL, 
    
    guarda tests/ccxt per gli esempi

🆗 cambio di STRUTTURA DATI

    unavolta capito come fare le op in manuale
    e con degli script di prova, devi generare 
    una struttura dati che possa soddisfare tutti i canali.

🆗 FROM MESSAGE TO OP_DATA TO TRADE

    mandare operazioni di un canale offline con
    dei messaggi fax simili di un canale specifico.
    Da un unico messaggio son passato a 
    trasformarlo nella struttura 
    dati univoca per turtti desiderata

🆗  LIVE TEST message freecrypto_singal
      ->  OP_DATA -> TRADE 

    mandare operazioni di un canale online FAX SIMILE

🆗  FTX TOKEN FILTER

    capire se il token del segnale e' 
    presente su ftx e farci una funzione che
    ritorna un booleano che permette o meno
    di fare ordini su ftx

🆗  estetics
   fix imports and add simplicity

## 🔥 To Do : In progress

🔥 reformat del progetto per esporre meno chiavi possibili
 
🔥 rebalance delle posizioni, ognuna con il 3% del capitale



<br>
<br>
<br>
<br>
<br>

### movimenti soldi

    BP > N26 > CRYPTO.com > FTX.com

### marketing
    commerciabilita' del progetto

### Workflow of accounter.py
listen sqlitedb/csv and exchange api for accounting and statistics

<br>
<br>

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

# EXAMPLE

base_operation_data_structure = {'side':'',
                                'symbol':'',
                                'take_profits':[],
                                'entry_prices':[],
                                'stop_losses':[]}

operation_data= {
    market: str,
    side: str,
    price: float,
    size: float, 
    type: str = 'limit',
    reduce_only: bool = False,        
        }

OUTPUT

{'avgFillPrice': None,
 'clientId': '1',
 'createdAt': '2022-03-31T00:00:45.813032+00:00',
 'filledSize': 0.0,
 'future': 'SOL-PERP',
 'id': 132710475744,
 'ioc': False,
 'liquidation': None,
 'market': 'SOL-PERP',
 'postOnly': False,
 'price': 108.01,
 'reduceOnly': False,
 'remainingSize': 0.1,
 'side': 'buy',
 'size': 0.1,
 'status': 'new',
 'type': 'limit'}


```

<br>
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

<br>
<br>

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

<br>
<br>

![alt text](/docs/img/flowchart.png)


<br>
<br>


## How to Run 
Lunch 2 different terminals 
```bash
source ./venv/bin/activate
python3 bot.py            # incoming end March 2022
python3 accounter.py      # incoming mid April 2022
```

<br>
<br>

## Installation
1. #### **Select Telegram channels to follow on params.py**

```
CHANNEL_1 = 'Test1'
CHANNEL_2 = 'Test2'
#
CHANNEL_20 = 'CryptoChannelBros'
```

2. #### **Create configurations file .env with your credentials** 

    Create .env file inside the project root folder <br> and insert your credential and API keys into it 

```
USERNAME_TELEGRAM = "@username"
PHONE_NUMBER = "+111111111" 
API_ID_TELEGRAM = 123456
API_HASH_TELEGRAM = "AAAAAAAAAAAAAAAAAAAAA" 
API_ID_FTX = 123456789
API_HASH_FTX = "AAAAAAAAAAAAAAAAAAAAAA" 
```

<br>

3. #### **Install 3rd party libraries**

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
<br>


### How to get credentials

#### FTX exchange
Generate FTX exchange API keys
1) Create FTX account
2) Deposit initial capital
3) Create FTX API

<br>

### Telegram credentials
Insert your credential as follow, use full phone number including + and country code. 
```
USERNAME = "@my_username"
PHONE_NUMBER = "+111111111111" 
```    
For Telegram API keys Visit the following website: my.telegram.org
``` python
API_ID = 123456789
API_HASH = "AAAAAAAAAAAAAAAAAAAAAA" 
```