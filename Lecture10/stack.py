

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
print(s1.show())
[]
print(s1.pop())
NE OK
print(s1.counter)
0
print(s1.summa)
0
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
print(s1.show())
[1, 2, 3, 4]
print(s1.counter)
4
print(s1.summa)
10
print(s1.pop())
OK
print(s1.pop())
OK
print(s1.pop())
OK
print(s1.pop())
OK
print(s1.pop())
NE OK