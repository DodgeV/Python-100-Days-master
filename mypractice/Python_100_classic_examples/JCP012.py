'''
【程序12】
题目：判断1-100之间有多少个素数，并输出所有素数及其和。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.程序源代码：
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
        print('这是第%d个素数'%h)
    leap = 1

print("the sum of all prime numbers is %d" % sum)
print('There are %d prime numbers in total' % h)