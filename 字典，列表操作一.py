a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {**a, **b}
print(c)
d = a.copy()
d.update(b)
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

f = [1, 2]
g = [3, 4]
h = f + g
print(h)  # [1, 2, 3, 4]

i = ['a', 'b', 'c']
j = [1, 2]

k = [1, 2, 3]
l = [item * 2 for item in k]
print(l)  # [2, 4, 6]

m = ['a', 'b', 'c']
n = [1, 2]
o = zip(m, n)
print(list(o))  # [('a', 1), ('b', 2)]
