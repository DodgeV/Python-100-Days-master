'''
【程序79】
题目：字符串排序。
1.程序分析：
2.程序源代码：
'''
if __name__ == '__main__':
    str1 = input('input string:\n')
    str2 = input('input string:\n')
    str3 = input('input string:\n')
    print(str1,str2,str3)
    
    if str1 > str2 : str1,str2 = str2,str1
    if str1 > str3 : str1,str3 = str3,str1
    if str2 > str3 : str2,str3 = str3,str2

    print('after being sorted.')
    print(str1,str2,str3)
