Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
li=[]
li
[]
type(li)
<class 'list'>
tp=()
tp
()
type(tp)
<class 'tuple'>
tp2=tuple()
tp2
()
type(tp2)
<class 'tuple'>
num=2.
num
2.0
type(num)
<class 'float'>
num=2,
num
(2,)
type(num)
<class 'tuple'>
li=[12,33,44]
st='sdfd'
se=set(st)
se
{'f', 's', 'd'}
ss={12,23,4,534,5}
ss
{4, 5, 534, 23, 12}
t=(1,2,3,4,'sdf')
tt=1,2,3,4,4.,5435.345,'dfd'
tt
(1, 2, 3, 4, 4.0, 5435.345, 'dfd')
t=tuple()
t
()
t=tuple(ss)
t
(4, 5, 534, 23, 12)
tuple(1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(1)
TypeError: 'int' object is not iterable
t
(4, 5, 534, 23, 12)
isistance(t,tuple)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    isistance(t,tuple)
NameError: name 'isistance' is not defined. Did you mean: 'isinstance'?
isinstance(t,tuple)
True
isinstance(t,list)
False
isinstance(t,int)
False
t=1.
t=1.,
t=1.
t1=1.,
t2=1,
print(t,t1,t2)
1.0 (1.0,) (1,)
n=(1,2,3,4,5)
type(n)
<class 'tuple'>
n[0]
1
n[-1]
5
n[2]
3
n[1]=
SyntaxError: invalid syntax
liN=list(n)
liN[2]=333
liN
[1, 2, 333, 4, 5]
n
(1, 2, 3, 4, 5)
n=tuple(liN)
n=tuple(liN)
n
(1, 2, 333, 4, 5)
n=(1,2,3,[1,2,3,4])
n[3]
[1, 2, 3, 4]
n[3].append(666)
n
(1, 2, 3, [1, 2, 3, 4, 666])


t
1.0
t=(1,23,4)
t
(1, 23, 4)
a,b,c=t
a
1
b
23
c
4
li=[1,2,3,4]
a,b,c,d=li
a
1
b
2
c
3
d
4
li
[1, 2, 3, 4]
s='abc'
a,b,c=s
a
'a'
b
'b'
c
'c'
t=(1,2,3,4,5,6,7)
a,b,c=t
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a,b,c=t
ValueError: too many values to unpack (expected 3)
a,b,*c=t
a
1
b
2
c
[3, 4, 5, 6, 7]
type(c)
<class 'list'>
a,*b,c=t
a
1
b
[2, 3, 4, 5, 6]
c
7
*a,b,c=t
a
[1, 2, 3, 4, 5]
b
6
c
7
st='sdfghfh'
a,b,*c=st
c
['f', 'g', 'h', 'f', 'h']
a,*b,c=st
a
's'
b
['d', 'f', 'g', 'h', 'f']
c
'h'

def numbers():
    return 1,2,3,4,5
numbers()
SyntaxError: invalid syntax
def numbers():
    return 1,2,3,4,5

numbers()
(1, 2, 3, 4, 5)
a,*b=numbers()
a
1
b
[2, 3, 4, 5]
result=numbers()
result
(1, 2, 3, 4, 5)
def numbers():
    return 'error.....',1,2,3,4,5

numbers()
('error.....', 1, 2, 3, 4, 5)

err,*tp_n=numbers()
err
'error.....'
tp_n
[1, 2, 3, 4, 5]
if err=="'error....."
SyntaxError: expected ':'

if err=='error.....:
SyntaxError: unterminated string literal (detected at line 1)
if err=='error.....':
    print(123)

    
123
t
(1, 2, 3, 4, 5, 6, 7)
t(:)
SyntaxError: invalid syntax
t[:]
(1, 2, 3, 4, 5, 6, 7)
aaa=t
aaa[1]=99
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    aaa[1]=99
TypeError: 'tuple' object does not support item assignment
t
(1, 2, 3, 4, 5, 6, 7)
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:5]
(2, 3, 4, 5)
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:-1]
(2, 3, 4, 5, 6)
t[::2]
(1, 3, 5, 7)
t[::-2]
(7, 5, 3, 1)
t
(1, 2, 3, 4, 5, 6, 7)
t+=1
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    t+=1
TypeError: can only concatenate tuple (not "int") to tuple
t+=(1,)
t
(1, 2, 3, 4, 5, 6, 7, 1)
t+t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t
(1, 2, 3, 4, 5, 6, 7, 1)
t+6
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    t+6
TypeError: can only concatenate tuple (not "int") to tuple
t*6
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t*=4
t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
t
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
5 in t
True
9999 in t
False
6 in t
True
a
1
b
[2, 3, 4, 5]
c
'h'
b='sdfg'
a,b,c
(1, 'sdfg', 'h')
t=(1,23,4,a,b,c)
t
(1, 23, 4, 1, 'sdfg', 'h')
ordersId=(1,23,4,1,'asdf',23)
ordersId+=(len(ordersId)+1,)
ordersId
(1, 23, 4, 1, 'asdf', 23, 7)
ordersId+=(1,2,3,4,5,6,7)
ordersId+=(len(ordersId)+1,)
ordersId
(1, 23, 4, 1, 'asdf', 23, 7, 1, 2, 3, 4, 5, 6, 7, 15)

