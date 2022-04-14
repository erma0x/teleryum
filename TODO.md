# In progress

⭐ AGGIUNGI CANALI





# Done

⭐ capire come fare 1 OP con 1TP e 1SL
    guarda tests/ccxt per gli esempi

⭐ capire come fare 1 OP con 3TP e 1SL, 
    guarda tests/ccxt per gli esempi

⭐ cambio di STRUTTURA DATI
    unavolta capito come fare le op in manuale
    e con degli script di prova, devi generare 
    una struttura dati che possa soddisfare tutti i canali.

⭐ FROM MESSAGE TO OP_DATA TO TRADE

    mandare operazioni di un canale offline con
    dei messaggi fax simili di un canale specifico.
    Da un unico messaggio son passato a 
    trasformarlo nella struttura 
    dati univoca per turtti desiderata

⭐  LIVE TEST message freecrypto_singal
      ->  OP_DATA -> TRADE 

    mandare operazioni di un canale online FAX SIMILE

⭐  FTX TOKEN FILTER

    capire se il token del segnale e' 
    presente su ftx e farci una funzione che
    ritorna un booleano che permette o meno
    di fare ordini su ftx

⭐  estetics
   fix imports and add simplicity


⭐  aggiungi freecrypto_signals in live

⭐  reformat del progetto per esporre meno chiavi possibili

⭐ BUG 1: quando apro piu TP o SL rimangono fuori pochi spiccioli che non verranno chiusi. Da fillare completamente. Se e'l'ultimo trade allora filla con la sua:  
    
    n_tp = 3
    quantita_entry = 2.0
    quantita_singolo_TP = 0.6

    quantita_ultimo_TP/SL  =  quantita_entry - quantita_singolo_TP  * n_TP

    [ quantita_ultimo_TP/SL = 0.8 ] 


⭐ tokenomics

⭐ rebalance delle posizioni, ognuna con max il 3% del capitale
    ed a scaglioni con capitali inferiori

⭐ api get aviable and free balance ftx

⭐ test fix bug 1

⭐ server redbox setup

⭐ ccxt.okex     open okex account

⭐ ccxt.okex    generate API READONLY

⭐ TEST freecrypto_signals FTX live on REDBOX: lascio per una notte

⭐ TEST pubblico FTX live on REDBOX: dopo tot tempo funziona

⭐ TEST domani prova un messaggio sul canale e verifica che dopo 8h lo script funziona ancora

⭐ TEST nohup su server e su locale

⭐ BUG freecrypto_signal errore su messaggio semplice con piu entry price 

⭐ BUG il secondo entry mi dice che ho la size proppo piccola
        #ETH 
        Buy 2500-2600
        Sell 3500-3550-3600
        Stoploss 1950-1900
        By (@SN_crypto)

            raise exact[string](message)
        ccxt.base.errors.InvalidOrder: ftx {"success":false,"error":"Size too small"}

⭐TEST MASSIMO ORDINI TRIGGER SU UN FTX PER L'ACCOUNT MAIN

⭐ resetta trading api main con FTX con sicurezza aggiuntiva (con ip)

⭐  crea trading api ftx c1 (con ip)

⭐  crea trading api ftx c2 (con ip)

⭐  fix api ip security ftx subaccounts

⭐ TESTA se il tetto a 25 triggers su FTX e' assoluto o per subaccount (compreso quindi anche il main)
    25 open triggers per ogni subaccount (compreso quindi anche il main)

⭐ ccxt.okex    INVIA CAPITALE TEST 3$

⭐ SETUP SERVER for live test c1 : check possible bugs il local before lunch it
TEST con messaggi semplici
TEST con messaggi complessi

⭐ ADD SIMPLICITY

⭐ live test RBX
PID 941873

⭐  ccxt.okex    INVIA CAPITALE medio (30$)

⭐ ccxt.okex    generate API OPERATIVE

🔻 ccxt.okex    test with ccxt XXX not found sufficent code development on ccxt/okex.py , try other 3rth party tools on github for interacting with API V5

⭐ explored alternative exchanges

🔻 manda sul server il canale 1 live e prova => test non riuscito per disconnessione da tg

🔻 test binance.eu vpn from poland => richiede il KYC

🔻 api get_aviable and get_free balance okex ==> not solved

⭐ test ftx offline

⭐ ASYNCIO cambio architettura telethon sync => telethon async 
trasforma l'architettura
    
    - BUG 1 sqlite3.OperationalError: database is locked
        SOLVE: https://www.rhumbarlv.com/how-do-i-fix-sqlite3-operationalerror-database-is-locked/
⭐ Github new personal access token from for early expiry

🔻  ASYNCIO cambio architettura telethon sync => telethon async 
trasforma l'architettura
    python-deamon prova a creare un demone invece di utilizzare nohup

⭐  ASYNCIO cambio architettura telethon sync => telethon async 
trasforma l'architettura
    SENZA python-deamon,
    
    ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=2 $HOSTNAME
    python3 teleryum.py  