import asyncio
import time
import pymongo
from urllib.parse import urlencode
import requests
import re

urls = []
clients = pymongo.MongoClient('localhost')
db = clients["newstt"]
col = db["news"]

def get_urls():

	for page in range(1,2):
		data= {
		'channel':'news',
		'cat_1':'gnxw',
		'cat_2':'=gdxw1||=gatxw||=zs-pl||=mtjj',
		'level':'=1||=2',
		'show_ext':1,
		'show_all':1,
		'show_num':22,
		'tag':1,
		'format':'json',
		'page':page
	}
		url = 'http://api.roll.news.sina.com.cn/zt_list?'+urlencode(data)
		urls.append(url)


async def parse_page_index(html):
	html = json.loads(html)
	if 'result' in html.keys():
		result = [data['url'] for data in html['result']['data']] # 返回详情页的url，放在result中
	return result


async def get_detail_urls(urls):
	detail_urls = []
	for url in urls:
		reg = re.search('doc-i(.*?).shtml',url)
		news_id = reg.group(1)
		# news_id = url.split('/')[-1].lstrip('doc-i').rstrip('.shtml')
		# print(news_id)
		detail_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}'
		durl = detail_url.format(news_id)# print(durl)
		detail_urls.append(durl)
	return detail_urls

async def get_page_url(url,future):
	response = requests.get(url)
	print(response.status_code)
	result = await parse_page_index(response.text) # 得到一页当中的详情页
	ha = await get_detail_urls(result)
	dic = {
		'url':url,
		'result':ha
	}
	future.set_result(dic)


def parse_detail_url(future):
	# print(future.result())
	for url in future.result()['result']:
		res = requests.get(url)
		res = json.loads(res.text.lstrip('var data='))
		if res and 'result' in res.keys():
			news= {
				'title' : res['result']['news']['title'],
				'url':future.result()['url'],
				'releaseTime':res['result']['news']['time'],
				'commentCount':res['result']['count']['total']
			}
			print(news)
			col.insert(news)
			print('成功掺入一组数据'+str(news))
	loop.stop()

get_urls()
loop = asyncio.get_event_loop()

for url in urls:
	print(url)
	future = asyncio.Future()
	asyncio.ensure_future(get_page_url(url,future))
	future.add_done_callback(parse_detail_url)

try:
    loop.run_forever()
finally:
	loop.close()
