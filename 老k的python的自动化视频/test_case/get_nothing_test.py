import requests
import unittest
from public import base
from ddt import ddt,data,unpack

@ddt
class GetNothing(unittest.TestCase):
    '''GET无参数测试'''
    def setUp(self):
        endpoint='get'
        self.url=base.get_url(endpoint)
    @data(200,400,500,201,301)
    def test_1(self,result):
        '''校验状态码是否为200'''
        r=requests.get(self.url)
        status_code=r.status_code
        self.assertEqual(status_code,result)
    @data(('headers','Connection','close'),('headers','Host','httbin.org'))
    @unpack
    def test_2(self,headers,value,result):
        '''校验header里的Connection的值'''
        r=requests.get(self.url)
        resp=r.headers['Connection']
        # print(resp)
        # self.assertEqual(r.headers['Connection'],'keep-alive')
        self.assertEqual(resp,'keep-alive')
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()