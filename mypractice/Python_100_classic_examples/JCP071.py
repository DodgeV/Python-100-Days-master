'''
������71��
��Ŀ����дinput()��output()��������&���5��ѧ�������ݼ�¼��
1.���������
2.����Դ���룺
ʹ��list��ģ��ṹ����ʹ��class��
stu = [string,string,list]
'''
N = 3
#stu
    # num : string
    # name : string
    # score[4]: list
student = []
for i in range(5):
    student.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))

def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % ( stu[i][0],stu[i][1] ),end = " ")
        for j in range(3):
            print('%-8d' % stu[i][2][j],end = " ")
        print('\n')

if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)
