import unittest
from public import base
testcasefile='get_params_headers_test.xlsx'
AllDate=base.get_data(testcasefile,'AllData')
TestData=base.get_data(testcasefile,'TestData')

EndPoint=AllDate[1][1]
DataAlldd=TestData[1][1]
RequestMethod=AllDate[1][2]
expectedresult=TestData[1][2]


class GetParamsHeadersTest(unittest.TestCase):
    '''GET有params和headers测试！！'''
    def setUp(self):
        endpoint=EndPoint
        self.url=base.get_url(endpoint)
    def test_params_headers(self):
        '''校验浏览器是否为Chrome'''
        # params={'show_env':1}
        # headers={
        #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
        #     'Accept-Encoding':'gzip, deflate',
        #     'Accept':'*/*',
        #     'Connection':'keep-alive'}
        '''给服务器发送请求'''
        # DataAll={'params':params,'headers':headers}
        DataAll=eval(DataAlldd) #字符串的转变成字典格式
        # r=requests.get(self.url,params=params,headers=headers,stream=True)
        # resp=HttpService.MyHTTP().get2(self.url,**DataAll)
        # Method='get'
        Method=RequestMethod
        resp=base.get_response2(self.url,Method,**DataAll)
        User_Agent=resp['headers']['User-Agent']
        self.assertIn(expectedresult,User_Agent)

    # def tearDown(self):
    #     pass
if __name__ == '__main__':
    unittest.main()