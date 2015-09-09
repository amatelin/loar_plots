# -*- coding: utf-8 -*-

import scrapy

from chemical_elements.items import ChemicalElementItem

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Timeline_of_chemical_element_discoveries"]

    def parse(self, response):
        for selector in response.xpath("//table[contains(@class, 'wikitable')]/tr"):
            item = ChemicalElementItem()
            item["Z"] = selector.xpath("td[1]/text()").extract()
            item["Element"] = selector.xpath("td[2]/a/text()").extract()
            item["Discovery"] = selector.xpath("td[3]/text()").extract()
            item["Discoverer"] = selector.xpath("td[5]/a/text()").extract()
            yield item 
        