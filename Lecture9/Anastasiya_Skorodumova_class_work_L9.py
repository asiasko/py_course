Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class Dog:
    pass

class Car:
    pass

class Lada:
    pass

class Wallet:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
class Dog:
    def __init__(self, name, age)
    
SyntaxError: expected ':'
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
d = Dog()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = Dog()
TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
d = Dog('Bobik', 34)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
dima = User('Dima', 'dima@fdhg.com')
type(d)
<class '__main__.Dog'>
type(dima)
<class '__main__.User'>
isinstance(dima, User)
True
isinstance(dima, Dog)
False
dima.name
'Dima'
dima.email
'dima@fdhg.com'
d.age
34
d.name
'Bobik'
vova = User('Vova', 'vova@fdhg.com')
dima.name
'Dima'
vova.name
'Vova'
User.email
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    User.email
AttributeError: type object 'User' has no attribute 'email'
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
User.users_counter
0
User.users_counter = 666
User.users_counter
666
User.users_counter += 1
User.users_counter
667
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter +=1

        
User.users_counter
0
dima = User('Dima','@')
vi = User('Vi','@')
User.users_counter
2
vi.users_counter
2
dima.users_counter
2
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter = 1

        
User.users_counter
0
d = User('Di','@')
User.users_counter
1
d.users_counter
1
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
d = User('Di','@')
v = User('Vi','@')
c = User('Ci','@')
User.users_counter
3
c.users_counter
3
c.users_counter = 555
User.users_counter

3
v.users_counter
3
d.mobile='2354546737'
c.name
'Ci'
c.mobile
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    c.mobile
AttributeError: 'User' object has no attribute 'mobile'
User.jojo=9999
User.jojo
9999
d.jojo
9999

class Wallet:
    """ представляет структуру полей для описания кошелька"""
    counter = 0
    def __init__(self, owner, currency, amount,address='',color='silver'):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.address = address
        self.color = color
        Wallet.wallet_id+=1
        self.wallet_id=Wallet.counter*10

        
Wallet.counter
0
fw=Wallet('S F', "BYN", 1000)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    fw=Wallet('S F', "BYN", 1000)
  File "<pyshell#82>", line 10, in __init__
    Wallet.wallet_id+=1
AttributeError: type object 'Wallet' has no attribute 'wallet_id'
fw=Wallet('S F', 'BYN', 1000)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    fw=Wallet('S F', 'BYN', 1000)
  File "<pyshell#82>", line 10, in __init__
    Wallet.wallet_id+=1
AttributeError: type object 'Wallet' has no attribute 'wallet_id'
class Wallet:
    """ представляет структуру полей для описания кошелька"""
    counter = 0
    def __init__(self, owner, currency, amount,address='',color='silver'):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.address = address
        self.color = color
        Wallet.counter+=1
        self.wallet_id=Wallet.counter*10

Wallet.counter
0
fw=Wallet('S F', "BYN", 1000)
fw.owner
'S F'
fw.currency
'BYN'
fw.amount
1000
fw.addres
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    fw.addres
AttributeError: 'Wallet' object has no attribute 'addres'. Did you mean: 'address'?
fw.address
''
fw.color
'silver'
sw=Wallet('D F', 'RUB', 100000, color='GOLD')
Wallet.counter
2
sw.color
'GOLD'
sw.wallet_id
20
wallet.__doc__
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    wallet.__doc__
NameError: name 'wallet' is not defined. Did you mean: 'Wallet'?
Wallet.__doc__
'представляет структуру полей для описания кошелька'
Wallet.__name__
'Wallet'
Wallet.__module__
'__main__'
Wallet.__bases__
(<class 'object'>,)
fw.__dict__
{'owner': 'S F', 'currency': 'BYN', 'amount': 1000, 'address': '', 'color': 'silver', 'wallet_id': 10}
sw.__dict__
{'owner': 'D F', 'currency': 'RUB', 'amount': 100000, 'address': '', 'color': 'GOLD', 'wallet_id': 20}
for k,v in fw.__dict__.items():
    print(k, ':',v)

    
owner : S F
currency : BYN
amount : 1000
address : 
color : silver
wallet_id : 10
for k,v in sw.__dict__.items():
    print(k, ':',v)

    
owner : D F
currency : RUB
amount : 100000
address : 
color : GOLD
wallet_id : 20


    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
