import unittest
import requests
from public import base
from public import HttpService
class GetParams(unittest.TestCase):
    def setUp(self):
        endpoint='get'
        self.url=base.get_url(endpoint)
    def test_get_params1(self):
        params={'show_env':1}
        DataAll={'params':params}
        Method='get'
        # resp=HttpService.MyHTTP().get(self.url,params)
        resp=base.get_response(self.url,Method,**DataAll)
        self.assertEqual(resp.headers['Connection'],'keep-alive')
    def test_get_params2(self):
        params={'show_env':1}
        DataAll={'params':params}
        Method='get'
        # resp=HttpService.MyHTTP().get(self.url,params)
        resp=base.get_response(self.url,Method,**DataAll)
        self.assertEqual(resp.headers['Content-Encoding'],'gzip')
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.mian()