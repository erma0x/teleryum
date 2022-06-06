from datetime import datetime

def parser_wolfxsignals(text_message):

    op_data={'side':'','symbol':'','take_profits':[],'entry_prices':[],'stop_losses':[],'laverage':1}

    TEXT_PATTERNS = ('/','TP','SL','️Leverage','x')

    for pattern in TEXT_PATTERNS:
        if pattern not in text_message:
            return False

    date = str(datetime.now())
    for row in text_message.split('\n'):
        if '/' in row:
            op_data['symbol'] = row[1:].split('/')[0]#.replace(' ','').replace('#','')

        if row.find('SELL'):
            op_data['side']='short'

        if row.find('BUY'):
            op_data['side']='buy'

        if op_data['side']:
            if 'TP' in row:
                temp = row.split()[1].split(' ')
                temp_list = []
                for n in range(len(temp)):
                    temp_list.append(temp[n])
                
                op_data['take_profits'] = temp_list

            if 'SL' in row:
                temp = row.split()[1].split(' ')
                temp_list = []
                for n in range(len(temp)):
                    temp_list.append(temp[n])

                op_data['stop_losses']= temp_list

            if 'Enter' in row:
                temp=''.join(row.split(' ')[2]).split('-')
                list_entry_prices = []
                for i in temp:
                    list_entry_prices.append(i)
                
                op_data['entry_prices'] = list_entry_prices

        if 'Leverage' in row:
            op_data['laverage']  = row.split()[1].replace('x','')

    return op_data