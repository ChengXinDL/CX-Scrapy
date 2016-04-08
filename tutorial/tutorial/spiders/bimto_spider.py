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
        divs = sel.xpath('//div[@class="content"]')
        items = []

        for div in divs:
            item = BimtoItem()
            item['title'] = div.xpath('./div[@class="cc"]/ul/li/a[@class="pic_title_p"]/p/text()').extract()
            item['link'] = div.xpath('./div[@class="cc"]/ul[@class="pic_list"]/li/a/@href').extract()

            #item['title'] = div.xpath('./div[@class="lc"]/ul/li/ul[@class="submenu"]/li/a/text()').extract()
            items.append(item)

        return items

        #url_ajax = ['http://www.bimto.cn/loadFamilyAjax']
        #return scrapy.Request(url_ajax, meta={'cookiejar'}, callback=self.parse)

        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
            