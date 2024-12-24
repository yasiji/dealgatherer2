import scrapy

class DealsSpider(scrapy.Spider):
    name = 'deals'
    start_urls = ['https://www.amazon.com/s?k=RTX+4060&crid=3EX9DYJ6QEXBH&sprefix=rtx+4060%2Caps%2C176&ref=nb_sb_noss_1']

    def parse(self, response):
        for deal in response.css('.s-main-slot .s-result-item'):
            product_name = deal.css('div.puis-padding-right-small h2 span::text').get()
            price = deal.css('span.a-offscreen::text').get()
            link = deal.css('a.a-link-normal.s-line-clamp-2::attr(href)').get()

            # Log for debugging
            self.logger.info(f"Product: {product_name}, Price: {price}, Link: {link}")

            # Yield only if product_name is not None
            if product_name and price:
                yield {
                    'product_name': product_name.strip(),
                    'price': price.strip(),
                    'retailer': 'Amazon',
                    'link': response.urljoin(link.strip()) if link else None,
                }
            # Handle pagination
            next_page = response.css('.s-pagination-next::attr(href)').get()
            if next_page:
                yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)   
                