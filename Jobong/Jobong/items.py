# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item

class JobongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class product(scrapy.Item):
	price=scrapy.Field()
	#img=scrapy.Field()
	title=scrapy.Field()

class products(scrapy.Item):
	price=scrapy.Field()
	image=scrapy.Field()
	title=scrapy.Field()