import unittest
from public import base
testcasefile='post_json_test.xlsx'
AllData=base.get_data(testcasefile,'AllData')
TestData=base.get_data(testcasefile,'TestData')

RequestData=TestData[1][1]
EndPoint=AllData[1][1]
RequestMethod=AllData[1][2]
expectedresult=TestData[1][2]




class PostJsonTest(unittest.TestCase):
    def setUp(self):
        endpoint=EndPoint
        self.url=base.get_url(endpoint)
    def test_post_json(self):
        # json={
        #     "info":{"code":1,"sex":"男","id":"1900","name":"巧吧软件测试"},
        #     "code":1,
        #     "name":"巧吧软件测试",
        #     "sex":"女",
        #     "data":[{"code":1,"sex":"男","id":"1900","name":"巧吧软件测试"},{"code":1,"sex":"男","id":"1900","name":"巧吧软件测试"}],
        #     "id":"1900"
        # }

        # r=requests.post(url,data=json.dumps(data))
        # print(r.headers)
        # print(r.text)
        DataAll=eval(RequestData)
        # DataAll={'json':json}
        # r=requests.post(self.url,json=json)
        # resp=json.loads(r.text)
        # resp=HttpService.MyHTTP().post(self.url,**DataAll)
        Method=RequestMethod
        resp=base.get_response(self.url,Method,**DataAll)
        name=resp.get('data')
        self.assertIsInstance(expectedresult,str)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()



