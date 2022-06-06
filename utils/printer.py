from termcolor import colored

def print_start():
    print(colored(LOGO,"cyan"))
    now = datetime.now(tzinfo)
    print(colored("\t SERVER ONLINE ","green"),now.strftime("%d/%m/%Y %H:%M:%S\n\n"))

def print_op_data(op_data):
    print(colored('OPERATION DATA','cyan'))
    print('symbol         \t',op_data['symbol'])
    print('trade side     \t',op_data['side'])
    print('entry prices   \t',' '.join(op_data['entry_prices']))
    print('take profits   \t',' '.join(op_data['take_profits']))
    print('stop losses    \t',' '.join(op_data['stop_losses']))
    print('leverage       \t',op_data['leverage'])

def print_message(message,channel):
    print('~'*70)
    print('\n',colored('NEW SIGNAL','green'),colored(channel,'cyan'),'\t', str(datetime.now(tzinfo))[:-13],'\n\n',message,'\n')
