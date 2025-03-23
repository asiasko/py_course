# наблюдатель observer
class Sub:
    def react(self, creator):
        print("Sub реагирует лайком на новое видео от:")
        print(creator)

        
class Creator:
    subs = []
    def follow(self, sub):
        Creator.subs.append(sub)
        print("подписчик успешно подписался")

        
class Creator:
    
    def __init__(self,name):
        self.subs = []
        self.name = name
    def __str__(self):
        return f"self.name"
    def follow(self, sub):
        Creator.subs.append(sub)
        print("подписчик успешно подписался")
    def notify_all(self):
        for sub in self.subs:
            sub.react(self)
    def create_event(self):
        print("произошло новое видео")
        self.notify_all()

        
chan_owner = Creator("MGH Channel")
chan_owner.subs
[]
chan_owner.name
'MGH Channel'
sub1 = Sub()
sub2 = Sub()
sub3 = Sub()
chan_owner.follow(sub1)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    chan_owner.follow(sub1)
  File "<pyshell#51>", line 9, in follow
    Creator.subs.append(sub)
AttributeError: type object 'Creator' has no attribute 'subs'
class Creator:
    
    def __init__(self,name):
        self.subs = []
        self.name = name
    def __str__(self):
        return f"self.name"
    def follow(self, sub):
        Creator.subs.append(sub)
        print("подписчик успешно подписался")
    def notify_all(self):
        for sub in self.subs:
            sub.react(self)
    def create_event(self):
        print("произошло новое видео")
        self.notify_all()

        
class Creator:
    
    def __init__(self,name):
        self.subs = []
        self.name = name
    def __str__(self):
        return f"{self.name}"
    def follow(self, sub):
        Creator.subs.append(sub)
        print("подписчик успешно подписался")
    def notify_all(self):
        for sub in self.subs:
            sub.react(self)
    def create_event(self):
        print("произошло новое видео")
        self.notify_all()

        
chan_owner = Creator("MGH Channel")
chan_owner.subs
[]
chan_owner.name
'MGH Channel'
sub1 = Sub()
sub2 = Sub()
sub3 = Sub()
chan_owner.follow(sub1)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    chan_owner.follow(sub1)

#переделать!!!!

