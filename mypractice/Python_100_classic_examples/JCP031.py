'''
����31��
��Ŀ�����������ڼ��ĵ�һ����ĸ���ж�һ�������ڼ��������һ����ĸһ���������
�������жϵڶ�����ĸ��
python2 ʹ�� letter = stdin.read(1)  ��  stdin.flush()
python3 ʹ�� input
1.�����������������ȽϺã������һ����ĸһ�������ж����������if����жϵڶ�����ĸ��
2.����Դ���룺
'''
letter = input('input a letter:')
while True:
    if letter == 'S':
        print('please input second letter:')
        letter = input('input a letter:')
        if letter == 'a':
            print('Saturday')
            break
        elif letter  == 'u':
            print('Sunday')
            break
        else:
            print('data error')
    elif letter == 'F':
        print('Friday')
        break
    elif letter == 'M':
        print('Monday')
        break
    elif letter == 'T':
        print('please input second letter:')
        letter = input('input a letter:')
        if letter  == 'u':
            print('Tuesday')
            break
        elif letter  == 'h':
            print('Thursday')
            break
        else:
            print('data error')
            # break
    elif letter == 'W':
        print('Wednesday')
        break
    else:
        print('data error')
    letter = input('input a letter:')
