import requests
check_url = "http://wechat.51fight.cn"

def check_proxy_ip(proxy):
	proxies = proxy
	try:
		res = requests.get(check_url, proxies=proxy)
		if res:
			return True
	except Exception as e:
		print(e)
		return False
	return False


proxy = {"HTTP" : "125.118.78.174:808"}
print(check_proxy_ip(proxy))
