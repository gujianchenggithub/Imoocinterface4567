import requests
import unittest
from public import base
from public import HttpService
class PostDataTest(unittest.TestCase):
    def setUp(self):
        endpoint='post'
        self.url=base.get_url(endpoint)
    def test_post_data1(self):
        params={'show_env':1}
        data={'a':'巧吧软件测试','b':'form-data'}
        DataAll={'params':params,'data':data}
        resp=HttpService.MyHTTP().post(self.url,**DataAll)
        # r=requests.post(self.url,params=params,data=data)
        # resp=r.json()
        self.assertEqual(resp["form"]['a'],'巧吧软件测试')
        # print(resp["form"]['a'])
    # @unittest.skip('无条件跳过')
    def test_post_data2(self):
        params={'show_env':1}
        data={'a':'巧吧软件测试','b':'form-data'}
        DataAll={'params':params,'data':data}
        resp=HttpService.MyHTTP().post(self.url,**DataAll)
        form=resp.get('form').get('a')
        self.assertIsInstance(form,str)

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()