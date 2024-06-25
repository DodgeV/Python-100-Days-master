'''
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''
# 实现有误
import xlrd
from xml.dom import minidom, Node


def gen_xml(root, child, comment, data):
    doc = minidom.Document()
    node_root = doc.createElement(root)
    node_students = doc.createElement(child)
    node_students.appendChild(doc.createComment(comment))
    node_students.appendChild(doc.createTextNode(data))
    node_root.appendChild(node_students)
    doc.appendChild(node_root)
    filename = child + '.xml'
    with open(filename, 'w', encoding='utf-8') as f:
        doc.writexml(f, newl='\n')


def xls_to_xml(filename, comment):
    file = xlrd.open_workbook(filename)
    table = file.sheet_by_name(filename.split('.')[0])
    row = table.nrows
    data = dict()
    for i in range(row):
        data[str(i+1)] = table.row_values(i)[1:]
    print(str(data))
    gen_xml('root', 'students', comment, str(data))

# comment = "学生信息表'id' : [名字, 数学, 语文, 英文]"
# xls_to_xml('student.xls', comment)