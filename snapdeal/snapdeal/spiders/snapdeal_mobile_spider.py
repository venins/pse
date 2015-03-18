import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from snapdeal.items import SnapdealItem

class snapdeal_spider(CrawlSpider):
    name='snapdeal_mobile'
    allowed_domains = ['snapdeal.com']
    #generating the list of the start url using for loop(start=20*page number)
    start_urls = ["http://www.snapdeal.com/products/mobiles-mobile-phones?sort=plrty&start=%s"%(i*20) for i in range(170)]
    rules = (
        Rule(LinkExtractor(allow=('snapdeal\.com/product/[\w-]+/\d+', )), callback='parse_item'),
    )


    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = SnapdealItem()
        item['product_url'] = response.url
        item['product_name'] = response.xpath('//p[@itemprop="name"]/text()').extract()
        #item['product_tag']=response.xpath('//span[@class="subtitle"]/text()').extract()
        item['product_price'] = response.xpath('//span[@itemprop="price"]/text()').extract()
        return item