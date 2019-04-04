import unittest
import requests
from time import sleep
from urllib import parse
class YicheTest(unittest.TestCase):
    def setUp(self):
        self.url='https://selectcar.yiche.com/selectcarforapp?mid=7&s=4&page=1&pagesize=20&cityId=201'

    def test_yicge_hanlanda(self):
        data={'name':'汉兰达'}
        name=parse.urlencode(data).encode('utf-8')
        r=requests.get(self.url,params=name)
        result=r.json()
        self.assertEqual(result['data']['resList'][4]['name'],'汉兰达')
        sleep(3)

    def test_yiche_param_error(self):
        data={'mid':'rrrr'}
        url='https://selectcar.yiche.com/selectcarforapp?'
        r=requests.get(url,params=data)
        result=r.json()
        self.assertEqual(result['status'],1)

    def test_yiche_no_param(self):
        url='https://selectcar.yiche.com/selectcarforapp'
        r=requests.get(url)
        result=r.json()
        self.assertEqual(result['data']['count'],1225)

if __name__ == '__main__':
    unittest.main()