#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import xlrd,xlwt
from xlutils.copy import copy

#打开excel
readbook = xlrd.open_workbook(r'C:\Users\kmf\接口复习\test.xlsx')
#获取读入文件的sheet
sheet1 = readbook.sheet_by_index(0)
sheet2 = readbook.sheet_by_name('sheet2')
allsheetnames = readbook.sheet_names()
print(sheet1,sheet2,allsheetnames)
#获取sheet最大行数和列数
nrows = sheet1.nrows#行
ncols = sheet2.ncols#列
print(nrows,ncols)
#获取某个单元格的值
lng = sheet1.cell(1,1).value#获取1行1列的表格值，从0开始计数
print(lng)
#获取某行/某列的值
row_value = sheet1.row_values(2)#获取x行的值，从0开始计数
col_value = sheet1.col_values(3)#获取y列的值，从0开始计数
print(row_value,col_value)




