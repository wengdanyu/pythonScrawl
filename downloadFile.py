#coding:utf-8
import requests
import mechanize
from bs4 import BeautifulSoup

def getResource(url):
	br = mechanize.Browser()
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	# print dir(mechanize._http)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
	
	# 设置表头
	headers = [
		('Cookie','JSESSIONID_GDS=cHAfth4Gs3tjpjzOoiACxe_sX2AxgrFiwXcz_wpKGKzQoSZt_Lbr!-1987278481;name=value'),
		('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
	]
	br.addheaders = headers
	try:
		res = br.open(url)# 打开网页
		
	except:
		print 'get resource fail'
		return None
	else:
		if res.getcode() == 200:
			return br.response().read()
		

def main():
	url = 'http://soda.datashanghai.gov.cn/query!queryGdsDataInfoById.action?type=0&dataId=AA4002017006'
	res = getResource(url)
	# 使用BeautifulSoup对返回的页面内容进行解析
	soup = BeautifulSoup(res,'lxml')
	trs = soup.find_all('tr',attrs={'class':'deep'})
	print(len(trs))
	for tr in trs:
		# print(tr.xpath('./td/text()').extract()[0])
		if tr.find('td'):
			print(tr.find('td').get_text())
			if tr.find('th').get_text().encode('utf-8') =='附件下载：':
				# fileLink = tr.find_all('a').get('href')
				fileLinks = tr.select('td > em > a')
				for fileLink in fileLinks:
					print('http://soda.datashanghai.gov.cn/'+fileLink.get('href'))
					res_url = 'http://soda.datashanghai.gov.cn/'+fileLink.get('href')
					response = requests.get(res_url)
					filename = fileLink.get('href').split('clientFilename=')[-1]
					# print(filename)
					with open(filename,'wb') as wp:
						wp.write(response.content)


if __name__ =='__main__':
	main()