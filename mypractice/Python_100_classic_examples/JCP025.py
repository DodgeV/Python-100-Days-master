'''
������25�� 
��Ŀ����1+2!+3!+...+20!�ĺ�
1.����������˳���ֻ�ǰ��ۼӱ�����۳ˡ� 
2.����Դ���룺
'''
#����һ
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print('1! + 2! + 3! + ... + 20! = %d' % s)

#������
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print('1! + 2! + 3! + ... + 20! = %d' % s)