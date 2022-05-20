import sys

project_folder = sys.path[0].replace('utils')

print_op = True


base_operation_data_structure = {'side':'',
                        'symbol':'',
                        'take_profits':[],
                        'entry_prices':[],
                        'stop_losses':[],
                        'laverage':10}
                        
        # {'side': 'buy',
        #  'symbol': 'ETH-PERP',
        #  'take_profits': ['3400', '3300','3200'],
        #  'entry_prices': ['2900', '3000'], 
        # 'stop_losses': ['2000','1900'],
        # 'laverage': 10}
