#coding:utf-8
import mechanize
from bs4 import BeautifulSoup
from getHeader import getHeader
class getDouBan():
	def __init__(self):
		self.url = 'https://www.douban.com/'
		self.headerFile = 'headerRaw.txt'
		self.outFile = 'douban.txt'

		self.spider()

	def getRes(self,url):
		br = mechanize.Browser()
		br.set_handle_equiv(True)
		br.set_handle_redirect(True)
		br.set_handle_referer(True)
		br.set_handle_robots(False)
		# print dir(mechanize._http)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
		
		headers = getHeader(self.headerFile)# 设置表头
		br.addheaders = headers
		# br.set_header(headers)
		br.open(url)# 打开网页
		return br.response().read()




	def spider(self):
		res = self.getRes(self.url)
		# soup = BeautifulSoup(res,'html5lib')
		soup = BeautifulSoup(res,'lxml')
		# lis = soup.find_all('li')
		# for li in lis:
		# 	print li.get_text()
		# print()

if __name__ =='__main__':
	getDouBan()

		

	
