import scrapy

class QuotesSpider(scrapy.Spider): # En esta clase se va a definir toda la lógica para traer toda la información que queremos desde internet
    name = 'quotes'
    start_urls = [ # Lista de urls donde se ponen las direcciones a donde quiero apuntar
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response): # Método más especial, define la lógica a partir de la cual extraemos información, response se refiere a la respuesta HTTP
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
