#lab
import datetime
datetime.datetime.now()
datetime.datetime(2025, 3, 5, 19, 46, 18, 454358)
datetime.datetime.now()
datetime.datetime(2025, 3, 5, 19, 46, 28, 787853)
say.__name__
'inner'
print(datetime.datetime.now())
2025-03-05 19:47:09.950677
def decorator(func):
    def inner(dname):
        print("привет из декоратора")
        print("Время запуска", datetime.datetime.now())
        print("Имя функции которая запускается", func.__name__)
        func(dname)
    return inner

@decorator
def say(name):
    print(f"{name}, как дела?")

    
def bye(name):
    print(f"{name}, пока")

    
say('Petya')
привет из декоратора
Время запуска 2025-03-05 19:51:36.849212
Имя функции которая запускается say
Petya, как дела?
bye('Petya')
Petya, пока
