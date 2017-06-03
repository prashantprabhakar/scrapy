import scrapy
from jabong.items import products

class namePriceImg(scrapy.Spider):
	name='jabongNamePriceImg'
	start_urls=['http://www.jabong.com/men/clothing/denims/denim-shirts/?tt=shirts&s=5&rank=6&qc=denim%20shirts%20men']

	def parse(self,response):
		productss= response.xpath('/html/body/section[1]/div/section/div/section/section[2]/div[1]/a/div')

		for p in productss:
			item=products()
			item['name']=p.xpath('div[1]/span/text()').extract()
			item['price']=p.xpath('div[2]/span[2]/text()').extract()