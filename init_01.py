#__init__ 其实就是python的构造方法
#类似于init()这种初始化方法，来初始化创建对象的状态


class FooBar:
    def __init__(self):
        self.somevar=42


f=FooBar()
f.somevar
