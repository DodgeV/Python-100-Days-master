'''
��Ŀ��һ��5λ�����ж����ǲ��ǻ���������12321�ǻ���������λ����λ��ͬ��ʮλ��ǧλ��ͬ��������
1.���������ͬ29��
2.����Դ���룺
'''
# ����1
x = input("input a number:")


for i in range(int(len(x)/2)):
    if x[i] != x[-i - 1]:
        print('this number is not a huiwen')
        x = None
        break
if x:
    print('this number is a huiwen')

# ����2
x = input("input a number:")
d = x[::-1]

# x = list(input('input a number:'))
# d = reversed(x)

if d == x:
    print('this number is a huiwen')
else:
    print('this number is not a huiwen')