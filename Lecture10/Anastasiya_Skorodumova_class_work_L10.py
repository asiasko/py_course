Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class Car:
    def __init__(self,brand,vol):
        self.brand=brand
        self.volume=vol
    def __str__(self):
        return f"{self.brand}:{self.volume}"

    
my_car=Car('VAZ', 1.8)
print(my_car)
VAZ:1.8
class Car:
    def __init__(kitty,brand,vol):
        kitty.brand=brand
        kitty.volume=vol
    def __str__(kitty):
        return f"{kitty.brand}:{kitty.volume}"

    
my_car=Car('VAZ', 0.8)
print(my_car)
VAZ:0.8
class Car:
    def __init__(self,brand,vol):
        self.brand=brand
        self.volume=vol
    def __str__(self):
        return f"str - {self.brand}:{self.volume}"
    def __repr__(self):
        return f"repr - {self.brand}:{self.volume}"

    
my_new_car=Car('ZAZ',1.2)
my_new_car
repr - ZAZ:1.2
print(my_new_car)
str - ZAZ:1.2
class Car:
    def __init__(self,brand,vol):
        self.brand=brand
        self.volume=vol
    def __str__(self):
        return f"str - {self.brand}:{self.volume}"
    def __repr__(self):
        return f"Inst of Car: \n\tBrand: - {self.brand}:\n\tVolume:{self.volume}"

    
my_new_car=Car('ZAZ',1.2)
my_new_car
Inst of Car: 
	Brand: - ZAZ:
	Volume:1.2
my_new_car.volume
1.2
my_new_car.volume=12.5
.volume
SyntaxError: invalid syntax
my_new_car
Inst of Car: 
	Brand: - ZAZ:
	Volume:12.5
class Car:
    counter=0
    def __init__(self,brand,vol):
        self.brand=brand
        self.volume=vol
        Car.counter+=1
    def __str__(self):
        return f"str - {self.brand}:{self.volume}"
    def __repr__(self):
        return f"Inst of Car: \n\tBrand: - {self.brand}:\n\tVolume:{self.volume}"

    
Car.counter
0
my_new_car=Car('ZAZ',1.2)
Car.counter
1
my_new_car2=Car('ZAZ',2.2)
Car.counter
2
Car.__doc__
Car.__bases__
(<class 'object'>,)
class Empty:
    pass
e=Empty()
SyntaxError: invalid syntax
class Empty:
    pass

e=Empty()
Empty.__bases
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    Empty.__bases
AttributeError: type object 'Empty' has no attribute '__bases'
Empty.__bases__
(<class 'object'>,)
e
<__main__.Empty object at 0x100f56ba0>
my_new_car=Car('ZAZ',1.2)
my_new_car.drive(123)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    my_new_car.drive(123)
AttributeError: 'Car' object has no attribute 'drive'
hasattr
<built-in function hasattr>
setattr
<built-in function setattr>
getattr
<built-in function getattr>
my_new_car
Inst of Car: 
	Brand: - ZAZ:
	Volume:1.2
my_new_car.brand
'ZAZ'
getattr(my_new_car, 'brand')
'ZAZ'
getattr(my_new_car, 'bra')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    getattr(my_new_car, 'bra')
AttributeError: 'Car' object has no attribute 'bra'
getattr(my_new_car, 'bra', False)
False
res=getattr(my_new_car, 'bra', False)
res
False
res=getattr(my_new_car, 'brand')
res
'ZAZ'
if getattr(my_new_car, 'brand')!=False:
    print(my_new_car.brand)

    
ZAZ
hasattr
<built-in function hasattr>
hasattr(my_new_car, 'brand')
True
hasattr(my_new_car, 'brd')
False
if hasattr(my_new_car, 'brand'):
    print(my_new_car.brand)

    
ZAZ
if hasattr(my_new_car, 'brand'):
    print(my_new_car.brand)
else:
    False

    
ZAZ
if hasattr(my_new_car, 'brd'):
    print(my_new_car.brand)
else:
    False

    
False
setattr
<built-in function setattr>
setattr(my_new_car, 'bra', 1234)
my_new_car.__dict__
{'brand': 'ZAZ', 'volume': 1.2, 'bra': 1234}
my_new_car.brand="asdgfstdhg"
my_new_car.hello=999
my_new_car.__dict__
{'brand': 'asdgfstdhg', 'volume': 1.2, 'bra': 1234, 'hello': 999}



class Animal:
    def eat(self):
        pass
    def go(self):def sleep(self):
        
