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
        title = response.xpath('//h1/a/text()').get() # Se le pone get para obtener el titulo, ya que solo es uno
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').extract()

        top_tags = response.xpath('//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').extract()

        yield {
            'title': title,
            'quotes': quotes,
            'top_tags': top_tags,
        }