siasko@air-anastasiya ~ % python3 --version
Python 3.13.1
asiasko@air-anastasiya ~ % python3          
Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> print
<built-in function print>
>>> print()

>>> print("hello world")
hello world
>>> print(1+1)
2
>>> Print("hello world")
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    Print("hello world")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print 123)
  File "<python-input-0>", line 1
    print 123)
             ^
SyntaxError: unmatched ')'
>>> print("hello\world")
<python-input-1>:1: SyntaxWarning: invalid escape sequence '\w'
  print("hello\world")
hello\world
>>> print("hello\nworld")
hello
world
>>> print("hello\tworld")
hello	world
>>> print("hello")
hello
>>> print('hello')
hello
>>> print('hello")
  File "<python-input-6>", line 1
    print('hello")
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print('hello "world"')
hello "world"
>>> print('hello "world" , "123" , "ads"')
hello "world" , "123" , "ads"
>>> print("world" , "123" , "ads")
world 123 ads
>>> print(1, 2, 3, 4, sep="***")
1***2***3***4
>>> print(1, 2, 3, 4, sep="   ")
1   2   3   4
>>> print()

>>> print(end=\n\n\n)
  File "<python-input-13>", line 1
    print(end=\n\n\n)
               ^
SyntaxError: unexpected character after line continuation character
>>> print(end="\n\n\n")



>>> print(1, 2, 3, 4, "wrld", sep="+   +")
1+   +2+   +3+   +4+   +wrld
>>> print(1, 2, 3, 4, "wrld", sep="+   +", end="***")
1+   +2+   +3+   +4+   +wrld***>>> 
>>> print(1, 2, 3, 4, "wrld", sep="+   +", end="***")programming or an experien\
ced developer
  File "<python-input-18>", line 1
    print(1, 2, 3, 4, "wrld", sep="+   +", end="***")programming or an experienced developer
                                                     ^^^^^^^^^^^
SyntaxError: invalid syntax
>>> print("Programming", "Essentials", "in", sep="***", end="...Python")
Programming***Essentials***in...Python>>> 
>>> print(1, 2, 3, 4, "wrld", sep="+   +", end="***")
1+   +2+   +3+   +4+   +wrld***>>> 
>>> print(2,3)
2 3
>>> print(2.3)
2.3
>>> print("""
... 1+1
... "1+1"
... ""1+1""
... asdasd""")

1+1
"1+1"
""1+1""
asdasd
>>> print(True>False)
True
>>> print(True)
True
>>> print(true)
Traceback (most recent call last):
  File "<python-input-37>", line 1, in <module>
    print(true)
          ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(1)
<class 'int'>
>>> type(1.7)
<class 'float'>
>>> print("""
... "I'm"\n""Learning""\n"""Python""")
... 
... 
... 
... 
  File "<python-input-40>", line 2
    "I'm"\n""Learning""\n"""Python""")
                                  ^
SyntaxError: unterminated triple-quoted string literal (detected at line 5)
>>> print("""
... "I'm"\n""Learning""\n"""Python"""")
... 1
... 
  File "<python-input-41>", line 2
    "I'm"\n""Learning""\n"""Python"""")
                                  ^
SyntaxError: unterminated triple-quoted string literal (detected at line 3)
>>> 
>>> 1cat=77
  File "<python-input-43>", line 1
    1cat=77
    ^
SyntaxError: invalid decimal literal
>>> 22222as=99
  File "<python-input-44>", line 1
    22222as=99
        ^
SyntaxError: invalid decimal literal
>>> my dog=100
  File "<python-input-45>", line 1
    my dog=100
       ^^^
SyntaxError: invalid syntax
>>> dog="Dog"
>>> dog
'Dog'
>>> dog=90
>>> dog
90
>>> type(dog)
<class 'int'>
>>> y=3
>>> y
3
>>> y+=5
>>> y
8
>>> 3*(8/9)+6
8.666666666666666
>>> 8/9
0.8888888888888888
>>> john,mary,adam=3,5,7
>>> total_apples=john+mary+adam
>>> total_apples
15
>>> john,mary,adam=3,5,7
>>> total_apples=john+mary+adam
>>> print(total_apples)
15
>>> 

>>> print 123)
  File "<python-input-0>", line 1
    print 123)
             ^
SyntaxError: unmatched ')'
>>> print("hello\world")
<python-input-1>:1: SyntaxWarning: invalid escape sequence '\w'
  print("hello\world")
hello\world
>>> print("hello\nworld")
hello
world
>>> print("hello\tworld")
hello	world
>>> print("hello")
hello
>>> print('hello')
hello
>>> print('hello")
  File "<python-input-6>", line 1
    print('hello")
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print('hello "world"')
hello "world"
>>> print('hello "world" , "123" , "ads"')
hello "world" , "123" , "ads"
>>> print("world" , "123" , "ads")
world 123 ads
>>> print(1, 2, 3, 4, sep="***")
1***2***3***4
>>> print(1, 2, 3, 4, sep="   ")
1   2   3   4
>>> print()

>>> print(end=\n\n\n)
  File "<python-input-13>", line 1
    print(end=\n\n\n)
               ^
SyntaxError: unexpected character after line continuation character
>>> print(end="\n\n\n")



>>> print(1, 2, 3, 4, "wrld", sep="+   +")
1+   +2+   +3+   +4+   +wrld
>>> print(1, 2, 3, 4, "wrld", sep="+   +", end="***")
1+   +2+   +3+   +4+   +wrld***>>> 
                                                    ^^^^^^^^^^^
>>> print("Programming", "Essentials",\
... 
...  "in", sep="***", end="...Python")
... Programming***Essentials***in...Python>>>
... 
  File "<python-input-28>", line 4
    Programming***Essentials***in...Python>>>
                 ^
SyntaxError: invalid syntax
>>> 
>>> print(1, 2, 3, 4, "wrld", sep="+   +", end="***")
1+   +2+   +3+   +4+   +wrld***>>> 
>>> print(2,3)
2 3
>>> print(2.3)
2.3
>>> print("""
... 1+1
... "1+1"
... ""1+1""
... asdasd""")

1+1
"1+1"
""1+1""
asdasd
>>> print(True>False)
True
>>> print(True)
True
>>> print(true)
Traceback (most recent call last):
  File "<python-input-37>", line 1, in <module>
    print(true)
          ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(1)
<class 'int'>
>>> type(1.7)
<class 'float'>
>>> print("""
... "I'm"\n""Learning""\n"""Python""")
... 
... 
... 
... 
  File "<python-input-40>", line 2
    "I'm"\n""Learning""\n"""Python""")
                                  ^
SyntaxError: unterminated triple-quoted string literal (detected at line 5)
>>> print("""
... "I'm"\n""Learning""\n"""Python"""")
... 1
... 
  File "<python-input-41>", line 2
    "I'm"\n""Learning""\n"""Python"""")
                                  ^
SyntaxError: unterminated triple-quoted string literal (detected at line 3)
>>> 
>>> 1cat=77
  File "<python-input-43>", line 1
    1cat=77
    ^
SyntaxError: invalid decimal literal
>>> 22222as=99
  File "<python-input-44>", line 1
    22222as=99
        ^
SyntaxError: invalid decimal literal
>>> my dog=100
  File "<python-input-45>", line 1
    my dog=100
       ^^^
SyntaxError: invalid syntax
>>> dog="Dog"
>>> dog
'Dog'
>>> dog=90
>>> dog
90
>>> type(dog)
<class 'int'>
>>> y=3
>>> y
3
>>> y+=5
>>> y
8
>>> 3*(8/9)+6
8.666666666666666
>>> 8/9
0.8888888888888888
>>> john,mary,adam=3,5,7
>>> total_apples=john+mary+adam
>>> total_apples
15
>>> john,mary,adam=3,5,7
>>> total_apples=john+mary+adam
>>> print(total_apples)
15
>>> 
