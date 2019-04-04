from public import Config
from public import HttpService
from public import read_excel

def get_url(EndPoint):
    host=Config.url()
    endpoint=EndPoint
    url=''.join([host,endpoint])
    return url
def get_response(url,Method,**DataAll):
    if Method=='get':
        resp=HttpService.MyHTTP().get(url,**DataAll)
    elif Method=='post':
        resp=HttpService.MyHTTP().post(url,**DataAll)
    return resp

def get_response2(url,Method,**DataAll):
    if Method=='get':
        resp=HttpService.MyHTTP().get2(url,**DataAll)
    elif Method=='post':
        resp=HttpService.MyHTTP().post2(url,**DataAll)
    return resp

def get_data(testfile,sheetname):
    datainfo=read_excel.XLDateinfo(r'E:\www\Imoocinterface\老k的python的自动化视频\test_data\%s'%testfile)
    Data=datainfo.get_sheetinfo_by_name(sheetname)
    return Data