# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spiders import Spider
from scrapy.selector import Selector

from tutorial.items import BimtoItem

class BimtoSpider(Spider):
    name = "bimto"
    allowed_domains = ["bimto.cn"]
    start_urls = ["http://www.bimto.cn/homepage"]

    def parse(self, response):

        sel = Selector(response)
        divs = sel.xpath('//div[@class="content"]')
        items = []

        try:
            start_request()
        except:
            pass

        for div in divs:
            item = BimtoItem()  
            item['title'] = div.xpath('text()').extract()
            item['link'] = div.xpath('.//@href').extract()
            item['desc'] = div.xpath('.//text()').re('-\s[^\n]*\\r')
            items.append(item)
        
        return items
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)


#    def start_request(self):

#        start_request_with_cookies = Request(url = "http://www.bimto.cn/getFamilyByMenuAjax",
#                                             cookies = [{'pgv_pvi':'7469594624',
#                                                         'JSESSIONID':'4737ED2EEEAD91771E099BF941F37B25',
#                                                         'pgv_si':'s2216630272',
#                                                         'famHistory':'2572e-5403d'}])

#        yield start_request_with_cookies