SyntaxError: invalid syntax
class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f"животное {self.color} ест.....")
    def go(self):
        print('животное двигается.....')
    def sleep(self):
        print('Zzzzzz...')

        
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)

        
cat = DomesticCat("Dima", "black", 0)
cat=DomesticCat("Dima", "black", 0)
cat.color
'black'
cat.name
'Dima'
cat.age
0
cat.eat
<bound method Animal.eat of <__main__.DomesticCat object at 0x101a68050>>
cat.eat()
животное black ест.....
cat.go
<bound method Animal.go of <__main__.DomesticCat object at 0x101a68050>>
cat.go()
животное двигается.....

class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f"животное {self.color} ест.....")
    def go(self):
        print('животное двигается.....')
    def sleep(self):
        print('Zzzzzz...')

        
class DomesticCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

cat2 = DomesticCat("Dima", "black", 0)
cat2
Cat Name:Dima
	Age:0
	Color:black

        
Animal
<class '__main__.Animal'>
DomesticCat
<class '__main__.DomesticCat'>
cat = DomesticCat("Dim","black",0)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    cat = DomesticCat("Dim","black",0)
  File "<pyshell#115>", line 4, in __init__
    super().__init__(color,age)
TypeError: object.__init__() takes exactly one argument (the instance to initialize)
class Animal:
    def __init(self,color,age):
        self.color=color
        self.age=age
    def eat(self):
        print(f"животное {self.color} ест.....")
    def go(self):
        print('животное двигается.....')
    def sleep(self):
        print('Zzzzzz...')

        
class Animal:
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def eat(self):
        print(f"животное {self.color} ест.....")
    def go(self):
        print('животное двигается.....')
    def sleep(self):
        print('Zzzzzz...')

        
'
class DomesticCat(Animal):
    def __init__(self,name,color,age):
        self.name=name
        super().__init__(color,age)

        
cat = DomesticCat("Dim","black",0)
cat
<__main__.DomesticCat object at 0x100f56cf0>
cat.eat
<bound method Animal.eat of <__main__.DomesticCat object at 0x100f56cf0>>
cat.eat()
животное black ест.....
cat.go()
животное двигается.....
cat.sleep()
Zzzzzz...
class Animal:
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def eat(self):
        print(f"животное {self.color} ест.....")
    def go(self):
        print('животное двигается.....')
    def sleep(self):
        print('Zzzzzz...')

        
