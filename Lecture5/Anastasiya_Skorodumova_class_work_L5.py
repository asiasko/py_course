Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print
<built-in function print>
impot this
SyntaxError: invalid syntax
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

n=10
users=[]
user_a_password=input("pass: ")
pass: 12345
user_a_name=input("name: ")
name: vasia
users.append([user_a_name,user_a_password],)
users
[['vasia', '12345']]
def register():
    user_a_name=input("name: ")
    user_a_password=input("pass: ")
    users.append([user_a_name,user_a_password],)
    print('done')

    
register
<function register at 0x1037ec5e0>
register()
name: kolya
pass: 321
done
users
[['vasia', '12345'], ['kolya', '321']]
for i in range(8):
    register()

    
name: sdfasa
pass: 45
done
name: hgkj
pass: 23
done
name: xfhxggfj
pass: 78
done
name: dfgbxfh
pass: 45
done
name: sdzfg
pass: 43543
done
name: xchggh
pass: 234
done
name: xcbg
pass: 34563
done
name: xcgngjx
pass: 456
done
users
[['vasia', '12345'], ['kolya', '321'], ['sdfasa', '45'], ['hgkj', '23'], ['xfhxggfj', '78'], ['dfgbxfh', '45'], ['sdzfg', '43543'], ['xchggh', '234'], ['xcbg', '34563'], ['xcgngjx', '456']]
users[0]
['vasia', '12345']


def hello():
    print('Hello!')

    
hello()
Hello!
def hello():
    user=input("your name:")
    print(f'Hello! {user}')

    
hello()
your name:asia
Hello! asia
def hello():
    user=input("your name:")
    print(f'Hello, {user}')
    for i in range(3):
        print(i, end=' ')
    d=88
    if d==88:
        print('XXX')
    print(42346234)

    
hello()
your name:fghd
Hello, fghd
0 1 2 XXX
42346234
gogogo()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    gogogo()
NameError: name 'gogogo' is not defined
hello=55
hello()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    hello()
TypeError: 'int' object is not callable
print(hello)
55
input
<built-in function input>

change_password()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    change_password()
NameError: name 'change_password' is not defined
def hi():print('hi')


hi(5)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    hi(5)
TypeError: hi() takes 0 positional arguments but 1 was given
def hello(user):
    print('Hello', user)

    
hello()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'user'
hello(1234)
Hello 1234
hello('sdf')
Hello sdf
hello(1,2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    hello(1,2)
TypeError: hello() takes 1 positional argument but 2 were given
def hello(a,b,c):
    print('Hello', a,b,c)

    
hello(1,2)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    hello(1,2)
TypeError: hello() missing 1 required positional argument: 'c'
hello(1,2,3)
Hello 1 2 3
hello(b=44,c=88,a=99)
Hello 99 44 88
hello(33,c=88,a=99)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    hello(33,c=88,a=99)
TypeError: hello() got multiple values for argument 'a'
hello(33,c=88,b=99)
Hello 33 99 88
hello(c=44,b=88,66)
SyntaxError: positional argument follows keyword argument
def hello(name,age):
    print('Hello', name,age)

    
hello('jojo',28)
Hello jojo 28
hello(28,'jojo')
Hello 28 jojo



def create_order(name,ph,age,msg):
    print("Order 34456: created.")
    print(f"order detailes:")
    print(f"     Name:{name}")
    print(f"     phone:{ph}")
    print(f"     age:{age}")
    print(f"     message:{msg}")
    print()

    
create_order('Goose',123))
SyntaxError: unmatched ')'
create_order('Goose',123)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    create_order('Goose',123)
TypeError: create_order() missing 2 required positional arguments: 'age' and 'msg'
def create_order(name,ph,age='',msg=''):
    print("Order 34456: created.")
    print(f"order detailes:")
    print(f"     Name:{name}")
    print(f"     phone:{ph}")
    print(f"     age:{age}")
    print(f"     message:{msg}")
    print()

    
create_order("Goose",123,18,'call me')
Order 34456: created.
order detailes:
     Name:Goose
     phone:123
     age:18
     message:call me

create_order('goose',123)
Order 34456: created.
order detailes:
     Name:goose
     phone:123
     age:
     message:

create_order('goose')
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    create_order('goose')
TypeError: create_order() missing 1 required positional argument: 'ph'

def a(name='jojo', age=123)
SyntaxError: expected ':'

def a(name='jojo', age=123):
    print(name,age)

    
a()
jojo 123
a('natasha')
natasha 123

name=input("-->")
-->1233456
name
'1233456'

def hello():
    pass




res=hello()
res
print(res)
None
def hello():
    print(1*44)

    
res=hello()
44
print(res)
None
def create_order(name,ph,age='',msg=''):
    if len(name)<2:
        return False
    if str(ph).isallnum()!=True:
        return False
    print("Order 34456: created.")
    print(f"order detailes:")
    print(f"     Name:{name}")
    print(f"     phone:{ph}")
    print(f"     age:{age}")
    print(f"     message:{msg}")
    print()
    return True

res=create_order('',123123)
res
False
def create_order(name,ph,age='',msg=''):
    if len(name)<2:
        return False
    if str(ph).isalnum()!=True:
        return False
    print("Order 34456: created.")
    print(f"order detailes:")
    print(f"     Name:{name}")
    print(f"     phone:{ph}")
    print(f"     age:{age}")
    print(f"     message:{msg}")
    print()
    return True

