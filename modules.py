def add(a,b):
    return a+b

def mulitply(a,b):
    return a*b
===========================
import math
print(math.sqrt(25))
print(math.ceil(25))
print(math.floor(25.5))
print(math.pi)
======================================
import os 
print(os.getcwd)
print(os.listdir)
print(os.mkdir('new folder'))
=================================================
from datetime import datetime, date, timedelta
now= datetime.now()
print(now.year,now.month,now.day)
print(now.strftime(' %H : %M : %S '))
today=date.today()
print(today)
tomorrow= today + timedelta(days = 4)
print(tomorrow)
diff = datetime(2026,1,1) - datetime.now()
print(diff)