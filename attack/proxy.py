# 模仿网上的版本使用python3进行重构
import requests
from bs4 import BeautifulSoup
proxy = open('proxy.txt','w')

for page in range(1,3):
	url = 'http://www.xicidaili.com/nn/%s'%page
	print(url)
	cookies = {'_free_proxy_session':'BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTg1NDJjY2ZmOTU1NmJlZjI4Y2Q2YTA4MDc5ZTJmYzMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXNZT0tZN0FucDRua1JPUmw1QVJ5NVFMME5iVVNiZnd1MkhSRzRiaHRjOXc9BjsARg%3D%3D--b69cda4c69ca88fa6eab24c4039786c21228757a'}
	user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
	headers = {'User_Agent':user_agent,'Connection':'keep-alive','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Host': 'www.xicidaili.com'}
	response = requests.get(url, headers = headers, cookies = cookies)
	print(response.text)

url = "http://www.baidu.com"
res = requests.get(url)
print(dir(res))
