'''
������39��
��Ŀ����һ���Ѿ��ź�������顣������һ������Ҫ��ԭ���Ĺ��ɽ������������С�
1. ��������������жϴ����Ƿ�������һ������Ȼ���ٿ��ǲ����м����������������
������������Ԫ��֮����������κ���һ��λ�á� 
2.����Դ���룺 
'''
if __name__ == '__main__':
    # ����һ
    a = [1,4,6,9,13,16,19,28,40,100]
    print('original list is:',a)
    number = int(input("insert a new number:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print('the new list is:',a)
    # ������
    # insert another number
    number = int(input('input a new number:\n'))
    if number > a[-1]:
        a.append(number)
    else:
        for i in range(len(a)):
            if a[i] > number:
                a.insert(i,number)
                break
    print('the new list is:',a)
