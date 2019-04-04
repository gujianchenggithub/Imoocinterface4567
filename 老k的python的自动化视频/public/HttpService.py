import requests
from public import Config
class MyHTTP(object):
    def __init__(self):
        self.url=Config.url()

    def get(self,url,params):
        resp=requests.get(url,params=params)
        return resp

    def get2(self,url,**DataAll):
        params=DataAll.get('params')
        headers=DataAll.get('headers')
        try:
            resp2=requests.get(url,params=params,headers=headers)
            text=resp2.json()
            return text
        except Exception as e:
            print('GET错误：s%'%e)

    def post(self,url,**DataAll):
        params=DataAll.get('params')
        headers=DataAll.get('headers')
        data=DataAll.get('data')
        json=DataAll.get('json')
        files=DataAll.get('files')
        try:
            resp2=requests.post(url,params=params,headers=headers,data=data,json=json,files=files,timeout=3)
            text=resp2.json()
            return text
        except Exception as e:
            print('POST错误：%s'%e)