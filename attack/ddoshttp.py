#使用http进行ddos攻击

import requests

URL = "http://wechat.51fight.cn"
MAX_CONN = 20000



def connect():
	requests.get(URL)

def attack():
	for x in range(0,10):
		connect()

def func(x):
	if x > 5:
		return True;
	return False;

if __name__ == '__main__':
	print(list(filter(func,[1,2,3,4,10])))

	print(list(map(func,[1,5,10])))

	print(list(map(lambda x : x**2,[7,5])))
