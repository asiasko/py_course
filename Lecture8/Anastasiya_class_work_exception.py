Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
a='asdfg'
a.capitalize()
'Asdfg'
a.decapitalize()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.decapitalize()
AttributeError: 'str' object has no attribute 'decapitalize'. Did you mean: 'capitalize'?
1/0
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
try:
    1/0
except:
    print(-1)

    
-1
try:
    li=[1,2,3]
    li[0.5]
except:
    print(-1)

    
-1
try:
    int('dssgfhgt34')
except:
    print(-1)

    
-1
int('dssgfhgt34')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int('dssgfhgt34')
ValueError: invalid literal for int() with base 10: 'dssgfhgt34'
try:
    1/0
except ValueError:
    print('ValueError')
except:
    print(-1)

    
-1
try:
    int('sdfsrdfgr342')
except ValueError:
    print('ValueError')
except:
    print(-1)

    
ValueError
try:
    1/0
except ZeroDivisionError:
    print('ZeroDivisionError x/0')
except ValueError:
    print('ValueError')
except:
    print(-1)

ZeroDivisionError x/0
try:
    int('@#dsgdf5467')
except ZeroDivisionError:
    print('ZeroDivisionError x/0')
except ValueError:
    print('ValueError')
except:
    print(-1)

    
ValueError
try:

    int('@#dsgdf5467')
except:
    print(-1)
except ZeroDivisionError:
    print('ZeroDivisionError x/0')
except ValueError:
    print('ValueError')
    
SyntaxError: default 'except:' must be last
try:
    li[0.5]
except ZeroDivisionError as zde.args:
    print('ZeroDivisionError x/0', zde.args)
except ValueError as ve.args:
    print('ValueError', ve.args)
except:
    print(-1)
    
SyntaxError: invalid syntax
try:
    li[0.5]
except ZeroDivisionError as zde:
    print('ZeroDivisionError x/0', zde.args)
except ValueError as ve:
    print('ValueError', ve.args)
except:
    print(-1)

    
-1
try:
    1/0
except ZeroDivisionError as zde:
    print('ZeroDivisionError x/0', zde.args)
except ValueError as ve:
    print('ValueError', ve.args)
except:
    print(-1)

    
ZeroDivisionError x/0 ('division by zero',)
try:
    raise ValueError('sdfarg')
except ZeroDivisionError as zde:
    print('ZeroDivisionError x/0', zde.args)
except ValueError as ve:
    print('ValueError', ve.args)
except:
    print(-1)

    
ValueError ('sdfarg',)
try:
    raise ZeroDivisionError
except ZeroDivisionError as zde:
    print('ZeroDivisionError x/0', zde.args)
except ValueError as ve:
    print('ValueError', ve.args)
except:
    print(-1)

    
ZeroDivisionError x/0 ()
raise IndexError
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    raise IndexError
IndexError
try:
    123/0
except (ValueError,ZeroDivisionError):
    print('ZeroDivisionError or ValueError')
except:
    print(-1)

    
ZeroDivisionError or ValueError
import elchupakabra
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    import elchupakabra
ModuleNotFoundError: No module named 'elchupakabra'
a=6
if a==8:
    try:
        import time
    except:
        pass
else:
    print('делай без time')

    
делай без time
time.sleep(12)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    time.sleep(12)
NameError: name 'time' is not defined. Did you forget to import 'time'?
a=8
if a==8:
    try:
        import time
    except:
        pass
else:
    print('делай без time')

    
time.sleep(12)




try:
    raise ZeroDivisionError  # 1/0
except:
    print('default')

    
default
try:
    raise ZeroDivisionError  # 1/0
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('default')

ZeroDivisionError
try:
    raise ZeroDivisionError  # 1/0
except ArithmeticError:
    print('ZeroDivisionError')
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('default')

    
ZeroDivisionError
print('ZeroDivisionError')
ZeroDivisionError

try:
    raise IndexError('[5] out of range')
except Exception as e:
    print(e.args)
except:
    print('default')

    
('[5] out of range',)
def a(x):
    try:
        res=int(x)
    except:
        print('123')

        
a(123)
a('sdgtrdthg53')
123
def a(x):
    try:
        res=int(x)
    except:
        print('123')
        raise

    
a(123)
a('asgffer')
123
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a('asgffer')
  File "<pyshell#107>", line 3, in a
    res=int(x)
ValueError: invalid literal for int() with base 10: 'asgffer'
def b(x):
    try:
        a(x)
    except:
        print(321)
        raise

    
b(234)
b('esdtres$')
123
321
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    b('esdtres$')
  File "<pyshell#116>", line 3, in b
    a(x)
  File "<pyshell#107>", line 3, in a
    res=int(x)
ValueError: invalid literal for int() with base 10: 'esdtres$'
assert 1
assert o
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    assert o
NameError: name 'o' is not defined
>>> assert ''
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    assert ''
AssertionError
>>> assert 'sd'
>>> assert[]
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    assert[]
AssertionError
>>> assert []
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    assert []
AssertionError
>>> assert [1,2,3]
>>> assert True
>>> assert False
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    assert False
AssertionError
>>> res=10
>>> assert res==10
>>> res=11
>>> 
>>> assert res==10
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    assert res==10
AssertionError
>>> assert (1,2,3)
>>> assert ()
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    assert ()
AssertionError
