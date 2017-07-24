class cl1:
    def __init__(self):            #类中的方法必须加参数self
        print('我的第一个类cl1')


class cl2:
    def __init__(self,name,job):
        print('My name is'+name+' My job is'+job)


class cl3:
    def __init__(self,name,job):
        self.myname = name
        self.myjob = job

class cl4:
    def myfunc1(self,name):
        print('hello  '+name)

class cl5:
    def __init__(self,name):
        self.myname = name
    def myfunc1(self):
        print('hello  '+self.myname)
