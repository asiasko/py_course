Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a,b=1,2
a
1
b
2
a==b
False
a!=b
True
a>b
False
a
1
b
2
a<b
True
a<=b
True
a,b=9,9
a==b
True
a!=b
False
a>=b
True
a<=b
True
res=a!=b
res
False
type(res)
<class 'bool'>

a
9
b
9
a>b
False
a>=b
True

password=input("/login:")
/login:12345
if password=="12345":
    print("ok")

    
ok
password=input("/login:")
/login:123
secret="123"
if password==secret:
    print("ok")

    
ok
password=input("/login:")
/login:333
if password==secret:
    print("ok")

    
if password==secret:
    print("ok")
else:
    print("wrong pass")

    
wrong pass
else:
    print("wrong pass")
    
SyntaxError: invalid syntax
secret="123"
secret1="bond*"
if password==secret:
    print("ok")
elif password==secret1:
    print("spy ok")

    
secret="123"
secret1="bond*"
if password==secret:
    print("ok")
elif password==secret1:
    print("spy ok")
    
SyntaxError: multiple statements found while compiling a single statement
if password==secret:
    print("ok")
elif password==secret1:
    print("spy ok")
else:
    print(-1)

    
-1
if True:
    print("ok")
elif True:
    print("-1 ok")

    
ok
if True:
    print("ok")
elif False:
    print("-1 ok")

    
ok
if False:
    print("ok")
elif True:
    print("-1 ok")

    
-1 ok

amount=900
if amount<1000:
    discount=amount*0.05
elif amount<5000:
    discount=amount*0.1
else:
    discount=amount*0.15

    
print("Discount is:", discount)
Discount is: 45.0
print("Net payable:", amount-discount)
Net payable: 855.0

secret="123"
secret1="bond*"

password=input("/login:") # 123
/login:123
if password==secret:
    print("ok")
elif password=secret1:
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if password==secret:
    print("ok")
elif password==secret1:
    print("spy ok")
else:
    print(-1)

    
ok
print("hahah")
hahah

a=123
if a==123:
    res=True
else:
    res=False

    
res
True

res=True if a==123 else False
res
True
res=a==123
res="XXX" if a==123 else "YYY"
res
'XXX'
password="123"
secret
'123'
secret1
'bond*'
if password==secret:
    print("ok")
elif password==secret1:
    print("spy ok")
else:
    print(-1)

    
ok
match password:
    case secret:
        print("ok")
    case secret1:
        print("spy ok")
        
SyntaxError: name capture 'secret' makes remaining patterns unreachable
match password:
    case '123':
        print("ok")
    case 'bond*':
        print("spy ok")
    case _:
        print(-1)

        
ok

counter=1
while counter<10:
    print(counter)
    counter+=2

    
1
3
5
7
9
counter
11
counter=1
while counter<10:
    print(counter)
    
SyntaxError: multiple statements found while compiling a single statement

counter=1
while counter<10:
    print(counter)

    
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1Traceback (most recent call last):
  File "<pyshell#128>", line 2, in <module>
    print(counter)
KeyboardInterrupt

counter=1
while counter<10:
    print(counter)
    if counter==5;
    
SyntaxError: invalid syntax
while counter<10:
    print(counter)
    if counter==5:
        print("exit")
        break
    counter+=2

    
1
3
5
exit
break
SyntaxError: 'break' outside loop
counter=1
while counter<10:
    counter+=2 
    if counter==5:
        print("go")
        continue
    print(counter)

    
3
go
7
9
11

for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(1,6,2):
    print(i)

    
1
3
5
for i in range(3,6):
    print(i)

    
3
4
5
import time
time.sleep(3)
for i in range(6):
    print("sleep ",i)
    time.sleep(1)

    
sleep  0
sleep  1
sleep  2
sleep  3
sleep  4
sleep  5

st="hello 1234"
to_find="2"
to_find in st
True
to_find="0"
to_find in st
False
if to_find in st:
    print("0 in st")
else:
    print("nope")

    
nope
to_find="23"
if to_find in st:
    print("0 in st")
else:
    print("nope")

    
0 in st
if to_find not in st:
    print("0 in st")
else:
    print("nope")

    
nope
noPrint="sdlghgerfv"
word=input("daj mne slova")
daj mne slova lsdfjwghoijvdsadfgry
word
' lsdfjwghoijvdsadfgry'
for char in word:
    print(char)

    
 
l
s
d
f
j
w
g
h
o
i
j
v
d
s
a
d
f
g
r
y
for char in word:
    if char in noPrint:
        continue
    print(char)

    
 
j
w
o
i
j
a
y
for char in word:
    if char not in noPrint:
        continue
    print(char)

    
l
s
d
f
g
h
v
d
s
d
f
g
r
for char in word:
    if char not in noPrint:
        continue
    print(char)
else:
    print("success...")

    
l
s
d
f
g
h
v
d
s
d
f
g
r
success...
age=21
money=1000
if age>18 and money>900:
    print("GRIND")

    
GRIND
age=16
money=1000
if age>18 and money>900:
    print("GRIND")
    
SyntaxError: multiple statements found while compiling a single statement
age=16
money=1000
if age>18 and money>900:
    print("GRIND")
    
SyntaxError: multiple statements found while compiling a single statement
if age>18 and money>900:
    print("GRIND")

    

True and True and True and False
False
age=17
if age>18 or money>900:
    print("GRIND")

    
GRIND
money=-1
if age>18 or money>900:
    print("GRIND")

    
>>> False or False or False
False
>>> False or False or True
True
>>> True
True
>>> not True
False
>>> age>10
True
>>> not age>10
False
>>> False
False
>>> not False
True
>>> not not not False
True
>>> 
>>> 60
60
>>> number=int("1010101110",2)
>>> number
686
>>> number2=int("1110100011",2)
>>> number2
931
>>> number=int("1010101110",2)
>>> number2=int("1110100011",2)
>>> bin(number)
'0b1010101110'
>>> bin(number2)
'0b1110100011'
>>> bin(number & number2)
'0b1010100010'
>>> bin(number | number2)
'0b1110101111'
>>> bin(number ^ number2)
'0b100001101'
