# items.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item

class LocationsItem(Item):
	# define the fields for your item here like:
	state = Field()
	town = Field()
	address = Field()
	store_number = Field()
