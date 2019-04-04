import unittest
from demo import RunMain
class TestMethod(unittest.TestCase):
    def test_01(self):
        url='http://httpbin.org/post'
        data={
            'user':'51zxw',
            'passwd':'8888'
        }
        method='POST'
        run=RunMain(url,method,data)
        run.send_post(url=url,data=data)
        self.assertEqual(run['form'],{"passwd": "8888", "user": "51zxw" })
    def test_02(self):
        url='http://httpbin.org/post'
        data={
            'user':'51zxw',
            'passwd':'8888'
        }
        method='POST'
        run=RunMain(url,method,data)
        run.send_post(url=url,data=data)
if __name__ == '__main__':
    unittest.main()