'''
【程序96】
题目：计算字符串中子串出现的次数
1.程序分析：
2.程序源代码：
'''
if __name__ == '__main__':
    str1 = input('input a string:\n')
    str2 = input('input a sub string:\n')
    ncount = str1.count(str2)
    print('{0} appears {1} times'.format(str2 ,ncount))
