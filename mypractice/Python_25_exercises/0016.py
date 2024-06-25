'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]

'''
import xlwt

with open('numbers.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    _numbers = eval(data)
    numbers = list()
    for i in range(3):
        numbers.extend(_numbers[i])
    row = len(numbers)//len(_numbers)

file = xlwt.Workbook()
table = file.add_sheet('numbers')
for i in range(len(numbers)):
    table.write(i // row, i % row, numbers[i])
file.save('numbers.xls')