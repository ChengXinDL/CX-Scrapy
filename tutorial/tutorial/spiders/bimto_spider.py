# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.selector import Selector

from tutorial.items import BimtoItem

class DmozSpider(scrapy.spiders.Spider):
    name = "bimto"
    allowed_domains = ["www.bimto.cn"]
    start_urls = ["http://www.bimto.cn/homepage"]

    def parse(self, response):

        sel = Selector(response)
        divs = sel.xpath('//div[contains(@class,"cc")]')
        items = []

        for div in divs:
            item = BimtoItem()
            item['title'] = div.xpath('.//ul/li').extract()
            items.append(item)
        
        return items
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)