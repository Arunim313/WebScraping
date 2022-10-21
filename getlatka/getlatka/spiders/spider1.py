import scrapy


class gtlSpider(scrapy.Spider):
    name = "gtlSpider"

    def start_requests(self):
        urls = ['http://getlatka.com/']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'gtl-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # self.log('Saved file %s' % filename )