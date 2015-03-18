import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from amazon.items import AmazonItem

class amazon_spider(CrawlSpider):
    name='amazon_mobile'
    allowed_domains = ['amazon.in']
    #generating the list of the start url using for loop(start=20*page number)
    start_urls = ["http://www.amazon.in/s/?rh=n:976419031,n:!976420031,n:1389401031,n:1389432031&page=%s"%i for i in range(1,77)]
    rules = (
        Rule(LinkExtractor(allow=('amazon\.in/[\w-]+/dp', )), callback='parse_item'),
    )


    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = AmazonItem()
        item['product_url'] = response.url
        item['product_name'] = response.xpath('//span[@id="productTitle"]/text()').extract()
        #item['product_tag']=response.xpath('//span[@class="subtitle"]/text()').extract()
        item['product_price'] = response.xpath('//span[@class="a-color-price"]/text()').extract()
        return item