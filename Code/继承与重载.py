#继承与重载
#某一个家庭父亲、母亲、儿子、女儿

class Father():
    def speak(self):
        print('I can speak!')

#单继承
class Son1(Father):
    pass

#母亲类
class Mother():
    def write(self):
        print('I can write!')

#女儿类
class Daughter(Father,Mother):
    def listen(self):
        print('I can listen!')

#重写
class Son2(Father):
    def speak(self):
        print('I can speak 2!')
