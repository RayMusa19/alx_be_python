from datetime import datetime, timedelta, date

def display_current_datetime():
    dt = datetime.now()
    current_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    print('Current date and time: ', current_date)
    return 

display_current_datetime()

def calculate_future_date():
    Days = int(input('Enter the number of days to add to the current date: '))
    future = date.today() + timedelta(days=Days)
    future_date = future.strftime("%Y-%m-%d")
    print(future_date)

    return
            
calculate_future_date()
