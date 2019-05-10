class A():
    num = 1

    def __init__(self, num):
        self.num = num

    @classmethod
    def set_num(cls, num):
        cls.num = num

    @property
    def n(self):
        return self.num

    @staticmethod
    def alter_num(number):
        num = number


print(A.num)
a1 = A(5)
print(a1.n)
print(a1.num)
print(A.num)
a2 = A(6)
print(a2.n)
print(a2.num)
print(A.num)

a1.set_num(2)
print(a1.n)
print(a1.num)
print(A.num)









