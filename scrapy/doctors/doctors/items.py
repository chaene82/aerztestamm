# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoctorsItem(scrapy.Item):
    # define the fields for your item here like:
    firmaname = scrapy.Field()
    name =  scrapy.Field()
    title = scrapy.Field() 
    discipline = scrapy.Field() 
    email = scrapy.Field()
    tel = scrapy.Field()
    fax = scrapy.Field()
    pass
