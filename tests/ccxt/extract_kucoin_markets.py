from kucoin_markets import *

for k,v in kucoin_markets.items():
    print("'",k,"'",':',v['contractSize'],",")