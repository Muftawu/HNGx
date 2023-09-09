import calendar
import datetime 
from datetime import date

d = date.today()

def get_date_today():
    return d

def get_day_of_week():
    return calendar.day_name[d.weekday()]

def get_utc_time():
    return datetime.datetime.now()

print(get_utc_time())
