import scrapy 

class QuotesSpider(scrapy.Spider):
    name = 'quotes' # Nombre unico con el cual scrapy se va a referir a este spider dentro del proyecto, no es repetible
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        print('*' * 10)
        print('\n\n')
        print(response.status, response.header)
        print('*' * 10)
        print('\n\n')
