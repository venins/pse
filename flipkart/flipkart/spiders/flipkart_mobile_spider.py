import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from flipkart.items import FlipkartItem

class flipkart_spider(CrawlSpider):
    name='flipkart_mobile'
    allowed_domains = ['flipkart.com']
    #generating the list of the start url using for loop(start=21*page number)
    start_urls = ["http://www.flipkart.com/mobiles/pr?sid=tyy,4io&start=%s"%(i*21) for i in range(0,75)]
    rules = (
        Rule(LinkExtractor(allow=('flipkart\.com/\w+-[\w-]+/p/', )), callback='parse_item'),
    )


    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = FlipkartItem()
        item['product_url'] = response.url
        item['product_name'] = response.xpath('//h1[@itemprop="name"]/text()').extract()
        item['product_tag']=response.xpath('//span[@class="subtitle"]/text()').extract()
        item['product_price'] = response.xpath('//span[@class="selling-price omniture-field"]/text()').extract()
        return item
