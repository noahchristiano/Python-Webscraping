# verifiedArtists.py
# Rap Genius
# Created by Noah Christiano on 8/15/2014.
# noahchristiano@rochester.edu

# -*- coding: utf-8 -*-
import scrapy
from genius.items import Artist

class VerifiedartistsSpider(scrapy.Spider):
	name = "verifiedArtists"
	allowed_domains = ["http://rapgenius.com/verified-artists"]
		#start_urls = ('http://rapgenius.com/verified-artists/' )
	
	def start_requests(self):
		for i in range(1, 75):
			yield  self.make_requests_from_url('http://rapgenius.com/verified-artists?page=' + str(i))
	
	def parse(self, response):
		names = response.xpath('//a[@class="login"]/text()').extract()
		iqs = response.xpath('//a[@class="iq_value"]/text()').extract()
		items = []

		for i in range(0, len(names)):
			item = Artist()
			item['name'] = names[i]
			item['iq'] = iqs[i]
			item['url'] = response.url
			items.append(item)
		
		return items
