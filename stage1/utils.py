import calendar
import datetime 
from datetime import date

# recommended time : 2023-09-09T15:24:06Z

d = date.today()

def get_date_today():
    return d

def get_day_of_week():
    return calendar.day_name[d.weekday()]

def get_utc_time():
    t = str(datetime.datetime.now()).split('.')[0]
    return t[:10] + 'T' + t[11:] + 'Z'

print(get_utc_time())
