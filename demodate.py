import time


def days_between_dates(dt1, dt2):
    date_format = "%d/%m/%Y"
    a = time.mktime(time.strptime(dt1, date_format))
    b = time.mktime(time.strptime(dt2, date_format))
    delta = b - a
    print(int(delta / 86400))


dt1 = "13/12/2018"
dt2 = "25/2/2019"
print(days_between_dates(dt1, dt2))
