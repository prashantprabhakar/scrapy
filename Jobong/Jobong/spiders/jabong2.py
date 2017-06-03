import scrapy
#from scrapy.exceptions import CloseSpider

from scrapy.spiders import Spider
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from Jobong.items import products
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector    

class propubSpider(scrapy.Spider):
	name = 'koovs'
	allowed_domains = ['jabong.com']
	max_pages = 4

	def start_requests(self):
		for i in range(self.max_pages):
			yield scrapy.Request('http://www.jabong.com/women/clothing/tops-tees-shirts/tops/?page=%d' % i, callback=self.parse)

			def parse(self, response):
				for sel in response.xpath('//*[@id="catalog-product"]/section[2]'):
					item = product()
					item['price'] = sel.xpath('//*[@class="price"]/span[2]/text()').extract()
					item['image'] = sel.xpath('//*[@class="primary-image thumb loaded"]/img').extract()
					item['title'] = sel.xpath('//*[@data-original-href]/@href').extract() 
