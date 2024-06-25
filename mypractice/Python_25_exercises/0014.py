'''第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
'''

import xlwt

with open('student.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    _student = eval(data)
    student = list()
    for i in range(1, 4):
        info = _student[str(i)]
        student.append(i)
        student.extend(info)
    row = len(_student)/len(student)


def horz_left(x, y, data):
    algnt = xlwt.Alignment()
    algnt.horz = xlwt.Alignment.HORZ_LEFT
    style = xlwt.XFStyle()
    style.alignment = algnt
    table.write(x, y, data, style)

file = xlwt.Workbook()
table = file.add_sheet('student')
for i in range(len(student)):
    if not i % 5:
        horz_left(i//5, i % 5, student[i])
    else:
        table.write(i//5, i % 5, student[i])

file.save('student.xls')