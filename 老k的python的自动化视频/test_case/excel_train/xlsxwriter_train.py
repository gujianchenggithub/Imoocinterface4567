import xlsxwriter
import xlutils
workbook=xlsxwriter.Workbook('test1213.xlsx')
worksheet=workbook.add_worksheet('test')

worksheet.write('A1','的方式告诉对方')
worksheet.write(1,0,'的方式告诉对方')

