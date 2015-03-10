# settings.py
# Rap Genius
# Created by Noah Christiano on 8/15/2014.
# noahchristiano@rochester.edu

# -*- coding: utf-8 -*-

# Scrapy settings for genius project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'genius'

SPIDER_MODULES = ['genius.spiders']
NEWSPIDER_MODULE = 'genius.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'genius (+http://www.yourdomain.com)'
