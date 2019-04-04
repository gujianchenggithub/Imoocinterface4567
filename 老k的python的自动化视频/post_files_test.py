import requests

host='http://httpbin.org/'
endpoint='post'
url=''.join([host,endpoint])
#普通上传
# files={'files':open('test.txt','rb')}

#通过文件上传字符串等！！
# files={'files':('test.txt','sssss')}

#3、自定义文件名、文件类型以及请求头（请求文件名称、文件路径、文件类型、文件请求头）
# files={'files':open('11.jpg','rb')}

#4、发送多个文件
# files=[
#     ('files1',('test.txt',open('test.txt','rb'))),
#     ('files2',('11.jpg',open('11.jpg','rb'),'image/png')),
# ]

#5、流式上传

with open('test.txt') as f:
    r=requests.post(url,data=f)

print(r.text)
resp=r.json()
print(resp["data"])