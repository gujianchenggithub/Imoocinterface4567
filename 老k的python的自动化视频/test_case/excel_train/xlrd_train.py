# from datetime import date,datetime
# newpath=os.chdir(r'E:\www\Imoocinterface\老k的python的自动化视频\test_case\excel_train')

import os
import xlrd
filename="100G测试资源（视频+教程）免费获取.xlsx"
file=os.path.join(os.getcwd(),filename)
'''1.打开文件'''
x1=xlrd.open_workbook(file)
# print(x1.sheet_names())
'''2.获取sheet'''
# print(x1.nsheets)
'''3.获取sheet内的汇总数据'''
table1=x1.sheet_by_name('目录')
# print(table1.name)
# print(table1.nrows)
# print(table1.ncols)
'''4.单元格批量读取'''
# print(table1.row_values(0,1,4))
# print(table1.col_values(0,0,2))
'''5.特定单元格读取'''  #三种方式呢
# print(table1.cell(1,2).value)
'''6.常用技巧：（0,0）转换成A1'''

print(xlrd.cellname(0,0))
'''7.获取表格内不同类型的name'''