ordersId+=(len(ordersId)+1,)
ordersId
(1, 23, 4, 1, 'asdf', 23, 7, 1, 2, 3, 4, 5, 6, 7, 15, 16)
ordersId+=(len(ordersId)+1,)
ordersId+=(len(ordersId)+1,)
ordersId+=(len(ordersId)+1,)
ordersId+=(len(ordersId)+1,)
ordersId
(1, 23, 4, 1, 'asdf', 23, 7, 1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20)
ordersId+=len(ordersId)+1
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    ordersId+=len(ordersId)+1
TypeError: can only concatenate tuple (not "int") to tuple
ordersId
(1, 23, 4, 1, 'asdf', 23, 7, 1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20)
len(ordersId)
20
s
'abc'
len(s)
3
len(li)
4
li
[1, 2, 3, 4]
t=(1,2,3,4)
155
155
144
144
t[1:3]
(2, 3)
(155,)
(155,)
(144,)
(144,)
t=(155,)+t[1:3]+(144,)
t
(155, 2, 3, 144)
t.count(2)
1
t.count(8888)
0
t.index(1)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    t.index(1)
ValueError: tuple.index(x): x not in tuple
t.index(2)
1
t.index(144)
3
del t[0]
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
tp=(1,2,3,4,5)
for value in tp:
    print(value, end=' '))
    
SyntaxError: unmatched ')'
for value in tp:
    print(value, end=' ')
print()
SyntaxError: invalid syntax
for value in tp:
    print(value, end=' ')
    print()

    
1 
2 
3 
4 
5 
for index in range(len(tp)):
    print(index, '-->', tp[index])

    
0 --> 1
1 --> 2
2 --> 3
3 --> 4
4 --> 5
tp
(1, 2, 3, 4, 5)
t=(4,3,2,1)
for value in t:
    print(value)

    
4
3
2
1
for value in t:
    if value *2==4:
        continue
    print(value)

    
4
3
1
t
(4, 3, 2, 1)
n=len(t)
n
4
for i in range(n):
    print(i,', value:',t[i])

    
0 , value: 4
1 , value: 3
2 , value: 2
3 , value: 1
list vs tuple
SyntaxError: invalid syntax
'list vs tuple'
'list vs tuple'








di={}
type(di)
<class 'dict'>
di1=dict()
di1
{}
type(di1)
<class 'dict'>
se
{'f', 's', 'd'}
di
{}
hash
<built-in function hash>
a=3
b=4.
c='dsf'
li=[1,2,3]
se={3,2,5,6}
tp=(1,2,3,4)
hash(a)
3
hash(b)
4
hash(c)
-3107451879112492287
hash(tp)
590899387183067792
hash(se)
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    hash(se)
TypeError: unhashable type: 'set'
hash(li)
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    hash(li)
TypeError: unhashable type: 'list'
def a():
    pass

a
<function a at 0x1059954e0>
hash(a)
274306382
di
{}
hash(di)
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    hash(di)
TypeError: unhashable type: 'dict'
dd={1:'a', 2.:'dssd', 's':'sfdsdf',a:'func'}
dd
{1: 'a', 2.0: 'dssd', 's': 'sfdsdf', <function a at 0x1059954e0>: 'func'}
dd[1]
'a'
dd[111]
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    dd[111]
KeyError: 111
dd[2.]
'dssd'
dd[a]
'func'
dd['s']
'sfdsdf'
fs=frozenset([12,2,34,5,])
fs
frozenset({2, 5, 12, 34})
type(fs)
<class 'frozenset'>
hash(fs)
8453542846474786068
dd=dd={1:'a', 2.:'dssd', 's':'sfdsdf',a:'func', fs:'froz set'}
dd
{1: 'a', 2.0: 'dssd', 's': 'sfdsdf', <function a at 0x1059954e0>: 'func', frozenset({2, 5, 12, 34}): 'froz set'}
dd[fs]
'froz set'
for k,v in dd:
    print(k,v)

    
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    for k,v in dd:
TypeError: cannot unpack non-iterable int object
for v in dd.keys():
    print(v)

    
1
2.0
s
<function a at 0x1059954e0>
frozenset({2, 5, 12, 34})
for v in dd.items():
    print(v)

    