SyntaxError: unexpected indent
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self,message):
        print(f"{self.name} says {message}!")

        
d1=User('Dima', '@')
d1.name
'Dima'
d1.hello
<bound method User.hello of <__main__.User object at 0x102cd2cf0>>
print
<built-in function print>
d1.hello()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    d1.hello()
TypeError: User.hello() missing 1 required positional argument: 'message'
d1.hello('hello there')
Dima says hello there!
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self,message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye-bye")

        
d1=User('Dima', '@')
d1.hello('sdfh')
Dima says sdfh!
d1.bye()
Dima says bye-bye

st='hello'
print(st)
hello
print(d1)
<__main__.User object at 0x102cd2e40>
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self,message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye-bye")
    def __str__(self):
        return f"User: name-{self.name}, email-{self.email}."

    
kate=User('Kate','kate3454@gmail.com')
kate.hello('dsgtsrse')
Kate says dsgtsrse!
kate.bye()
Kate says bye-bye
print(kate)
User: name-Kate, email-kate3454@gmail.com.
a=123
print(a)
123
dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
dir(User)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'bye', 'hello']


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self,message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye-bye")
    def __str__(self):
        return f"User: name-{self.name}, email-{self.email}."

    
class Storage:
    counter_id=0
    def __init__(self):
        self.storage = {}
    def add_user(self,user):
        Storage.counter_id+=1
        self.Storage.update([Storage.counter_id:user])
    def show_all(self):
        for user_id,user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print('__str__')
            print(user)
            print(user.bye())
            
SyntaxError: invalid syntax
class Storage:
    counter_id=0
    def __init__(self):
        self.storage = {}
    def add_user(self,user):
        Storage.counter_id+=1
        self.storage.update([Storage.counter_id:user])
    def show_all(self):
        for user_id,user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print('__str__')
            print(user)
            print(user.bye())

SyntaxError: invalid syntax

class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"User id:{user_id}")
            print(f"    Name:{user.name}")
            print(f"    Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "fsghsfdg")
kate=User('Kate','sdgrtegyetr')
vas=User('Vas','sredgrter')
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vas)
strg.show_all()
User id:1
    Name:Dima
    Email:fsghsfdg
__str__
User: name-Dima, email-fsghsfdg.
Dima says bye-bye
None
User id:2
    Name:Kate
    Email:sdgrtegyetr
__str__
User: name-Kate, email-sdgrtegyetr.
Kate says bye-bye
None
User id:3
    Name:Vas
    Email:sredgrter
__str__
User: name-Vas, email-sredgrter.
Vas says bye-bye
None















class Car:
    def __init__(self,vin,volume,model_name):
        self.vin=vin
        self.volume=volume
        self.model_name=model_name
    def __str__(self):
        return "привет из родительского класса"

    
class Sedan:
    pass

class Wagon:
    pass

Sedan.__bases__
(<class 'object'>,)
s=Sedan()
s
<__main__.Sedan object at 0x102cd2cf0>
class Sedan(Car):
    pass

class Wagon(Car):
    pass

Sedan.__bases__
(<class '__main__.Car'>,)
Wagon.__bases__
(<class '__main__.Car'>,)
s=Sedan()
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    s=Sedan()
TypeError: Car.__init__() missing 3 required positional arguments: 'vin', 'volume', and 'model_name'
s=Sedan('12343556732', 1.7, 'Megane')
print(s)
привет из родительского класса
isistance(s, Sedan)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    isistance(s, Sedan)
NameError: name 'isistance' is not defined. Did you mean: 'isinstance'?
isinstance(s,Sedan)
True
isinstance(s,Car)
True
class Car:
    def __init__(self,vin,volume,model_name):
        self.vin=vin
        self.volume=volume
        self.model_name=model_name
    def __str__(self):
        return "привет из родительского класса"
    def drive(self):
        print('врум врум врум')

        
class Sedan(Car):
    pass

class Wagon(Car):
    pass

w=Wagon(1232353465, 1.3,'12345')
w.__dict__
{'vin': 1232353465, 'volume': 1.3, 'model_name': '12345'}
car.__dict__
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    car.__dict__
NameError: name 'car' is not defined. Did you mean: 'Car'?
Car.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Car.__init__ at 0x1033022a0>, '__str__': <function Car.__str__ at 0x103302340>, 'drive': <function Car.drive at 0x1033023e0>, '__static_attributes__': ('model_name', 'vin', 'volume'), '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
w.drive()
врум врум врум
class Sedan(Car):
    def drive(self):
        print('sedan delaet brrrrr')

        
