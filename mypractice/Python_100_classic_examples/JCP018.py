'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。
1.程序分析：关键是计算出每一项的值。
2.程序源代码：
'''
from functools import reduce

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))

for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)

for i in Sn:
    if i == Sn[-1]:
        print('%d' % i,end = " ")
    else:
        print('%d + ' % i,end = ' ')

Sum = reduce(lambda x,y : x + y,Sn)
print('= %d' % Sum)
