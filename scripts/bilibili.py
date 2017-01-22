#
#此脚本用来完成B站相关的功能操作
#
#
#
#
#
import requests
headers = {
	"Cookie" :  "sid=9qhhgp1a; fts=1467304323; LIVE_BUVID=f0e37c7a5dc0c3f5ffad7be90daeb990; LIVE_BUVID__ckMd5=7db44986fcf26859; buvid3=904CEB19-D2FE-43B4-B16A-B4FA60B2BD6F19756infoc; rpdid=kwmwlqpmwmdopqkkxsxxw; DedeUserID=7217992; DedeUserID__ckMd5=845ac2206f48575a; SESSDATA=aed075d4%2C1487080048%2C514d96be; ck_pv=NIdO36; SSID=mD8d_aUcrQcaBI7D1eGEC6sHfgxpZ_alPhykH9DBGK916pc6s8nVNdeZvmG25mJS99S6BRumMRCYjqzkKb_bSf49NtQmQLI43W73spS7HbgFQY_c; _ver=1; purl_token=bilibili_1485096438; _cnt_dyn=null; _cnt_pm=0; _cnt_notify=30; uTZ=-480; _dfcaptcha=1ee215627f8c6cd2da8a8e41ea60d7f4",
	"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36"
	}

#查询番剧列表
def query_list():
	url = "http://data.bilibili.com/v/web/web_count_event"
	data = {
		"mid" : "7217992",
		"fts" : "1467304323",
		"url" : "http%3A%2F%2Fbangumi.bilibili.com%2Fanime%2Ftimeline",
		"proid" : "1",
		"ptype" : "1",
		"eid": "anime_timeline_guide",
		"args" : "daynumber:6",
		"_" : "1485101678929"
		}
	#添加header中的数据
	headers['Origin'] = 'http://bangumi.bilibili.com'
	headers['Referer'] = 'http://bangumi.bilibili.com/anime/timeline'
	headers['Host'] = 'data.bilibili.com'
	res = requests.get(url,data = data, headers = headers)
	print(dir(res))
	print(res.headers)
	return res.content

#评论
def add_reply():
	url = "http://api.bilibili.com/x/v2/reply/add"
	data = {
		"oid":"8159858", 
		"type":"1",
	 	"message":"强势围观经费传说",
		 "plat":"1", "jsonp":"jsonp"
		}
	res = requests.post(url,data = data, headers = headers)

	return res.content


if __name__ == '__main__':
	# res = requests.get("http://www.bilibili.com/")
	# print(dir(res))
	# print(res.content)
	# reply = add_reply()
	# print(reply)
	animelist = query_list()
	print(animelist)



