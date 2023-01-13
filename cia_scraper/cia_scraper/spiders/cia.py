import scrapy

# XPath
# Links = //a[starts-with(@href, "collection") and (parent::h3 | parent::h2)]/@href

class SpiderCIA(scrapy.Spider):
    name = 'cia'
    start_urls = ['https://www.cia.gov/readingroom/historical-collections']

    custom_settings = {
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            },
        },
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['oscarbucio2001@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Automaton',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_desclassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3 | parent::h2)]/@href').extract()

        for link in links_desclassified:
            yield response.follow(link, callback=self.parse_link)

    def parse_link(self, response):
        pass