res=create_order('Jan',123123)
Order 34456: created.
order detailes:
     Name:Jan
     phone:123123
     age:
     message:

res=create_order('Jan',' 123123')
res
False
def create_order(name,ph,age='',msg=''):
    if len(name)<2 or ph.isalnum()!=True:
        return False
    print("Order 34456: created.")
    print(f"order detailes:")
    print(f"     Name:{name}")
    print(f"     phone:{ph}")
    print(f"     age:{age}")
    print(f"     message:{msg}")
    print()
    return True

def Up(name):
    print(name.upper())

    
Up('sdfadf')
SDFADF
def Up(name):
    return name.upper()
upName=UP('sdfdsg')
SyntaxError: invalid syntax
upName=Up('sdfdsg')
SDFDSG
upName
ph=123213421
age=999
msg=12345345
create_order('ssdfd',"123324")
Order 34456: created.
order detailes:
     Name:ssdfd
     phone:123324
     age:
     message:

True
ph
123213421
age
999
help
Type help() for interactive help, or help(object) for help about object.
help()
Welcome to Python 3.13's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.13/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q", "quit" or "exit".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

def create_order(name,ph,age='',msg=''):
    """Функция, которая делает тото/
Параметры,
name---string 
ph --> строка обязательна
age --> строка необязательна
msg --> строка необязательна """
    if len(name)<2 or ph.isalnum()!=True:
        return False
    print("Order 34456: created.")
    print(f"order detailes:")
    print(f"     Name:{name}")
    print(f"     phone:{ph}")
    print(f"     age:{age}")
    print(f"     message:{msg}")
    print()
    return True

help(create_order)
Help on function create_order in module __main__:

create_order(name, ph, age='', msg='')
    Функция, которая делает тото/
    Параметры,
    name---string
    ph --> строка обязательна
    age --> строка необязательна
    msg --> строка необязательна

create_order.__doc__
'Функция, которая делает тото/\nПараметры,\nname---string \nph --> строка обязательна\nage --> строка необязательна\nmsg --> строка необязательна '
def a():
    print(1)

def b():
    print(2)

    
def c():
    print(3)

c()
3
del c
c90
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    c90
NameError: name 'c90' is not defined
c()
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    c()
NameError: name 'c' is not defined
b()
2
qwe=b
b
<function b at 0x1037ee200>
qwe()
2
a()
1
id(a)
4353615296
sss=a
sss()
1
del a
sss()
1

def numbers(num):
    if num%2==0:
        return True
    return None

numbers(2)
True
numbers(3)
print(numbers(3))
None
def numbers(num):
    if num%2==0:
        return True

    
print(numbers(3))
None
print(numbers(2))
True
def numbers(num):
    return num%2==0

print(numbers(3))
False
print(numbers(2))
True
a=10
s='sdsdsd'
isinstance(a,int)
True
isinstance(a,str)
False
isinstance(a,list)
False
if isinstance(a,str):
    print('INT')
elif
SyntaxError: invalid syntax
if isinstance(a,int):
    print('INT')
elif isinstance(a,str):
    print('STRING')

    
INT
isinstance(a,(int,float,str))
True
def check(a):
    if isinstance(a,int):
        print('INT')
    elif isinstance(a,str):
        print('STRRR')

        
check(6)
INT

total=0
def add_to_total(n):
    total=total+n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#213>", line 2, in add_to_total
    total=total+n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
print(total)
0
def add_to_total(n):
    global total=total+n
    
SyntaxError: invalid syntax

x=2183
def add(x):
    print('inside: ',x,id(x))
    x+=8888
    print('inside: ',x,id(x))

    
x
2183
add(x)
inside:  2183 4353475952
inside:  11071 4353476176
x
2183
def add(number):
    print('inside: ',number,id(number))
    number+=8888
    print('inside: ',number,id(number))

    
x
2183
number
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    number
NameError: name 'number' is not defined. Did you mean: 'numbers'?
add(x)
inside:  2183 4353475952
inside:  11071 4353476080
number
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    number
NameError: name 'number' is not defined. Did you mean: 'numbers'?
def add(number):
    print('inside: ',number,id(number))
    global number+=8888
    print('inside: ',number,id(number))
    
SyntaxError: invalid syntax


def a():
    print(1)

    
def b():
    print(2)

    
def c():
    print(3)

    
li=[a,b,c]
li
[<function a at 0x1038142c0>, <function b at 0x103814400>, <function c at 0x103814360>]
for i in li:
    i

    
<function a at 0x1038142c0>
<function b at 0x103814400>

<function c at 0x103814360>







for i in li:
    i()

    
1
2
3


def noname(number):
    if number>20:
        return True
    return number+noname(number+4)

noname(1)
46
# 1+5+9+13+17+21
1+5+9+13+17+21
66
1+5+9+13+17+True
46
import sys
>>> sys.getrecursionlimit()
1000
>>> sys.setrecursionlimit(2000)
>>> sys.getrecursionlimit()
2000
>>> 
>>> 
>>> f1=f2=1
>>> f1
1
>>> f2
1
>>> f1,f2=f2,f1+f2
>>> f1
1
>>> f2
2
>>> f1,f2=f2,f1+f2
>>> f1
2
>>> f2
3
>>> f1,f2=f2,f1+f2
>>> f1
3
>>> f2
5
>>> f1,f2=f2,f1+f2
>>> f1
5
>>> f2
8
>>> f1=f2=1
>>> for i in range(10):
...     f1,f2=f2,f1+f2
... 
...     
>>> f2
144
