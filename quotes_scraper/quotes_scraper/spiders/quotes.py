import scrapy 

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()

class QuotesSpider(scrapy.Spider):
    name = 'quotes' # Nombre unico con el cual scrapy se va a referir a este spider dentro del proyecto, no es repetible
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        print('*' * 10)
        print('\n\n\n')
        # print(response.status, response.headers)
        title = response.xpath('//h1/a/text()').get() # Se le pone get para obtener el titulo, ya que solo es uno
        print(f'Titulo: {title}')
        
        print('\n\n')
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').extract()
        print('Citas: ')
        for quote in quotes:
            print(f'- {quote}')
        print('\n\n')
        

        print('\n\n')
        top_tags = response.xpath('//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').extract()
        print('El top 10 de las citas es: ')
        for tag in top_tags:
            print(f'- {tag}')
        print('\n\n')

        print('\n\n\n')
        print('*' * 10)
