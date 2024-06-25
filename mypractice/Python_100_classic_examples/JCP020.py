'''
【程序20】
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
　　　第10次落地时，共经过多少米？第10次反弹多高？
1.程序分析：见下面注释
2.程序源代码：
'''
Sn = 100.0 # 第一次落地时经过100米
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn # 第n次经过多少米
    Hn /= 2 # 第n次的高度

print('Total of road is %f' % Sn)
print('The tenth height is %f meter' % Hn)
