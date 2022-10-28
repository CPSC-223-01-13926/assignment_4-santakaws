# Lab 4
# Author: Brennon Hahs

import json
import calendar

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return {}

def write_data(data, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

def max_temperature(data, date):
    x = -200
    for key in data:
        if key[0:8] == date and data[key]['t'] > x:
            x = data[key]['t']
    return x

def min_temperature(data, date):
    x = 200
    for key in data:
        if key[0:8] == date and data[key]['t'] < x:
            x = data[key]['t']
    return x

def max_humidity(data, date):
    x = 0
    for key in data:
        if key[0:8] == date and data[key]['h'] > x:
            x = data[key]['h']
    return x

def min_humidity(data, date):
    x = 100
    for key in data:
        if key[0:8] == date and data[key]['h'] < x:
            x = data[key]['h']
    return x

def tot_rain(data, date):
    sum_rain = 0
    for key in data:
        if key[0:8] == date:
            sum_rain += data[key]['r']
    return sum_rain

def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display += 'Date                      Time  Temperature  Humidity  Rainfall\n'
    display += '====================  ========  ===========  ========  ========\n'

    for key in data:
        if key[0:8] == date:
            m = calendar.month_name[int(date[4:6])]
            d = ' ' + str(int(date[6:8])) + ', '
            y = str(int(date[0:4]))
            mdy = m+d+y

            tm = key[8:10] + ':' + key[10:12] + ':' + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            display = display + f'{mdy: <22}' + f'{tm: <10}' + f'{t: >11}' + f'{h: >10}' + f'{r: >10}\n'
    
    return display

def report_historical(data):
    display =  '============================== HISTORICAL REPORT ===========================\n'
    display += '                          Minimum      Maximum   Minumum   Maximum     Total\n'
    display += 'Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n'
    display += '====================  ===========  ===========  ========  ========  ========\n'
    key_list = []

    for key in data:
        if key[0:8] not in key_list:
            key_list.append(key[0:8])
            m = calendar.month_name[int(key[4:6])]
            d = ' ' + str(int(key[6:8])) + ', '
            y = str(int(key[0:4]))
            mdy = m+d+y
            mint = min_temperature(data=data, date=key[0:8])
            maxt = max_temperature(data=data, date=key[0:8])
            minh = min_humidity(data=data, date=key[0:8])
            maxh = max_humidity(data=data, date=key[0:8])
            totr = tot_rain(data=data, date=key[0:8])
            totrc = f'{totr:.2f}'
            display += f'{mdy: <20}{mint: >13}{maxt: >13}{minh: >10}{maxh: >10}{totrc: >10}\n'
    
    return display
        