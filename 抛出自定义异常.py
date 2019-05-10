"""
使用python 语言编写一个方法getSquareSum,参数为n,
返回:1**2 + 2**2 + 3**2 + ... + n**2 的和（注：n必须为正整数，需对n进行判断，不满足抛出异常）
"""

class NumTypeError(Exception):
    def __str__(self):
        return '不符合要求'


def getSquareSum():

    n = input('请输入一个正整数:')
    try:
        if not n.isdigit() or int(n) < 0:
            raise NumTypeError()
    except Exception as e:
        print(e)
    else:
        n = int(n)
        res = 0
        for num in range(1, n + 1):
            res += num ** 2
        print(res)


if __name__ == '__main__':
    getSquareSum()

