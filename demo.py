import requests
class RunMain(object):
    def __init__(self,url,method,data):
        self.url=url
        self.method=method
        self.data=data
    def send_post(self,url,data):
        r=requests.post(url=url,data=data)
        print(r.text)
if __name__ == '__main__':
    url='http://httpbin.org/post'
    data={
        'user':'51zxw',
        'passwd':'8888'
    }
    method='POST'
    run=RunMain(url,method,data)
    run.send_post(url=url,data=data)
