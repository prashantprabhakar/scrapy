from shopclues.items import ImgData
import scrapy


class multipleImages(scrapy.Spider):
	name='multipleImages'
	start_urls=['http://www.shopclues.com//electronic-accessories-8/cameras-18/cameras-special.html?search=1&q1=camera']
	def parse (self, response):
		images = ImgData()
		images['image_urls']=[] 
		for url in response.css('div.products-grid div.grid-product'):
			images['image_urls'].append(url.css('img::attr(src)').extract_first())
			yield images
