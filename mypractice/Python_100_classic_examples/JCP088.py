'''
������88��
��Ŀ����ȡ7������1��50��������ֵ��ÿ��ȡһ��ֵ�������ӡ����ֵ��Ӧ�����ģ���
1.���������
2.����Դ���룺
'''
if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(eval(input('input a number:\n')))
        while a < 1 or a > 50:
            a = int(eval(input('input a number in [1~50]:\n')))
        print(a * '*')
        n += 1
