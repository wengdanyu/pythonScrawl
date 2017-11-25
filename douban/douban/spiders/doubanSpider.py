from scrapy.spiders import Spider
from scrapy.http import Request
from douban.items import DoubanItem,commentItem
from scrapy import Field

import json
import requests
import re
import scrapy

class doubanSpider(Spider):
	name = 'douban'

	start_urls = ['https://book.douban.com/top250?icn=index-book250-all']
	book_urls = []
	
	def parse(self,response):
		books = response.xpath('//*[@id="content"]/div/div[1]/div/table')
		# print(books)
		for book in books:
			db = DoubanItem()
			db['item_type'] = 'DoubanItem'
			if book.xpath('tr[@class="item"]/td[2]/div[1]/a/text()'):
				db['bname'] = book.xpath('tr[@class="item"]/td[2]/div[1]/a/text()').extract()[0].strip()
			
			if book.xpath('tr[@class="item"]/td[2]/div[1]/a/@href'):
				db['url'] = book.xpath('tr[@class="item"]/td[2]/div[1]/a/@href').extract()[0].strip()
				# print(db['url'])
			
			if book.xpath('tr/td[2]/p[1]/text()'):
				db['author'] = book.xpath('tr/td[2]/p[1]/text()').extract()[0].split('/')[0].strip()
			
			if book.xpath('tr/td[2]/div[2]/span[@class="rating_nums"]/text()'):
				db['start'] = book.xpath('tr/td[2]/div[2]/span[@class="rating_nums"]/text()').extract()[0].strip()
			
			if book.xpath('tr/td[2]/p[2]/span/text()'):
				db['quote'] = book.xpath('tr/td[2]/p[2]/span/text()').extract()[0].strip()
			# print(db)
			yield(db)
			yield Request(db['url']+'comments/',self.parse_detail,meta={'item':db['url']})
	
	def parse_detail(self,response):
		# print(response.url)
		detail_url = response.meta['item']
		comment_items = response.xpath('//*[@id="comments"]/ul/li[@class="comment-item"]')
		# print(len(comment_items))
		for comment_item in comment_items:
			comment = commentItem()
			comment['item_type'] = 'commentItem'
			comment['url'] = detail_url
			if comment_item.xpath('div[@class="comment"]/h3/span[2]/a/text()'):
				comment['name'] = comment_item.xpath('div[@class="comment"]/h3/span[2]/a/text()').extract()[0].strip()
			if comment_item.xpath('div[2]/h3/span[2]/a/@href'):
				comment['person_url'] =comment_item.xpath('div[2]/h3/span[2]/a/@href').extract()[0].strip()
			if comment_item.xpath('div[@class="comment"]/h3/span[2]/span[2]/text()'):
				comment['publish_time'] =comment_item.xpath('div[@class="comment"]/h3/span[2]/span[2]/text()').extract()[0].strip()
			if comment_item.xpath('div[@class="comment"]/p/text()').extract()[0].strip():
				comment['content'] =comment_item.xpath('div[@class="comment"]/p/text()').extract()[0].strip()
			print(comment)
			yield comment








