from shopclues.items import ImgData
import scrapy


class multipleData(scrapy.Spider):
	name='multipleData'
	start_urls=['http://www.shopclues.com/electronic-accessories-8/cameras-18/cameras-special.html?search=1&q1=camera',]

	def parse (self, response):
		for content in response.css('div.products-grid div.grid-product'):
			yield {
			'id': content.css('img::attr(id)').extract()
			}