# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class DoubanPipeline(object):
	def __init__(self):
		self.file1 = codecs.open('book_top250.json',encoding='utf-8',mode='wb')
		self.file2 = codecs.open('book_top250comment.json',encoding='utf-8',mode='wb')

	def process_item(self,item,spider):
		# print(item['item_type']+'--<')
		# line = json.dumps(dict(item),ensure_ascii = False)+'\n'
		# self.file1.write(line)
		# return item
		if item['item_type'] =='DoubanItem':
			line = json.dumps(dict(item),ensure_ascii = False)+'\n'
			self.file1.write(line)
			return item
		elif item['item_type'] =='commentItem':
			line = json.dumps(dict(item),ensure_ascii=False)+'\n'
			self.file2.write(line)
			return item
  # def process_item(self, item, spider):