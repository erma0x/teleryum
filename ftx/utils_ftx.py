def get_free_balance_ftx():
    client = FtxClient(api_key=FTX_READONLY_C1,api_secret=FTX_READONLY_C1_HASH,subaccount_name='c1')
    free_balance = client.get_balances()[0]['free']
    #print('YOUR FREE BALANCE: '+str(round(free_balance,2)))
    return float(free_balance)

def get_total_balance_ftx( percentage_for_position=0.03 ):
    client = FtxClient(api_key=FTX_READONLY_C1,api_secret=FTX_READONLY_C1_HASH,subaccount_name='c1')
    total_balance = client.get_balances()[0]['total']
    return float(total_balance)

async def get_amount_position_usdt_ftx():
    total_balance = get_total_balance_ftx()
    if total_balance > 300:
        amount_position_usdt =  total_balance * 0.03   # get 3% of the position
    elif total_balance > 200:
        amount_usd_position =  total_balance * 0.1    # get 10% of the position
    else:
        amount_usd_position = 20

    return amount_usd_position