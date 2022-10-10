import weather

w_data = {}

while True:
    print('      *** TUFFY TITAN WEATHER LOGGER MAIN MENU \n\n')
    print('1. Set data filename')
    print('2. Add weather data')
    print('3. Print daily report')
    print('4. Print historical report')
    print('5. Exit the program \n\n')
    user_in = int(input('Enter menu choice: '))
    print('\n')
    
    if user_in == 1:
        filename = input('Enter data filename: ')
        print('\n')
        w_data = weather.read_data(filename=filename)
    elif user_in == 2:
        date = input('Enter date (YYYYMMDD): ')
        time = input('Enter time (hhmmss): ')
        temp = input('Enter temperature: ')
        hum = input('Enter humidity: ')
        rain = input('Enter rainfall: ')
        w_data = {date+time:{'t':temp, 'h':hum, 'r':rain}}
        weather.write_data(data=w_data, filename='w.dat')
        print('\n')
    elif user_in == 3:
        date = input('Enter date (YYYYMMDD): ')
        print('\n')
        print(weather.report_daily(data=w_data, date=date))
    elif user_in == 4:
        print('\n')
        print(weather.report_historical(data=w_data))
    elif user_in == 5:
        quit()
    else:
        print('Invalid choice. Re-enter menu choice.\n')
