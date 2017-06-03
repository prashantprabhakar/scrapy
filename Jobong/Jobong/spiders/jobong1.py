import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.spider import BaseSpider
from scrapy.http import Request
from Jobong.items import product


# class Product(scrapy.Item):
#     brand=scrapy.Field()
#     title=scrapy.Field()

class aqaqspider(BaseSpider):
    name = "jabong"
    allowed_domains = ["jabong.com"]
    start_urls = [
    "http://www.jabong.com/women/clothing/tops-tees-shirts/tops/?page=1&limit=52&sortField=popularity&sortBy=desc",
]
    page = 1

    def parse(self, response):
        products = response.xpath('//*[@id="catalog-product"]/section[2]/div')
        if not products:
            raise CloseSpider("No more products!")

        for p in products:
            item = product()
            item['price'] = p.xpath('a/div/div[2]/span[@class="standard-price"]/text()').extract()
            #item['img']=p.css('a figure div[2] img::attr(src)').extract()
            item['title'] = p.xpath('a/div/div[1]/text()').extract()
            if item['title']:
                yield item

        self.page += 1
        yield Request(url="http://www.jabong.com/women/clothing/tops-tees-shirts/tops/?page=%d&limit=52&sortField=popularity&sortBy=desc" % self.page,
                  callback=self.parse, 
                  dont_filter=True)  
