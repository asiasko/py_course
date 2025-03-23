#декоратор decorator
def add(a, b):
    return a+b

def add(a,b):
    print("jhvfhgdrts")

    
def add(a,b):
    print("jhvfhgdrts")
    return a+b**2

def add(a, b):
    return a+b

def decorator(func):
    def inner(ia, ib)
    
SyntaxError: expected ':'
def decorator(func):
    def inner(ia, ib):
       print("jhvfhgdrts")
       ib **= 2
       func(ia, ib)
    return inner

add(2,3)
5
@decorator
def add(a, b):
    return a+b

add(2,3)
jhvfhgdrts
res = add(2,3)
jhvfhgdrts
res
@decorator
def add(a, b):
    return a+b

add(2,3)
jhvfhgdrts
@decorator
def add(a, b):
    print(a+b)

    
add(2,3)
jhvfhgdrts
11



def decorator(func):
       print("привет из декоратора")
       func()

       
вуа ыфн()Ж
SyntaxError: invalid syntax
def say():
    print("как дела?")

    
say()
как дела?
@decorator
def say():
    print("как дела?")

    
привет из декоратора
как дела?
say()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    say()
TypeError: 'NoneType' object is not callable
def decorator(func):)
SyntaxError: unmatched ')'
def decorator(func):
    def inner():
        print("привет из декоратора")
        func()
    return inner

@decorator
def say():
    print("как дела?")

    
say()
привет из декоратора
как дела?
say()
привет из декоратора
как дела?
say()
привет из декоратора
как дела?

def decorator(func):
    print("привет из декоратора")
    return func

@decorator
def say():
    print("как дела?")

    
привет из декоратора
say()
как дела?
say()
как дела?
say()
как дела?

def decorator(func):
    def inner():
        print("привет из декоратора")
        func()
    return inner

@decorator
def say():
    print("как дела?")

    
say()
привет из декоратора
как дела?
say()
привет из декоратора
как дела?
@decorator
def bye():
    print("пока")

    
bye()
привет из декоратора
пока
bye()
привет из декоратора
пока
def say(name):
    print(f"{name}, как дела?")

    
def decorator(func):
    def inner(dname):
        print("привет из декоратора")
        func(dname)
    return inner

@decorator
def say(name):
    print(f"{name}, как дела?")

    
say("Петя")
привет из декоратора
Петя, как дела?
