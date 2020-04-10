#!/usr/bin/python
# coding: utf-8
import requests
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
f=open("/Users/zad/Desktop/test /子域名爆破/字典.txt","r")
c = raw_input("输入要查询的domain:(比如baidu.com):")
b=0
d="ok"
print "努力查询中。。。"
while True:
    line=f.readline()
    if line:
        a=line.strip()
        try:
            url='http://'+a+'.'+c
            r=requests.get(url,headers=headers)
            if r.status_code==200:
                b=b+1
                print "\033[1;45m [+]....找到...... \033[0m",r.url
        except requests.exceptions.ConnectionError:
            pass
                                                    
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.ConnectTimeout:
            pass
    else:
        break
d=str(b)
print "[!]^_^一共找到了"+d+"个子域名!"
f.close()


