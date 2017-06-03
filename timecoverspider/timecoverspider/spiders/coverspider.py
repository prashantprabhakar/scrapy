# import the necessary packages
from timecoverspider.items import MagazineCover
import datetime
import scrapy
 
class CoverSpider(scrapy.Spider):
	name = "pyimagesearch-cover-spider"
	start_urls = ["http://content.time.com/time/coversearch/"] 

def parse(self, response):
		# let's only gather Time U.S. magazine covers
		url=response.css("body div#archiveMain section.sec-content div.editions-issues ul.ul-covers li h3").extract_first()
		yield scrapy.Request(url.css("a::attr(href)").extract_first(), self.parse_page)