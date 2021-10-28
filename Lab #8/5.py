import datetime
print(datetime.datetime(int(input('Введите год: ')), 1, 1) + datetime.timedelta(int(input('Введите порядковый номер дня: ')) - 1))
