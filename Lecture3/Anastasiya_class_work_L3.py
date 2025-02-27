Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
li=[]
print(li)
[]
li1=list()
print(li1)
[]
a=[1,2,3,True,'qwe']
a
[1, 2, 3, True, 'qwe']
a[3]
True
a[4]
'qwe'
a["1"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a["1"]
TypeError: list indices must be integers or slices, not str
a[5]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[5]
IndexError: list index out of range
type(li)
<class 'list'>
type(a)
<class 'list'>
a
[1, 2, 3, True, 'qwe']
a[0]
1
type(a[0])
<class 'int'>
print(1,2.3,True,"fg",a)
1 2.3 True fg [1, 2, 3, True, 'qwe']
st="Hello"
st.upper()
'HELLO'
st
'Hello'
q=100
q.upper()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    q.upper()
AttributeError: 'int' object has no attribute 'upper'


a=[4,3,45,6,7,8,93]
a
[4, 3, 45, 6, 7, 8, 93]
a.append(777)
a
[4, 3, 45, 6, 7, 8, 93, 777]
a.insert(2,9)
a
[4, 3, 9, 45, 6, 7, 8, 93, 777]
a.insert(3,5)
a
[4, 3, 9, 5, 45, 6, 7, 8, 93, 777]
len(a)
10
a.insert(2,3)
a
[4, 3, 3, 9, 5, 45, 6, 7, 8, 93, 777]
a.reverse()
a
[777, 93, 8, 7, 6, 45, 5, 9, 3, 3, 4]
a.reverse()
a
[4, 3, 3, 9, 5, 45, 6, 7, 8, 93, 777]
a.pop()
777
a.pop(3)
9
res=a.pop(3)
a
[4, 3, 3, 45, 6, 7, 8, 93]
res
5
del a[0]
a
[3, 3, 45, 6, 7, 8, 93]
del li
li
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    li
NameError: name 'li' is not defined. Did you mean: 'li1'?
a
[3, 3, 45, 6, 7, 8, 93]
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
a.remove(8)
a
[3, 3, 45, 6, 7, 93]
a.pop(88)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.pop(88)
IndexError: pop index out of range
toDel=555
if toDel in a:
    a.remove(toDel)

    
a.count(6)
1
a
[3, 3, 45, 6, 7, 93]
a.append(6)
a.count(6)
2
a.count(777)
0
a
[3, 3, 45, 6, 7, 93, 6]
a.clear()
a
[]
a.index(6)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.index(6)
ValueError: 6 is not in list
a=[3,9,45,6,7,93,6]
a.index(6)
3
a.index(6,a.index(6)+1)
6
a
[3, 9, 45, 6, 7, 93, 6]
li=[7,7,7]
a+=li
a
[3, 9, 45, 6, 7, 93, 6, 7, 7, 7]
a*=2
a
[3, 9, 45, 6, 7, 93, 6, 7, 7, 7, 3, 9, 45, 6, 7, 93, 6, 7, 7, 7]
q=[1,3,5,7,2,4,6]
q
[1, 3, 5, 7, 2, 4, 6]
q[0]
1
q[6]
6
q[-1]
6
q[-2]
4
q[-7]
1
q
[1, 3, 5, 7, 2, 4, 6]
q[2]=555
q
[1, 3, 555, 7, 2, 4, 6]
q[3]=999
q
[1, 3, 555, 999, 2, 4, 6]


hat_list=[1,2,3,4,5]
len(hat_list)
5
a.insert(2,a=input("vvedite chislo:")
         1
         
SyntaxError: '(' was never closed
a.insert(2,a=input("vvedite chislo:"))
         
vvedite chislo:5
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.insert(2,a=input("vvedite chislo:"))
TypeError: list.insert() takes no keyword arguments
a.insert(2,input("vvedite chislo:"))
         
vvedite chislo:5
hat_list.insert(2,input("vvedite chislo:"))
         
vvedite chislo:5
hat_list
         
[1, 2, '5', 3, 4, 5]
hat_list.insert(2,str.input("vvedite chislo:"))
         
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    hat_list.insert(2,str.input("vvedite chislo:"))
AttributeError: type object 'str' has no attribute 'input'
hat_list.insert(2,str(input("vvedite chislo:")))
         
vvedite chislo:3
hat_list
         
[1, 2, '3', '5', 3, 4, 5]
hat_list.pop()
         
5
hat_list
         
[1, 2, '3', '5', 3, 4]
print("Dlina spiska: ",len(hat_list))
         
Dlina spiska:  6
hat_list=[1,2,3,4,5]
         
len(hat_list)
         
5
hat_list.insert(2,input("vvedite chislo:"))
         
vvedite chislo:5
print(hat_list)
         
[1, 2, '5', 3, 4, 5]
hat_list.pop()
         
5
print("Dlina spiska: ",len(hat_list))
         
Dlina spiska:  5
hat_list=int(insert(2,input("vvedite chislo:")))
         
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    hat_list=int(insert(2,input("vvedite chislo:")))
NameError: name 'insert' is not defined
hat_list
         
[1, 2, '5', 3, 4]
hat_list.insert(2,int(input("vvedite chislo:")))
         
vvedite chislo:5
hat_list
         
[1, 2, 5, '5', 3, 4]
q=[1,3,555,999,2]
         
li=[]
         
for i in range(int(input("n--->"))):
         li.append(int(input("n--->")))

         
n--->34
n--->23
n--->56y7
Traceback (most recent call last):
  File "<pyshell#121>", line 2, in <module>
    li.append(int(input("n--->")))
ValueError: invalid literal for int() with base 10: '56y7'

for i in range(int(input("n--->"))):
         li.append(int(input("n--->")))

         
n--->12
n--->234
n--->56
n--->34
n--->23
n--->1
n--->2
n--->exit()
Traceback (most recent call last):
  File "<pyshell#124>", line 2, in <module>
    li.append(int(input("n--->")))
ValueError: invalid literal for int() with base 10: 'exit()'

li
         
[23, 234, 56, 34, 23, 1, 2]
summa=0
         
for i in range(len(li)):
         summa+=li[i]

         
summa
         
373
summa=0
         
for val in li:
         summa+=val

         
summa
         
373
li
         
[23, 234, 56, 34, 23, 1, 2]
li.reverse()
         
li.append(1000)
         
li
         
[2, 1, 23, 34, 56, 234, 23, 1000]
print(li)
         
[2, 1, 23, 34, 56, 234, 23, 1000]
sorted(li)
         
[1, 2, 23, 23, 34, 56, 234, 1000]
li
         
[2, 1, 23, 34, 56, 234, 23, 1000]
for i in sorted(li):
         print(i,sep=" ")

         
1
2
23
23
34
56
234
1000
for i in sorted(li):
         print(i,end=" ")

         
1 2 23 23 34 56 234 1000 
li
         
[2, 1, 23, 34, 56, 234, 23, 1000]
sorted(li, reverse=True)
         
[1000, 234, 56, 34, 23, 23, 2, 1]
li
         
[2, 1, 23, 34, 56, 234, 23, 1000]


li=[3,5,0,-10,4]
         
a,b=66,77
         
tmp=a
         
a=b
         
b=tmp
         
a
         
77
b
         
66
a,b=66,77
         
a
         
66
b
         
77
a,b=b,a
         
a
         
77
b
         
66
li
         
[3, 5, 0, -10, 4]
li[1],li[2]=li[2],li[1]
         
li
         
[3, 0, 5, -10, 4]
li[2],li[3]=li[3],li[2]
         
li
         
[3, 0, -10, 5, 4]
li[3],li[4]=li[4],li[3]
         
li
         
[3, 0, -10, 4, 5]
li[1],li[2]=li[2],li[1]
         
li
         
[3, -10, 0, 4, 5]
li[0],li[1]=li[1],li[0]
         
li
         
[-10, 3, 0, 4, 5]
li[1],li[2]=li[2],li[1]
         
li
         
[-10, 0, 3, 4, 5]
li1=[8,10,6,2,4]
         
swapped=True
         
while swapped:
    swapped=False
    for index in range(len(li)-1):
        if li[index]>li[index+1]:
            swapped=True
            li[index], li[index+1]=li[index+1], li[index]

            
li
[-10, 0, 3, 4, 5]
li1=[8,10,6,2,4]
         
swapped=True
         
while swapped:
    swapped=False
    for index in range(len(li1)-1):
        if li1[index]>li1[index+1]:
            swapped=True
            li1[index], li1[index+1]=li1[index+1], li1[index]
            
SyntaxError: multiple statements found while compiling a single statement

swapped=True
         
while swapped:
    swapped=False
    for index in range(len(li1)-1):
        if li1[index]>li1[index+1]:
            swapped=True
            li1[index], li1[index+1]=li1[index+1], li1[index]
            
SyntaxError: multiple statements found while compiling a single statement
li
[-10, 0, 3, 4, 5]
max(li)
5
min(li)
-10
sum(li)
2
print
<built-in function print>
max
<built-in function max>


li=[1,2,3,4]
a=li
a
[1, 2, 3, 4]
li
[1, 2, 3, 4]
id(li)
4307533760
id(a)
4307533760
a[1]=99999
a
[1, 99999, 3, 4]
li
[1, 99999, 3, 4]
li=[1,2,3,4]
a=li.coppy()
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    a=li.coppy()
AttributeError: 'list' object has no attribute 'coppy'. Did you mean: 'copy'?
a=li.copy()
id(li)
4322595520
id(a)
4322597568
a[1]=5555
a
[1, 5555, 3, 4]
li
[1, 2, 3, 4]
a=li[:]
a
[1, 2, 3, 4]
li
[1, 2, 3, 4]
id(li)
4322595520
id(a)
4322756224
li[:]
[1, 2, 3, 4]
li[:3]
[1, 2, 3]
li[1:]
[2, 3, 4]
li
[1, 2, 3, 4]
li+=li
li
[1, 2, 3, 4, 1, 2, 3, 4]
kk=li[::2]
kk
[1, 3, 1, 3]
li
[1, 2, 3, 4, 1, 2, 3, 4]
li[::-1]
[4, 3, 2, 1, 4, 3, 2, 1]
77 in li
False


s={}
type(s)
<class 'dict'>
s=set()
type(s)
<class 'set'>
s={"df",1,2,3,1,1,2,3}
s
{1, 2, 3, 'df'}
s.add(1)
s
{1, 2, 3, 'df'}
for v is s:
    
SyntaxError: invalid syntax
for v in s:
    print(v, end=" ")

    
1 2 3 df 
999 in s
False
1 in s
True
s.update({1,2,3,4,6666})
s
{1, 2, 3, 4, 6666, 'df'}
s.clear()
s
set()
s={1, 2, 3, 4, 6666, 'df'}
s.remove(555)
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    s.remove(555)
KeyError: 555
s.remove(4)
s
{1, 2, 3, 'df', 6666}
s.discard(444)
s
{1, 2, 3, 'df', 6666}
s.discard(2)
len(s)
4
li
[1, 2, 3, 4, 1, 2, 3, 4]
li=list(set(li))
li
[1, 2, 3, 4]
type(li)
<class 'list'>
set(li)
{1, 2, 3, 4}
s
{1, 3, 'df', 6666}
list(s)
[1, 3, 'df', 6666]
st
'Hello'
list(st)
['H', 'e', 'l', 'l', 'o']
set(st)
{'l', 'e', 'H', 'o'}
li
[1, 2, 3, 4]
s
{1, 3, 'df', 6666}
st
'Hello'
int(li)
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    int(li)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
str(li)
'[1, 2, 3, 4]'
print(li)
[1, 2, 3, 4]
ppp=str(li)
li
[1, 2, 3, 4]
ppp
'[1, 2, 3, 4]'
list(ppp)
['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ']']


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
li=list(set(my_list))
li
[1, 2, 4, 6, 9]
[1, 2, 4, 6, 9]
[1, 2, 4, 6, 9]
my_list
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list=my_list.reverse()
new_list
new_list
new_list=reverse(my_list)
Traceback (most recent call last):
  File "<pyshell#292>", line 1, in <module>
    new_list=reverse(my_list)
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
new_list=reversed(my_list)
new_list
<list_reverseiterator object at 0x101a99a50>
my_list
[9, 2, 6, 2, 4, 1, 4, 4, 2, 1]


my_list[::-1]
[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]





li=[1,2,3,4,5]
resList=[]
for v in li:
    resList.append(v**2)

    
li
[1, 2, 3, 4, 5]
resList
[1, 4, 9, 16, 25]


li=[1,2,3,4,5]
resList=[v**2 for v in li]
resList
[1, 4, 9, 16, 25]


li=[1,2,3,4,5,6,7,8,9,10]
resList=[v**2 for v in li if v%2==0]
resList
[4, 16, 36, 64, 100]

li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


numbers=[int(input("---->")) for i in range(int(input("n--->")))]
n--->6
---->44
---->55
---->66
---->1
---->2
---->3
numbers
[44, 55, 66, 1, 2, 3]

number=[]
n=int(input("n--->"))
n--->6
for i in range (n):
    numbers.append(int(input("--->")))

    
--->5
--->5
--->5
--->5
--->5
--->5
numbers
[44, 55, 66, 1, 2, 3, 5, 5, 5, 5, 5, 5]
li=input("x x x x:--->")
x x x x:--->1 2 3 4
li
'1 2 3 4'
li=li.split()
li
['1', '2', '3', '4']
li=[int(v) for v in li]
li
[1, 2, 3, 4]
sum(li)
10
li=[int(v) for v in input("x x x x:--->").split()]
x x x x:--->5 6 7 8
li
[5, 6, 7, 8]
summa=sum([int(v) for v in input("x x x x:--->").split()])
x x x x:--->5 6 7 8
summa
26

li=[]
summa=0
numbersStr=input("x x x x:--->")
x x x x:--->3 4 5 6
numberStr
Traceback (most recent call last):
  File "<pyshell#349>", line 1, in <module>
    numberStr
NameError: name 'numberStr' is not defined. Did you mean: 'numbersStr'?
numbersStr
'3 4 5 6'
li=numbersStr.split()
li
['3', '4', '5', '6']
resList
[4, 16, 36, 64, 100]
resList=[]
for v in li:
    resList.append(int(v))

    
resList
[3, 4, 5, 6]
summa=sum(resList)
summa
18


li=[1,2,3,4]
li[0]
1
li[1]
2
>>> li=[[],[],[]]
>>> li[0]
[]
>>> li[2]
[]
>>> li=[[1,2,3],[11,22,33],[0,5,8]]
>>> li[0]
[1, 2, 3]
>>> li[1]
[11, 22, 33]
>>> li[2]
[0, 5, 8]
>>> li[0][2]
3
>>> li[1][1]
22
>>> li[2][1]
5
>>> li[2][0]
0
>>> li=[[1,2,3],[11,22,33],[0,5,8]]
>>> li[0].append(333)
>>> li
[[1, 2, 3, 333], [11, 22, 33], [0, 5, 8]]
>>> li[0][2]=222
>>> li
[[1, 2, 222, 333], [11, 22, 33], [0, 5, 8]]
>>> li=[[[1,2,3],[1,2,3]]]
>>> li
[[[1, 2, 3], [1, 2, 3]]]
>>> li[0][0]
[1, 2, 3]
>>> li[0][0][1]
2
>>> li[0][0].clear()
>>> li
[[[], [1, 2, 3]]]
