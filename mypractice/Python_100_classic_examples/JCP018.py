'''
��Ŀ����s=a+aa+aaa+aaaa+aa...a��ֵ������a��һ�����֡�����2+22+222+2222+22222(��ʱ
����������5�������)������������м��̿��ơ�
1.����������ؼ��Ǽ����ÿһ���ֵ��
2.����Դ���룺
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
