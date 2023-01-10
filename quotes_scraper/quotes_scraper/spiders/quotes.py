import scrapy 

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()
# Next Page Button = //ul[@class="pager"]//li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes' # Nombre unico con el cual scrapy se va a referir a este spider dentro del proyecto, no es repetible
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    # Si no se quiere poner en consola la especificación de creación de archivos podemos se puede crear un nuevo atributo 
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
    }


    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').extract()) # Se va a estar llenando cada vez dependiendo si existe o no next_page_button_link por el callback que se manda

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            yield {
                'quotes': quotes
            } # Se regresa ya al final si la validación del next_áge_button_link fue falsa

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get() # Se le pone get para obtener el titulo, ya que solo es uno
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').extract()

        top_tags = response.xpath('//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').extract()

        top = getattr(self, 'top', None) # Se le pasa la instancia self, se busca 'top', si existe se guarda dentro de la variable top si el atributo no existe el resultado será None 
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield {
            'title': title,
            'top_tags': top_tags,
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})