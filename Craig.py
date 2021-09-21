import scrapy
from scrapy import Request


class CarSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://newyork.craigslist.org/d/appliances/search/ppa/','https://boston.craigslist.org/d/appliances/search/ppa/',
                  'https://washingtondc.craigslist.org/d/appliances/search/ppa','https://orangecounty.craigslist.org/d/appliances/search/ppa'
        ,'https://sandiego.craigslist.org/d/appliances/search/ppa']

    def parse(self, response):
        titles_url = response.xpath('//h3[@class="result-heading"]/a/@href').getall()

        for url in titles_url:
            yield scrapy.Request(url, callback=self.parse_title)

        next_page_url_partial = response.xpath('//a[@class="button next"]/@href').extract_first()
        full_url = self.start_urls[0] + next_page_url_partial
        yield scrapy.Request(full_url, callback=self.parse)

        full_url_1 = self.start_urls[1] + next_page_url_partial
        yield scrapy.Request(full_url_1, callback=self.parse)

        full_url_2 = self.start_urls[2] + next_page_url_partial
        yield scrapy.Request(full_url_2, callback=self.parse)

        full_url_3 = self.start_urls[3] + next_page_url_partial
        yield scrapy.Request(full_url_3, callback=self.parse)

        full_url_4 = self.start_urls[4] + next_page_url_partial
        yield scrapy.Request(full_url_4, callback=self.parse)

    def parse_title(self,response):
        title = response.xpath('//span[@class="postingtitletext"]/span[@id="titletextonly"]/text()').extract_first()
        desc = response.xpath('//section[@id="postingbody"]/text()').extract()

        yield {
            'title':title,
            'desc':desc
        }

