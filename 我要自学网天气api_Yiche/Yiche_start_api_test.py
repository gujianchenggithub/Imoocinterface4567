import requests
from urllib import parse
url='https://selectcar.yiche.com/selectcarforapp?mid=7&s=4&page=1&pagesize=20&cityId=201'
data={'name':'汉兰达'}
name=parse.urlencode(data).encode('utf-8')

r=requests.get(url=url,params=name)
respons_data=r.json()
print(respons_data)
print(respons_data['status'])
print(respons_data['data']['resList'][4]['name'])