'''
������26�� 
��Ŀ�����õݹ鷽����5!��
1.����������ݹ鹫ʽ��fn=fn-1*4!
2.����Դ���룺
'''
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum

for i in range(6):
    print('%d! = %d' % (i,fact(i)))
