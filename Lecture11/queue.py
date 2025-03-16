class EmptyQueueError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"EmptyQueueError: message: {self.message}"

    
class Queue:
    def __init__(self):
        self.__queue = []
    def get(self):
        if len(self.__queue) < 1:
            raise EmptyQueueError("Очередь пустая")
        return self.__queue.pop(0)
    def put(self, value):
        self.__queue.append(value)

        
q1 = Queue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
q1.get()
1
q1.get()
2
q1.get()
3
q1.get()
4
q1.get()
5
q1.get()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    q1.get()
  File "<pyshell#15>", line 6, in get
    raise EmptyQueueError("Очередь пустая")
EmptyQueueError: EmptyQueueError: message: Очередь пустая