class DomesticCat(Animal):
    def __init__(self,name,color,age):
        self.name=name
        super().__init__(color,age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = DomesticCat("Dima","black",0)
cat
Cat Name:Dima
	Age:0
	Color:black
class DomesticCat(Animal):
    counter=123
    def __init__(self,name,color,age):
        self.name=name
        self.id=DomesticCat.counter
        DomesticCat.counter+=1
        super().__init__(color,age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = DomesticCat("Dima","black",0)
cat.id
123
vat.id=123324
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    vat.id=123324
NameError: name 'vat' is not defined. Did you mean: 'cat'?
cat.id=2341345
cat.id
2341345
class DomesticCat(Animal):
    counter=123
    def __init__(self,name,color,age):
        self.name=name
        self.id_=DomesticCat.counter
        DomesticCat.counter+=1
        super().__init__(color,age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = DomesticCat("Dima","black",0)
cat.id
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    cat.id
AttributeError: 'DomesticCat' object has no attribute 'id'. Did you mean: 'id_'?
cat.id_
123
cat.id_=13436
cat.__dict__
{'name': 'Dima', 'id_': 13436, 'color': 'black', 'age': 0}
class DomesticCat(Animal):
    counter=123
    def __init__(self,name,color,age):
        self.name=name
        self.__id=DomesticCat.counter
        DomesticCat.counter+=1
        super().__init__(color,age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = DomesticCat("Dima","black",0)
cat.__id
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    cat.__id
AttributeError: 'DomesticCat' object has no attribute '__id'
cat.__dict__
{'name': 'Dima', '_DomesticCat__id': 123, 'color': 'black', 'age': 0}
cat._DomesticCat__id
123
cat._DomesticCat__id=3452
cat._DomesticCat__id
3452





stack=[]
def push(value):
    stack.append(value)

    
def pop():
    stack.pop()

    
push(1)
push(2)
push(3)
push(4)
stack
[1, 2, 3, 4]
pop()
stack
[1, 2, 3]
pop()
stack
[1, 2]
pop()
stack
[1]


class Stack:
    pass

class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()

        
s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.stack
[1, 2, 3]
s2=Stack()
s2.stack
[]
s1.pop
<bound method Stack.pop of <__main__.Stack object at 0x100f56900>>
s1.pop()
s1.stack
[1, 2]

class Stack:
    def __init__(self):
        self.__stack=[]
    def push(self,value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    
s1=Stack()
s1.pop()
'NE OK'
s1.push(123)
s1.push(1)
s1.push(3)
s1.push(2)
s1.show()
[123, 1, 3, 2]
s1.pop()
'OK'
s1.show()
[123, 1, 3]

class Stack:
    def __init__(self):
        self.__stack=[]
    def push(self,value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    
class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter=0
        self.summa=0
    def push(self,value):
        self.counter+=1
        self.summa+=value
        super().push(value)

        
s1=CountingStack()
s1.show
<bound method Stack.show of <__main__.CountingStack object at 0x100f56900>>
s1.show()
[]
s1.pop()
'NE OK'
s1.stack
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    s1.stack
AttributeError: 'CountingStack' object has no attribute 'stack'








a=10
b=11
a+b
21
a.__add__(b)
21
a-b
-1
a.__sub__(b)
-1
a/b
0.9090909090909091
help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(self, /)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(self, /)
 |      Flooring an Integral returns itself.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __round__(self, ndigits=<unrepresentable>, /)
 |      Rounding an Integral returns itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(self, /)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is equal to the original int.
 |
 |      The ratio is in lowest terms and has a positive denominator.
 |
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(self, /)
 |      Returns self, the complex conjugate of any int.
 |
 |  is_integer(self, /)
 |      Returns True. Exists for duck type compatibility with float.is_integer.
 |
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_bytes(bytes, byteorder='big', *, signed=False)
 |      Return the integer represented by the given array of bytes.
 |
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        sys.byteorder as the byte order value.  Default is to use 'big'.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  denominator
 |      the denominator of a rational number in lowest terms
 |
 |  imag
 |      the imaginary part of a complex number
 |
 |  numerator
 |      the numerator of a rational number in lowest terms
 |
 |  real
 |      the real part of a complex number

a.__truediv__(b)
0.9090909090909091
s='lhfgkuyyg'
s1='kuyf'
s+s1
'lhfgkuyygkuyf'
s.__add__(s1)
'lhfgkuyygkuyf'
help(string)
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    help(string)
NameError: name 'string' is not defined. Did you forget to import 'string'?
help(str)

's' in s
False
'l' in s
True
s.__contains__('l')
True
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self,nextcat):
        return self.age+nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __it__(self,nextcat):
        return self.age<next.cat.age

    
c=Cat('Cat',5)
c2=Cat('Senya',6)
c+c2
11
len(c)
5
len(c2)
6
c<c2
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    c<c2
TypeError: '<' not supported between instances of 'Cat' and 'Cat'
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self,nextcat):
        return self.age+nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __it__(self,nextcat):
        return self.age<nextcat.age

    
c<c2
Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    c<c2
TypeError: '<' not supported between instances of 'Cat' and 'Cat'
c=Cat('Cat',5)
c2=Cat('Senya',6)
c<c2
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    c<c2
TypeError: '<' not supported between instances of 'Cat' and 'Cat'
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self,nextcat):
        return self.age+nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self,nextcat):
        return self.age<nextcat.age

    
c=Cat('Cat',5)
c2=Cat('Senya',6)
c<c2
True
c>c2
False
'a' in c
True
'd' in c
False
c
<__main__.Cat object at 0x100f56900>



class Wallet:
    def __init__(self, amount):
        self.amount=amount
    def __add__(self,int_value):
        return self.amount+int_value
    def __sub__(self,int_value):
        return self.amount-int_value
    def __len__(self):
        return self.amount

    
my_wallet=Wallet(1000)
my_wallet+100
1100
len(my_wallet)
1000
class Wallet:
    def __init__(self, amount):
        self.amount=amount
    def __add__(self,int_value):
        return self.amount+=int_value
    def __sub__(self,int_value):
        return self.amount-=int_value
    def __len__(self):
        return self.amount
    
SyntaxError: invalid syntax

class Wallet:
    def __init__(self, amount):
        self.amount=amount
    def __add__(self,int_value):
        return self.amount += int_value
...     def __sub__(self,int_value):
...         return self.amount -= int_value
...     def __len__(self):
...         return self.amount
...     
SyntaxError: invalid syntax
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount=amount
...     def __add__(self,int_value):
...         return self.amount += int_value
...     def __sub__(self,int_value):
...         return self.amount -= int_value
...     def __len__(self):
...         return self.amount
...     
SyntaxError: invalid syntax
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount=amount
...     def __add__(self,int_value):
...         self.amount += int_value
...         return self.amount
...     def __sub__(self,int_value):
...         self.amount -= int_value
...         return self.amount
...     def __len__(self):
...         return self.amount
... 
...     
>>> my_wallet=Wallet(1000)
>>> my_wallet+100
1100
>>> len(my_wallet)
1100
>>> my_wallet-50
1050
>>> len(my_wallet)
1050
