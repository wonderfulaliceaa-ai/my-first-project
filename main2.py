
import datetime
date1 = datetime.datetime(3024, 2, 29, 12)
print(date1)
print(type(date1))

date2 = datetime.date(3024, 2, 1)
date3 = datetime.time(23, 2, 29, 34)
print(date2)
print(date3)





print()
date5 = datetime.datetime.now()

# %A - день тижня
# %a - день тижня скоречено
# %d - номер дня
# %b - назва місяця скорочено
# %B - назва місяця
# %m - номер місяця
# %y - номер року 2 цифри
# %Y - номер року 4 цифри
print(date5.strftime("%a"))
print(date5.strftime("%A"))
print(date5.strftime("%d"))
print(date5.strftime("%b"))
print(date5.strftime("%B"))
print(date5.strftime("%m"))
print(date5.strftime("%Y"))
print(date5.strftime("%y"))
# %H - години
# %I - гидини am/pm
# %M - хвилини
# %S - секунди
print(date5.strftime("%H"))
print(date5.strftime("%I"))
print(date5.strftime("%M"))
print(date5.strftime("%S"))

