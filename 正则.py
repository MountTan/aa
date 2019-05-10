import re

a1 = re.match(r'python', 'Programing Python,should pythonic')
a2 = re.search(r'python', 'should be pythonic')

print(a2.group())
# print(a1.group())


rea = re.split('(Ch)', '1vy8rVDChtnxChaichan')
print(rea)
# ['1vy8rVD', 'Ch', 'tnx', 'Ch', 'aichan']

rea = re.split('Ch', '1vy8rVDChtnxChaichan')
print(rea)
# ['1vy8rVD', 'tnx', 'aichan']

# 注意小括号的作用


src = 'security/afafsff/?ip=123.4.56.78&id=45'
c = re.search(r'(\d.*)&', src)
print(c.group(1))









