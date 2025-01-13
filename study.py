import datetime

now = datetime.datetime.now()
print(now)

current_time = datetime.datetime.now().time()
print(current_time)

date_str = "2024-12-01"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)

formatted_date = now.strftime("%d/%m/%Y")
print(formatted_date)

date1 = datetime.date(2024, 12, 1)
date2 = datetime.date(2023, 12, 1)
delta = date1 - date2 
print(delta.days)

tz = pytz.timezone('Europe/Moscow')
datetime_moscow = datetime.now(tz)
print(datetime_moscow)      
