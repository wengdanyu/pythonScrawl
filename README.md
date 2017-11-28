# pythonScrawl
以下是对每个项目的简单介绍：

#getNews.py
use python to crawl information from web
通过使用python asyncio 获取新浪最新新闻

#douban
使用scrapy抓取豆瓣top250的图书信息，一下部分评论

#doubanCheck
mechanize模块，运用cookies和user_agent模拟登录豆瓣网
headerRaw.txt存储的是手动登录豆瓣网后，从chrome的network中对主页的请求参数复制过来形成的一个文件
Accept:
Accept-Encoding:
...
Cookie:
...
User-Agent:
getHeader.py是对该headerRaw.txt提取，返回cookies和useragent的元组
