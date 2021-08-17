# own modules

# third party modules

# python modules
from colorama import Fore, Style, init
import fmath
from datetime import timedelta, date
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=100))

print(timedelta(minutes=120))


fmath.substract(10, 8)
fmath.substract(9, 9)
fmath.substract(1, 10)
fmath.add(123, -122)


print("---------------------------------")


init(convert=True)
print(Fore.RED+"Hello World")
print(Fore.BLUE+"Hello World")
print(Fore.GREEN+"Hello World")
print(Fore.CYAN+"Hello World")
print(Fore.YELLOW+"Hello World")
