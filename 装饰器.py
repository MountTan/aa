"""
输出下面的打印结果
"""


def decorate(func):
    print('func')

    def inner(**kwargs):
        kwargs.update(a='b')
        print(kwargs)
        result = func(**kwargs)
        return result

    print('inner')
    return inner


@decorate
def test(**kwargs):
    return kwargs

test()

#####################################
"""
func
inner       # 将装饰器装饰在 test（）的时候，decorate（）就执行了
{'a': 'b'}  # 当调用test()时， inner才会执行
"""
