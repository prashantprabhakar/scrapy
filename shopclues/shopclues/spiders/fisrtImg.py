import scrapy

class FirstImg(scrapy.Spider):
	name="firstImg"
	start_urls=[
		'http://www.shopclues.com/canon-powershot-sx410-is-2.html',
		   ]

	def parse (self, response):
		for content in response.css("body div.site-container div#container div.ml_containermain div.content-helper div.aside-site-content div.product form#product_form_83013851 div.product-gallery div#product_images_83013851_update div.slide"):
                    
			yield{
				'url': content.css('a#det_img_link_83013851_25781870::attr(href)').extract()
			     }




 
