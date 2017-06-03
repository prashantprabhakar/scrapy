from shopclues.items import ImgData
import scrapy
import datetime


class DownloadFirstImg(scrapy.Spider):
	name="DownloadfirstImg"
	start_urls=[
	'http://www.shopclues.com/canon-powershot-sx410-is-2.html',
	]

	def parse (self, response):
		url= response.css("body div.site-container div#container div.ml_containermain div.content-helper div.aside-site-content div.product form#product_form_83013851 div.product-gallery div#product_images_83013851_update div.slide a#det_img_link_83013851_25781870")

		yield scrapy.Request(url.xpath('@href').extract(),self.parse_page)

		def parse_page(self,response):
			for href in response.xpath("//img"):
				yield scrapy.Request(href.xpath("@href").extract(), self.parse_covers)

		def parse_pcovers(self,response):
			imgURl=response.css("body div.site-container div#container div.ml_containermain div.content-helper div.aside-site-content div.product form#product_form_83013851 div.product-gallery div#product_images_83013851_update div.slide a#det_img_link_83013851_25781870::attr(href)").extract()

			yield {
			ImgData(image_urls=[imgURl])
			}










