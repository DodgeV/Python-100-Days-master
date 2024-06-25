'''
【程序23】 
题目：打印出如下图案（菱形）

   *
  ***
 *****
*******
 *****
  ***
   *
1.程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重
　　　　　　for循环，第一层控制行，第二层控制列。 
2.程序源代码： 
'''

for i in range(4):
    for j in range(2 - i + 1):
        print(' ',end = "")
    for k in range(2 * i + 1):
        print('*',end = "")
    print("")

for i in range(3):
    for j in range(i + 1):
        print(' ',end = "")
    for k in range(4 - 2 * i + 1):
        print('*',end = "")
    print("")
