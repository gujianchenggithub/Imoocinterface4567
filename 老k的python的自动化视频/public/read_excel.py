import xlrd
class XLDateinfo():
    def __init__(self,path=''):
        self.xl=xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,name):
        self.sheet=self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheet_info(self):
        infolist=[]
        for row in range(0,self.sheet.nrows):
            info=self.sheet.row_values(row)
            infolist.append(info)
        return infolist
if __name__ == '__main__':
    datainfo=XLDateinfo(r'E:\www\Imoocinterface\老k的python的自动化视频\test_data\get_params_headers_test.xlsx')
    alldata=datainfo.get_sheetinfo_by_name('AllData')
    TestData=datainfo.get_sheetinfo_by_name('TestData')
    print(alldata)
    print(TestData)