'''
������68��
��Ŀ����n��������ʹ��ǰ�����˳�������m��λ�ã����m���������ǰ���m����
1.���������
2.����Դ���룺
'''

number = []

def move(array,n,m):
    array_end = array[n - 1]
    for i in range(n - 1,-1,- 1):
        array[i] = array[i - 1]
    array[0] = array_end
    m -= 1
    if m > 0:move(array,n,m)

if __name__ == '__main__':
    n = int(input('the total number is:\n'))
    m = int(input('move back m bits:\n'))

    for i in range(n):
        number.append(int(input('input a number:\n')))
    
    print('orignal number:',number)

    move(number,n,m)

    print('after moved:',number)
