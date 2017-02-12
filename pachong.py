# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
page = 18
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	#print response.read()
except urllib2.URLError , e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason

content = response.read().decode('utf-8')
#parttern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?></a><a.*?<h2>(.*?)</h2></a><div.*?'+'content">(.*?)</div></a><div.*?thumb">(.*?)</div><div class="stats.*?class="number">(.*?)</i>',re.S)
parttern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
items = re.findall(parttern,content)

for item in items:
	print item[0],item[1],item[2]