(1, 'a')
(2.0, 'dssd')
('s', 'sfdsdf')
(<function a at 0x1059954e0>, 'func')
(frozenset({2, 5, 12, 34}), 'froz set')
for k,v in dd.items():
    print(k, ':',v)

    
1 : a
2.0 : dssd
s : sfdsdf
<function a at 0x1059954e0> : func
frozenset({2, 5, 12, 34}) : froz set
for tp in dd.items():
    print(tp)

    
(1, 'a')
(2.0, 'dssd')
('s', 'sfdsdf')
(<function a at 0x1059954e0>, 'func')
(frozenset({2, 5, 12, 34}), 'froz set')
dd[1]
'a'
dd.get(1)
'a'
dd[1123]
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    dd[1123]
KeyError: 1123
dd.get(1123)
dd[-4]='sdffgghfd'
for tp in dd.items():
    print(tp)

    
(1, 'a')
(2.0, 'dssd')
('s', 'sfdsdf')
(<function a at 0x1059954e0>, 'func')
(frozenset({2, 5, 12, 34}), 'froz set')
(-4, 'sdffgghfd')
dd[0]=0
for tp in dd.items():
    print(tp)

    
(1, 'a')
(2.0, 'dssd')
('s', 'sfdsdf')
(<function a at 0x1059954e0>, 'func')
(frozenset({2, 5, 12, 34}), 'froz set')
(-4, 'sdffgghfd')
(0, 0)
dd.keys()
dict_keys([1, 2.0, 's', <function a at 0x1059954e0>, frozenset({2, 5, 12, 34}), -4, 0])
sorted(dd.keys())
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    sorted(dd.keys())
TypeError: '<' not supported between instances of 'str' and 'float'
dd[1]=12313
dd
{1: 12313, 2.0: 'dssd', 's': 'sfdsdf', <function a at 0x1059954e0>: 'func', frozenset({2, 5, 12, 34}): 'froz set', -4: 'sdffgghfd', 0: 0}
dd.update([55,'55555'])
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    dd.update([55,'55555'])
TypeError: cannot convert dictionary update sequence element #0 to a sequence
dd.update((55,'55555'))
Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    dd.update((55,'55555'))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
dd.update([55:'55555'])
SyntaxError: invalid syntax
dd.update({55:'55555'})
dd
{1: 12313, 2.0: 'dssd', 's': 'sfdsdf', <function a at 0x1059954e0>: 'func', frozenset({2, 5, 12, 34}): 'froz set', -4: 'sdffgghfd', 0: 0, 55: '55555'}
dd.update([(2,2222),(5,5555),(6,6666)])
dd
{1: 12313, 2.0: 2222, 's': 'sfdsdf', <function a at 0x1059954e0>: 'func', frozenset({2, 5, 12, 34}): 'froz set', -4: 'sdffgghfd', 0: 0, 55: '55555', 5: 5555, 6: 6666}
d=dict(name='jojo',age=8888)
d
{'name': 'jojo', 'age': 8888}
dd.update(gogogo='sdgghfdhr')
dd
{1: 12313, 2.0: 2222, 's': 'sfdsdf', <function a at 0x1059954e0>: 'func', frozenset({2, 5, 12, 34}): 'froz set', -4: 'sdffgghfd', 0: 0, 55: '55555', 5: 5555, 6: 6666, 'gogogo': 'sdgghfdhr'}
len(dd)
11
dd.pop(1)
12313
dd.popitem()
('gogogo', 'sdgghfdhr')
del dd('s')
SyntaxError: cannot delete function call
1 in dd
False
key=input()
dfg
dd
{2.0: 2222, 's': 'sfdsdf', <function a at 0x1059954e0>: 'func', frozenset({2, 5, 12, 34}): 'froz set', -4: 'sdffgghfd', 0: 0, 55: '55555', 5: 5555, 6: 6666}
if ff in dd:
    dd.pop(1)
else:
    print('nety')

    
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    if ff in dd:
NameError: name 'ff' is not defined. Did you mean: 'fs'?
if key in dd:
    dd.pop(key)
else:
    print('nety')

    
nety
key=2.0
if key in dd:
    dd.pop(key)
    print('OK')
... else:
...     print('nety')if key in dd:
...         dd.pop(key)
...     else:
...         print('nety')
...         
SyntaxError: invalid syntax
>>> if key in dd:
...         dd.pop(key)
...         print('OK')
...     else:
...         print('nety')
...         
SyntaxError: unindent does not match any outer indentation level
>>> if key in dd:
...     dd.pop(key)
...     print('OK')
... else:
...     print('nety')
... 
...     
2222
OK
>>> li=[]
>>> li.pop()
Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    li.pop()
IndexError: pop from empty list
>>> di=(i:i**3 for i in range(50,60))
SyntaxError: invalid syntax
>>> di={i:i**3 for i in range(50,60)}
>>> di
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
>>> type(di)
<class 'dict'>
