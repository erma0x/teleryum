def kucoin_side(side, trigger ='TAKEPROFIT'):
    '''TAKEPROFIT or STOPLOSS'''
    if side =='buy' and trigger=='TAKEPROFIT':
        return 'up'
    if side =='buy' and trigger=='STOPLOSS':
        return 'down'
    if side =='sell' and trigger=='TAKEPROFIT':
        return 'down'
    if side =='sell' and trigger=='STOPLOSS': 
        return 'up'
    return None

def get_free_balance(exchange):
    balance = exchange.fetch_balance()
    return balance['free']['USDT']

def get_total_balance(exchange):
    balance = exchange.fetch_balance()
    return balance['total']['USDT']

def balance_trigger_orders_quantity(trigger_prices, entry_quantity):
    trigger_quantities = []
    single_trigger_quantity = round( entry_quantity/len(trigger_prices) ,8)
    n_triggers = len(trigger_prices)
    if n_triggers > 1:
        if 0 != entry_quantity % ( single_trigger_quantity * (n_triggers-1) ):
            trigger_quantities = [single_trigger_quantity for i in trigger_prices][:-1]
            last_trigger_quantity = entry_quantity % ( single_trigger_quantity * (n_triggers-1) ) + single_trigger_quantity
            trigger_quantities.append(last_trigger_quantity)
        else:
            trigger_quantities = [single_trigger_quantity for i in trigger_prices]
    else:
        trigger_quantities.append(entry_quantity)
    return trigger_quantities
    
async def get_amount_position_usdt(exchange):
    '''
    Get the amount of USDT avaiable on the exchange for the operation
    '''
    total_balance = get_total_balance(exchange=exchange)

    if total_balance > 300:
        amount_position_usdt =  total_balance * 0.03   # get 3% of the position
    elif total_balance > 200:
        amount_usd_position =  total_balance * 0.1    # get 10% of the position
    else:
        amount_usd_position = 20

    return amount_usd_position


def balance_contract_quantity(trigger_prices, entry_quantity):
    """
    each trigger_quantities must be a multiply of the base increment
    """
    trigger_quantities = []
    if len(trigger_prices)>1:
        trigger_quantities = [ math.ceil(entry_quantity/len(trigger_prices)) for i in trigger_prices]

    else:
        trigger_quantities.append(entry_quantity)

    return trigger_quantities