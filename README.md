# Python-Webscraping
Created by Noah Christiano on 8/15/2014.

noahchristiano@rochester.edu

Python Webscraping is a collection of scripts I have written in Python for scraping data off of websites.

Rap Genius uses Selenium and Scrapy to find the top contributing artists from the Rap Genius verified artist page. This project is how I familiarized myself with Scrapy and Selenium (and Python).

Lowes scrapes search result pages into a database using Selenium. It attempts to leverage multiprocessing. This project utilizes the Scrapy, Selenium, Requests, JSON, Multiprocessing, and Sqlite3 libraries. This project was the main reason I delved into web scraping.

Kimsufi scrapes JSON data to determine current availability of servers for lease, then sends a status email. It utilizes JSON and Requests libraries to scrape the Kimsufi website. SMTPlib is used to send the email, notifying you of the server's availability. This project is me doing something useful with my knowledge.
