class Parent(object):
    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def p_test(self):
        pass


class Child(Parent):
    a = 4
    b = 5

    def __init__(self):
        super(Child, self).__init__()
        # self.a = 6
        # self.b = 7

    def c_test(self):
        pass

    def p_test(self):
        pass


p = Parent()
c = Child()
print(Parent.__dict__)
print(Child.__dict__)
print(p.__dict__)
print(c.__dict__)

####################################
"""
{'__module__': '__main__', 'a': 0, 'b': 1, '__init__': <function Parent.__init__ at 0x00000278830898C8>, 'p_test': <function Parent.p_test at 0x0000027883089950>, '__dict__': <attribute '__dict__' of 'Parent' objects>, '__weakref__': <attribute '__weakref__' of 'Parent' objects>, '__doc__': None}
{'__module__': '__main__', 'a': 4, 'b': 5, '__init__': <function Child.__init__ at 0x00000278830899D8>, 'c_test': <function Child.c_test at 0x0000027883089A60>, 'p_test': <function Child.p_test at 0x0000027883089AE8>, '__doc__': None}
{'a': 2, 'b': 3}
{'a': 6, 'b': 7}
"""
# 总结：
#
# 　　1） 内置的数据类型没有__dict__属性
#
# 　　2） 每个类有自己的__dict__属性，就算存着继承关系，父类的__dict__ 并不会影响子类的__dict__
#
# 　　3） 对象也有自己的__dict__属性， 存储self.xxx 信息，父子类对象公用__dict__





















