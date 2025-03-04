Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter +=1
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f"user name: {self.name}."

    
User.get_counter()
0
k = User("Kate")
print(k)
user name: Kate.
k.get_counter()
1
User.get_counter()
1
User.__counter
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    User.__counter
AttributeError: type object 'User' has no attribute '__counter'. Did you mean: 'get_counter'?
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter +=1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    def __str__(self):
        return f"user name: {self.name}."

    
k = User("Kate")
print(k)
user name: Kate.
User.get_counter
<bound method User.get_counter of <class '__main__.User'>>
User.get_counter()
1
User.set_counter(55)
User.get_counter()
55
User.counter = 888
k.get_counter()
55
k.set_counter(6666)
User.get_counter()
6666
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter +=1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    def __str__(self):
        return f"user name: {self.name}."

    
class User:
    __counter = 0
    
    def __init__(self, name):
        self.name = name
        User.__counter +=1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    def __str__(self):
        return f"user name: {self.name}."
    
    @staticmethod
    def check_name(name):
        return False if len(name)<2 else True

    
user1 = "Kate"
if User.check_name(user1):
    inst1 = User(user1)
else:
    print("Имя слишком короткое")

    
print(inst1)
user name: Kate.
user2 = "J"
if User.check_name(user2):
    inst1 = User(user2)
else:
    print("Имя слишком короткое")

    
Имя слишком короткое


class User:
    __counter = 0
    
    def __init__(self, name):
        print("__init__")
        self.name = name
        User.__counter +=1

    @classmethod
    def init_age_including(cls, name, age):
        print("alt __init__")
        user = cls(name)
        user.age = age
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    def __str__(self):
        return f"user name: {self.name}."
    

    
u1 = User("Vova")
__init__
u2 = User.init_age_including("Vova", 19)
alt __init__
__init__
User.get_counter()
2
u1.name
'Vova'
u1.age
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    u1.age
AttributeError: 'User' object has no attribute 'age'
u2.name
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    u2.name
AttributeError: 'NoneType' object has no attribute 'name'
u2.age
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    u2.age
AttributeError: 'NoneType' object has no attribute 'age'
u2
print(u2
      0
      
SyntaxError: '(' was never closed
print(u2)
      
None
u2 = User.init_age_including("Vova", 19)
      
alt __init__
__init__
print(u2)
      
None
# txt csv json xml
      

# prep export status
      
class ExportToTXT:

    def __init__(self, file_name)
    
SyntaxError: expected ':'
class ExportToTXT:
    # петя делает свою таску
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
class ExportToCSV:
    # вася свою часть кода
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to csv", self.file_name)
    def preparation(self):
        print("preparation")

        
class ExportToXML:
    # вася свою часть кода
    def __init__(self, file_name):
        self.f_n = file_name
    def export333(self):
        print("export to xml", self.file_name)
    def gotovka(self):
        print("preparation")
    def check_stts(self):
        print("status")

        
li = [ExportToTXT("1.txt"), ExportToCSV("1.csv"), ExportToXML("1.xml")]
for inst in li:
    inst.export()

    
Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    inst.export()
AttributeError: 'ExportToTXT' object has no attribute 'export'
from abc import ABC, abstractmethod
class Export(ABC):
    @abstractmethod
    def export(self):
        pass
    @abstractmethod
    def prep(self):
        pass
    @abstractmethod
    def status(self):
        pass

    
class ExportToTXT(Export):
    # петя делает свою таску
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
inst = ExportToTXT("sgrthsdyth")
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    inst = ExportToTXT("sgrthsdyth")
TypeError: Can't instantiate abstract class ExportToTXT without an implementation for abstract methods 'export', 'prep', 'status'
class ExportToTXT(Export):
    # петя делает свою таску
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
inst = ExportToTXT("1.txt")
inst.status()
status
keyboardInterrupt
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    keyboardInterrupt
NameError: name 'keyboardInterrupt' is not defined. Did you mean: 'KeyboardInterrupt'?
inst.prep()
prep
inst.export()
export to txt 1.txt
class ExportToCSV:
    # вася свою часть кода
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to csv", self.file_name)
    def preparation(self):
        print("preparation")

        
ExportToCSV("sdf")
<__main__.ExportToCSV object at 0x1029f74d0>
inst2 = ExportToCSV("sdfg.csv")
print(inst2)
<__main__.ExportToCSV object at 0x103064050>
inst2.__dict__
{'file_name': 'sdfg.csv'}
inst2.export()
export to csv sdfg.csv
inst2.prep()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    inst2.prep()
AttributeError: 'ExportToCSV' object has no attribute 'prep'
class ExportToCSV:
    # вася свою часть кода
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to csv", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
class ExportToJSON:
    # вася свою часть кода
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to json", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
li = [ExportToTXT("1.txt"), ExportToCSV("2.csv"), ExportToJSON("n1.json")]
for inst in li:
    inst.export()

    
export to txt 1.txt
export to csv 2.csv
export to json n1.json


class A:
    pass

class B(A):
    pass

class C(B):
    pass
c.__mro__
SyntaxError: invalid syntax
C.__mro__
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    C.__mro__
NameError: name 'C' is not defined
class C(B):
    pass

C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]




