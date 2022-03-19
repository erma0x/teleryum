exchange = ccxt.binance()


exchange.fetchTicker('BTC/USDT')

exchange.fetchTicker('BTC/USDT')['last']   # LAST PRICE

enableRateLimit = True

cosa = 'BTC/USDT'

excange.createMarketBuyOrder(cosa, quanto)
excange.createLimitSellOrder(cosa, quanto, prezo)


def quanto_in_dollari(cosa, quanto):
   return quanto/excange.createMarketBuyOrder(cosa)['last']
    
    
excange.createMarketBuyOrder(cosa, quanto_in_dollari(quanto))
