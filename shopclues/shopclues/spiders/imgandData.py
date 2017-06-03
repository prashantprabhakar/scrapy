from shopclues.items import ImgData
import scrapy


class ImgandData(scrapy.Spider):
	name='imgandData'
	start_urls=['http://www.shopclues.com/canon-powershot-sx410-is-2.html',]

	


	def parse (self, response):

		url= response.css("body div.site-container div#container div.ml_containermain div.content-helper div.aside-site-content div.product form#product_form_83013851 div.product-gallery div#product_images_83013851_update div.slide a#det_img_link_83013851_25781870")
		yield ImgData(image_urls=[url.xpath('@href').extract_first()])
		
		for content in response.css("body div.site-container div.site-content div.product-details-list"):
			yield{
			'description': content.css('p::text').extract()
			}

			