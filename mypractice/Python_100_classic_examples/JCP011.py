'''
������11��
��Ŀ���ŵ����⣺��һ�����ӣ��ӳ������3������ÿ���¶���һ�����ӣ�С���ӳ�����������
��������ÿ��������һ�����ӣ��������Ӷ���������ÿ���µ���������Ϊ���٣�
1.��������������ӵĹ���Ϊ����1,1,2,3,5,8,13,21....
2.����Դ���룺
main()
{
long f1,f2;
int i;
f1=f2=1;
for(i=1;i<=20;i++)
��{ printf("%12ld %12ld",f1,f2);
������if(i%2==0) printf("\n");/*���������ÿ���ĸ�*/
������f1=f1+f2; /*ǰ�����¼�������ֵ����������*/
������f2=f1+f2; /*ǰ�����¼�������ֵ����������*/
��}
}
'''
f1 = 1
f2 = 1
for i in range(1,21):
    print('%12d %12d' % (f1,f2))
    if (i % 2) == 0:
        print('')
    f1 = f1 + f2
    f2 = f1 + f2
    