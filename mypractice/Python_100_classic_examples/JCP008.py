'''
������8��
��Ŀ�����9*9�ھ���
1.����������������п��ǣ���9��9�У�i�����У�j�����С�
2.����Դ���룺
#include "stdio.h"
main()
{
��int i,j,result;
��printf("\n");
��for (i=1;i<10;i++)
����{ for(j=1;j<10;j++)
��������{
����������result=i*j;
����������printf("%d*%d=%-3d",i,j,result);/*-3d��ʾ����룬ռ3λ*/
��������}
������printf("\n");/*ÿһ�к���*/
����}
}
'''
# for - for
for i in range(1,10):
    for j in range(1,i+1):
        print('%d��%d=%-3d' % (i,j,i*j),end = "")
    print("\n")
    
# while - while
i = 1
while i <= 9:
    j = 1
    while(j <= i):
        print(f'{i}��{j}={i*j}',end = "\t")
        j += 1
    print("")
    i += 1