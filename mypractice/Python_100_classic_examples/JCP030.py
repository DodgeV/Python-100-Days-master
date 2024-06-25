'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　　　
1.程序分析：同29例
2.程序源代码：
'''
# 方法1
x = input("input a number:")


for i in range(int(len(x)/2)):
    if x[i] != x[-i - 1]:
        print('this number is not a huiwen')
        x = None
        break
if x:
    print('this number is a huiwen')

# 方法2
x = input("input a number:")
d = x[::-1]

# x = list(input('input a number:'))
# d = reversed(x)

if d == x:
    print('this number is a huiwen')
else:
    print('this number is not a huiwen')