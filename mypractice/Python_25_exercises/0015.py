'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''

import xlwt  
  
# 读取并解析数据  
with open('city.txt', 'r', encoding='utf-8') as f:  
    data = f.read()  
    city_data = eval(data)  # 注意：使用eval处理不信任的输入是不安全的  
  
# 准备Excel工作簿和工作表  
file = xlwt.Workbook()  
table = file.add_sheet('city')  
  
# 定义左对齐样式  
style = xlwt.XFStyle()  
alignment = xlwt.Alignment()  
alignment.horz = xlwt.Alignment.HORZ_LEFT  
style.alignment = alignment  
  
# 写入数据  
row = 0  # 初始化行号  
for key, value in city_data.items():  
    # 写入城市编号（作为字符串，因为键是字符串）  
    table.write(row, 0, key, style)  
    # 写入城市名  
    table.write(row, 1, value, style)  
    row += 1  # 移动到下一行  
  
# 保存Excel文件  
file.save('city.xls')
