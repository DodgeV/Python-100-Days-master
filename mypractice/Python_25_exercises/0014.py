'''第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
'''

import xlwt  
import json  
  
# 读取数据  
with open('student.txt', 'r', encoding='utf-8') as f:  
    data = f.read()  
    students = json.loads(data)  # 使用 json.loads() 替代 eval()  
  
# 创建 Excel 表格  
file = xlwt.Workbook()  
table = file.add_sheet('student')  
  
# 写入表头  
headers = ['Name', 'ID', 'Score']  
for col, header in enumerate(headers):  
    table.write(0, col, header, xlwt.easyxf('align: left'))  
  
# 写入学生数据  
for row, student in enumerate(students, start=1):  
    for col, key in enumerate(headers):  
        table.write(row, col, student.get(key, ''))  
  
# 保存 Excel 文件  
file.save('student.xls')
