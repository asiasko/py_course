class Dog:
    inst_cont = False
    def __init__(self, name):
        if Dog.inst_cont == False:
            self.name = name
            Dog.inst_cont = True
        else:
            raise Exception("собака это синглтон")

        
Dog.inst_cont
False
d1 = Dog("Bobik")
d2 = Dog("Vasia")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d2 = Dog("Vasia")
  File "<pyshell#24>", line 8, in __init__
    raise Exception("собака это синглтон")
Exception: собака это синглтон