'''
������32��
��Ŀ��Press any key to change color, do you want to try it. Please hurry up!
1.���������������������������������
2.����Դ���룺
#include <conio.h>
	void main(void)
	{
		int color;
		for (color = 0; color < 8; color++)
		{
			textbackground(color); /*�����ı��ı�����ɫ*/
			cprintf("this is color %d\r\n",color);
			cprintf("ress any key to continue\r\n");
			getch();  /*�����ַ�������*/
		}
	}
'''