s=Sedan(123234535,3.3,'sdgfrg')
s.drive()
sedan delaet brrrrr
class Wagon(Car):
    pass

w=Wagon(1232353465, 1.3,'12345')
w.drive()
врум врум врум
class Sedan(Car):
    def drive(self):
        super().drive()print('sedan delaet brrrrr')
        
SyntaxError: invalid syntax
class Sedan(Car):
    def drive(self):
        super().drive()print('sedan delaet brrrrr')
        
SyntaxError: invalid syntax
class Sedan(Car):
    def drive(self):
        super().drive()print('sedan delaet brrrrr')
        
SyntaxError: invalid syntax
class Sedan(Car):
    def drive(self):
        super().drive() print('sedan delaet brrrrr')
        
SyntaxError: invalid syntax
class Sedan(Car):
    def drive(self):
        super().drive()
        print('sedan delaet brrrrr')

        
w=Wagon(1232353465, 1.3,'12345')

s=Sedan(43524567, 3.3,'dfgh')
w.drive()
врум врум врум
s.drive()
врум врум врум
sedan delaet brrrrr




class Car:
    def __init__(self,vin,volume,model_name):
        self.vin=vin
        self.volume=volume
        self.model_name=model_name
    def __str__(self):
        return "привет из родительского класса"
    def drive(self):
        print('врум врум врум')
    def show_car(self):
        print(self.vin,self.volume,self.model_name)

        
class Sedan(Car):
    def __init__(self):
        self.body_type='Sedan'
    def drive(self):
        super().drive()
        print('sedan delaet brrrrr')

        
s=Sedan(235446563, 3.3, 'sdgdfghrt')
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    s=Sedan(235446563, 3.3, 'sdgdfghrt')
TypeError: Sedan.__init__() takes 1 positional argument but 4 were given
s=Sedan()
s.drive()
врум врум врум
sedan delaet brrrrr
s.show_car()
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    s.show_car()
  File "<pyshell#260>", line 11, in show_car
    print(self.vin,self.volume,self.model_name)
AttributeError: 'Sedan' object has no attribute 'vin'


class Car:
    def __init__(self,vin,volume,model_name):
        self.vin=vin
        self.volume=volume
        self.model_name=model_name
    def __str__(self):
        return "привет из родительского класса"
    def drive(self):
        print('врум врум врум')
    def show_car(self):
        print(self.vin,self.volume,self.model_name)

        
class Sedan(Car):
    def __init__(self,vin,volume,model_name):
        self.body_type='Sedan'
        super().__init__(vin,volume,model_name)
    def drive(self):
        super().drive()
        print('sedan delaet brrrrr')

        
s=Sedan(235446563, 3.3, 'sdgdfghrt')

s.body_type
'Sedan'
s.vin
235446563
s.volume
3.3
s.model_name
'sdgdfghrt'
s.show_car()
235446563 3.3 sdgdfghrt

money = 2341435652
money=-12423453
class Wallet:
    def __init__(self,money):
        self.money=money

        
wall=Wallet(1232432534)
wall.money=-12435436
wall.money
-12435436
class Wallet:
    def __init__(self,money):
        self.__money=money

        
wall=Wallet(1232432534)
wall.money
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    wall.money
AttributeError: 'Wallet' object has no attribute 'money'
>>> wall.money=-21435
>>> class Wallet:
...     def __init__(self,money):
...         self.__money=money
...     def read(self,secret):
...         if secret==123:
...             return self.__money
...         return 'unauthorised'
...     def add(self, amount,secret):
...         if secret!=123:
...             return 'unauthorised'
...         if amount>0:
...             self.__money+=amount
...         return 'unauthorised'
... 
...     
>>> my_wallet=Wallet(100)
>>> my_walley.money
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    my_walley.money
NameError: name 'my_walley' is not defined. Did you mean: 'my_wallet'?
>>> my_wallet.__money
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    my_wallet.__money
AttributeError: 'Wallet' object has no attribute '__money'
>>> my_wallet.read(321)
'unauthorised'
>>> my_wallet.read(123)
100
>>> 
>>> 
