import requests
host='http://httpbin.org/'
endpoint='cookies/set/sessioncookies/123456789'
url=''.join([host,endpoint])
url1='http://httpbin.org/cookies'


r=requests.get(url1)
print(r.text)


session=requests.Session()
session.get(url)
r1=session.get(url1)
print(r1.text)

header1={'test1':'aa'}
header2={'test2':'bb'}

session1=requests.session()
session1.headers.update(header1)
r2=session1.get('http://httpbin.org/headers',headers=header2)
print(r2.text)

session1.headers['test1']=None
r3=session1.get('http://httpbin.org/headers',headers=header2)
print(r3.text)