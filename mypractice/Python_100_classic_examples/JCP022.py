'''
������22��
��Ŀ������ƹ����ӽ��б������������ˡ��׶�Ϊa,b,c���ˣ��Ҷ�Ϊx,y,z���ˡ��ѳ�ǩ����
�����������������������Ա����������������a˵������x�ȣ�c˵������x,z�ȣ��������ҳ�
�������������ֵ������� 
1.����������ж������ķ�������һ�����ֱ�ȥ��2��sqrt(�����)������ܱ�������
���������������������������������֮�������� ������������
2.����Դ���룺 
'''
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\t c -- %s' % (chr(i),chr(j),chr(k)))