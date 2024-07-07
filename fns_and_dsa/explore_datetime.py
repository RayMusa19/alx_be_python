import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    
    print('Current date and time: ', current_date)
    return 

display_current_datetime()

def calculate_future_date():
    Days = int(input('Enter the number of days to add to the current date: '))
    future_date = datetime.date.today() + datetime.timedelta(days=Days)
    print(future_date)

    return
            
calculate_future_date()
