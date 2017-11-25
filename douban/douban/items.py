# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_type = Field()
    bname = Field()
    url = Field()
    author = Field()
    quote = Field()
    start = Field()
    # pass
class commentItem(scrapy.Item):
    item_type = Field()
    url = Field()
    name = Field()
    person_url = Field()
    publish_time = Field()
    content = Field()

