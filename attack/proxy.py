# 模仿网上的版本使用python3进行重构
import requests
import re
from bs4 import BeautifulSoup
proxy = open('proxy.txt','w')
proxy_list = open('proxy_list.txt','w')


for page in range(1,2):
    url = 'http://www.xicidaili.com/nn/%s'%page
    headers = {
        "Host": "www.xicidaili.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
    }

    response = requests.request('GET',url, headers = headers)
    print(response.text)
    res = BeautifulSoup(response.text)
    # print(res.find_all(re.compile("\d.\d.\d.\d")))
    data = []
    table = res.find('table', id="ip_list")
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        tmp = []
        for item in cells:
            tmp.append(item.find(text=True))
        try:
            tmp2 = tmp[1:2][0]
            tmp3 = tmp[2:3][0]
            tmp4 = tmp[5:6][0]
            data.append({tmp4: tmp2 + ":" + tmp3})
            proxy.write( tmp4 + ":" + tmp2 + ":" + tmp3 + "\n")
        except Exception as e:
                pass

    print(table)
    print(type('table'))
    print(type(table.findAll("tr")))

    print(data)
    proxy_list.write(str(data))



