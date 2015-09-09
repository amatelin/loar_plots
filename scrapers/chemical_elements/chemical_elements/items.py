# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChemicalElementItem(scrapy.Item):
    Z = scrapy.Field()
    Element = scrapy.Field()
    Discovery = scrapy.Field()
    Discoverer = scrapy.Field()
