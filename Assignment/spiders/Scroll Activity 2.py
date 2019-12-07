# -*- coding: utf-8 -*-
import json
import scrapy


class ScrollSpider(scrapy.Spider):
    name = 'Scroll'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):

        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'Author': quote['author']['name'],
                'Text': quote['text'],
                'Tags': quote['tags']
                }
        if (data['has_next']):
            next_page = data['page'] + 1
            yield scrapy.Request(url = self.api_url.format(next_page), callback = self.parse)

 
