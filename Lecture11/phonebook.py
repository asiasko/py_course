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
Traceback (most recent call last):File "<pyshell#229>", line 1, in <module>
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
