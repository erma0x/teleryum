# In progress
### PRIORITA

capire se posso usare una sola funzione
trader_ccxt()
o devo fare
trader_ftx
trader_kucoin
trader_kraken
per le diverse api in relazione anche con ccxt


google auth x telerym gmail

⭐ crea account kraken
⭐ crea account kucoin
⭐ api trade 
⭐ api trade 
⭐ api lettura 
⭐ api lettura 
⭐ ccxt kucoin? funziona?
⭐ ccxt kraken? funziona?


⭐ Lungo test con la nuova architettura su RBX -> guarda print dei messaggi
START 15/04/2022 17:39:21
find pid with htop
dura piu di 24h













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


⭐ AGGIUNGI CANALI CON I MESSAGGI

🔻 TEST LIVE DEI MESSAGGI DI 10 GRUPPI CONTEMPORANEAMENTE 
    ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=2 $HOSTNAME
    python3 teleryum.py  
    
    > DISCONNETTE DOPO 30 MIN con 2 min di MaxTimeout e senza nohup
    ho alzato a 20 min il timeout del ssh e con nohup se non devo avere i print

⭐ TEST LIVE DEI MESSAGGI DI 10 GRUPPI CONTEMPORANEAMENTE 
    ssh -o ServerAliveInterval=5 -o ServerAliveCountMax=2 $HOSTNAME
    python3 teleryum.py  
    > FIX await architecture

⭐ FIX NOHUP output and errors deamon

⭐ Test messaggi che arrivano su log.out di nohup con python3 -u
    pid 990595
    
     OK DEAMON 
    nohup python3 -u teleryum.py > log.out 2> log.err & 
    
    spit out the pid process 
    if u want to kill it : kill -9 

⭐ test nohup python3 -u teleryum.py > log.out 2> log.err & FUNZIONANTE per 20h consecutive
    -> cambio architettura con client.loop.run_forever()

⭐ demone funzionante: disponibile da guardare con 'htop'

🔻 EXPLORATION passa ad okex con ccxt-rest su github
    -> ci spostiamo su ftx, kraken e kucoin


⭐ capire a quale gruppo affidarsi per i test, creato il file groups_raw.txt


⭐ capire a quale exchange affidarsi e con quale strumento
puntare su okex con leva x10, kucoin x2/x5, ftx x2
    -> ci spostiamo su ftx, kraken e kucoin