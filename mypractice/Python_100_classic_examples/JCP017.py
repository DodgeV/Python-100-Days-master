'''
【程序17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
1.程序分析：利用while语句,条件为输入的字符不为'\n'.
　　　　　　
2.程序源代码：
'''
import string
s = input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha(): # 英文字母
        letters += 1
    elif c.isspace(): # 空格
        space += 1
    elif c.isdigit(): # 数字
        digit += 1
    else: # 其它字符
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))
