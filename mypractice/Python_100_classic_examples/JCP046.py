'''
【程序46】
题目：宏#define命令练习(1)　　　
1.程序分析：
2.程序源代码：
没有C语言的宏，就这么写了
'''

def SQ(x):
    return x * x
print('Program will stop if input value less than 50.')
again = 1
while again:
    num = int(input('Please input number：'))
    print('The square for this number is： %d' % (SQ(num)))
    if num >= 50:
        again = True
    else:
        again = False
