'''
������36��
��Ŀ����100֮�ڵ�����������
1.���������
2.����Դ���룺 
'''
from math import sqrt

h = 0
leap = 1
sum = 0

for m in range(2,101):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % m,end = "")
        sum += m
        h += 1
        print('���ǵ�%d������'%h)
    leap = 1

print("the sum of all prime numbers is %d" % sum)
print('There are %d prime numbers in total' % h)
