#!/usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
import re

def proxy_spider():
	url = 'http://www.xicidaili.com/nn'
  #header should be reset if deployed on a new host
	header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

	r = requests.get(url = url, headers = header)

	soup = bs(r.content, 'lxml')

	datas = soup.find_all(name = 'tr', attrs = {'class': re.compile('|[^odd]')})

	for data in datas:
		soup_proxy_content = bs(str(data), 'lxml')
		soup_proxys = soup_proxy_content.find_all(name = 'td')
		ip = str(soup_proxys[1].string)
		port = str(soup_proxys[2].string)
		types = str(soup_proxys[5].string) 
		proxy_check(ip, port, types)
		
def proxy_check(ip, port, types):
	proxy = {}
	proxy[types.lower()] = '%s:%s'%(ip, port)
	try:
		r = requests.get('http://1212.ip138.com/ic.asp', proxies = proxy, timeout = 6)
		ip_content = re.findall(r'\[(.*?)\]', r.text)[0]
		if ip == ip_content:
			print proxy
	except Exception, e:
		pass

proxy_spider()
