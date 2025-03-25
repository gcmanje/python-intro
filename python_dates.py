from datetime import date, timedelta

today = date.today()
print(today)

f_day = today.strftime(" %a %d-%m-%Y")
print(f_day)

date_after_65_days = today + timedelta(days=65)
print(date_after_65_days)

# 2025-01-15 1995-09-06
# number of days
# number of weeks
# number of months

do=date(2025 ,1 ,15)
d1=date( 1995 ,9, 6)
delta=do-d1
print(delta)

diff =date( 2025,1,15)-date( 1995,9,6)
print(diff.days)

#pip install pillow
