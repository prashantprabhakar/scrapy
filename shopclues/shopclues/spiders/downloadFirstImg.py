from shopclues.items import ImgData
import scrapy
import datetime


class DownloadFirstImg(scrapy.Spider):
	name="DownloadfirstImg"
	start_urls=[
	'http://www.shopclues.com/electronic-accessories-8/cameras-18/cameras-special.html?search=1&q1=camera',
	]

	
	def parse (self, response):
		url= response.css("div.products-grid div.grid-product")
		yield ImgData(image_urls=[url.css('img::attr(src)').extract_first()])
		#yield ImgData(image_urls=[url.xpath('img[attr(src)]').extract_first()])








