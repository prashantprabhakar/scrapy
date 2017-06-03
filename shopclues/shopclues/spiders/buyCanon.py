import scrapy

class BuyCanon(scrapy.Spider):
	name="canon"
	start_urls=[
		'http://www.shopclues.com/canon-powershot-sx410-is-2.html',
		   ]

	def parse (self, response):
		for content in response.css("body div.site-container div.site-content div.product-details-list"):
			yield{
				'description': content.css('p::text').extract()
			     }

		for content2 in response.css("body div.site-container div.site-content div.content_block_features div.product-features-list"):
			yield{
				'subheader': content2.css('h3.subheader::text').extract(),
				'section': content2.css('div label::text').extract(),
				'value': content2.css('div span::text').extract(),

			     }