class A:
    a = 10

    
class B(A):
    b = 100

    
class C(B):
    c = 1000

    
c=C()
c1 = C()
c1.c
1000
c1.b
100
c1.a
10
c1.d
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    c1.d
AttributeError: 'C' object has no attribute 'd'
class A:
    a = 10
    def __init__(self):
        aaa = 11

        
class B:
    b = 100
    def __init__(self):
        bbb = 111

        
class C(B):
    c = 1000
    def __init__(self):
        ccc = 1111
        super().__init__()

        
c1 = C()
c1.c
1000
c1.ccc
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    c1.ccc
AttributeError: 'C' object has no attribute 'ccc'
class A:
    a = 10
    def __init__(self):
        self.aaa = 11

        
class B:
    b = 100
    def __init__(self):
        self.bbb = 111

        
class C(B):
    c = 1000
    def __init__(self):
        self.ccc = 1111
        super().__init__()

        
c1 = C()
c1.c
1000
c1.ccc
1111
c1.b
100
c1.bbb
111
c1.a
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    c1.a
AttributeError: 'C' object has no attribute 'a'
c1.aaa
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    c1.aaa
AttributeError: 'C' object has no attribute 'aaa'

try:
    raise AttributeError
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
err
fin
try:
    1+1
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
2
ok
fin



def a(number):
    try:
        return number
    except:
        return number+1
    else:
        return number+2
    finally:
        return number ** 10

    
a(10)
10000000000
def a(number):
    try:
        return number
    except:
        return number+1
    else:
        return number+2

    
a(10)
10



class User:
    def __init__(self, name):
        self.name = name
      
    def __str__(self):
        return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            pass
        return f"звоню {number}"

    
class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message

        
raise NumberError(12312, "короткий номер!")
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    raise NumberError(12312, "короткий номер!")
NumberError: (12312, 'короткий номер!')

class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message

        
class User:
    def __init__(self, name):
        self.name = name
      
    def __str__(self):
        return f"user name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            raise NumberError(number, "Короткий номер!")
        return f"звоню {number}"

    
user1 = User("Vasia")
user1.call(1223)
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    user1.call(1223)
  File "<pyshell#234>", line 8, in call
    if len(number) < 8:
TypeError: object of type 'int' has no len()
try:
    user1.call("1223")
except:
    NumberError as e:
        
SyntaxError: invalid syntax
try:
    user1.call("1223")
except:
    NumberError as e:
        
SyntaxError: invalid syntax
try:
    user1.call("1223")
except NumberError as e:
    print(e)
except:
    print("-1")

    
('1223', 'Короткий номер!')
class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message
...     def __str__(self):
...         return f"NumberError: number: {self.number}, {self.message}"
... 
...     
>>> class User:
...     def __init__(self, name):
...         self.name = name
...       
...     def __str__(self):
...         return f"user name: {self.name}."
...     def call(self, number):
...         if len(number) < 8:
...             raise NumberError(number, "Короткий номер!")
...         return f"звоню {number}"
... 
...     
>>> user1 = User("Vasia")
>>> try:
...     user1.call("1223")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
NumberError: number: 1223, Короткий номер!
>>> try:
...     user1.call("12245365376573")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
'звоню 12245365376573'
>>> # phonebook.py
>>> 
>>> 
