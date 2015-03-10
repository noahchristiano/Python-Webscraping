# lowes_automator.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from listing import Listing

class LowesAutomator():
	
	driver = None
	
	#prevent the feedback survey from interrupting crawl
	def no_feedback(self):
		pass
	
	#setup selenium webdriver
	def initialize(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://www.lowes.com/Search=pella#!")
		assert "Shop at Lowes.com" in self.driver.title
		self.no_feedback()
	
	#prepare to change store
	def initialize_change_store(self, store):
			store_info_dropdown = self.driver.find_element_by_xpath('//a[@id="nav-store-info"]')
			store_info_dropdown.click()
			current_store_address = self.driver.find_element_by_xpath('//li[@class="store_info_address"]').text
			change = self.driver.find_element_by_xpath('//a[@id="nav-store-change"]')
			change.click()
			loc_field = self.driver.find_element_by_xpath('//input[@id="Header-map-search"]')
			loc_field.clear()
			loc_field.send_keys(store.store_number)
			loc_search = self.driver.find_element_by_xpath('//button[@id="Header-map-search-submit"]')
			loc_search.click()
			
			loading = True
			while loading:
				try:
					loading = self.driver.find_element_by_xpath('//h2[@class="error-title"]').get_attribute('class') != 'error-title'
					print 'Store search error: ' + store.store_number
					return False
				except:
					pass
				try:
					if self.driver.find_element_by_xpath('//span[@class="store-location"]').text != current_store_address:
						return True
				except:
					pass

	#change store
	def change_store(self):
		store = self.driver.find_element_by_xpath('//a[@class="make-store"]')
		store.click()
	
	#search for product
	def product_search(self):
		item_search = self.driver.find_element_by_xpath('//input[@id="Ntt"]')
		item_search.send_keys('pella')
		item_search.send_keys(Keys.RETURN)

	#set page result size to 48
	def view_most_results(self):
		dropdown = None
		try:
			dropdown = self.driver.find_element_by_xpath('//option[@value="48"]')
			dropdown.click()
		except:
			pass

	#get total result pages
	total_result_pages = None
	def set_total_results_pages(self):
		self.view_most_results()
		self.total_result_pages = self.driver.find_element_by_xpath('//span[@class="totalPages"]').text
	
	#make sure item list is done loading
	load_next_check = None
	def itemlist_wait(self):
		loading = True
		while loading:
			try:
				if self.driver.find_element_by_xpath('//ul[@class="productInfo"]/li[@class="last"]').text[9:] != self.load_next_check:
					loading = False
			except:
				pass

	#load the next results page
	def next_results_page(self):
		results_next = self.driver.find_element_by_xpath('//a[@class="nav-control-forward arrow"]')
		results_next.click()
		self.itemlist_wait()

	#returns true if end of result pages
	def end_results(self, total_result_pages):
		if self.driver.find_element_by_xpath('//span[@class="currentPage"]').text == self.total_result_pages:
			return True

	#collect results from one page
	def collect_page_results(self, store):
			names = self.driver.find_elements_by_xpath('//a[@name="listpage_productname"]')
			model_numbers = self.driver.find_elements_by_xpath('//ul[@class="productInfo"]/li[@class="last"]')
			item_numbers = self.driver.find_elements_by_xpath('//ul[@class="productInfo"]/li[not(@class="last")]')
			prices = self.driver.find_elements_by_xpath('//p[@class="pricing"]/strong')
			self.load_next_check = model_numbers[0].text[9:]
			page_results = []
			for i in range(0, len(names)):
				listing = Listing()
				listing.name = names[i].text
				listing.item_number = item_numbers[i].text[8:]
				listing.model_number = model_numbers[i].text[9:]
				listing.price = prices[i].text[1:]
				listing.country = store.country
				listing.state = store.state
				listing.town = store.town
				listing.store_number = store.store_number
				listing.address = store.address
				page_results.append(listing)
			return page_results

	#scrape results from one store
	def collect_store_results(self, store):
		self.set_total_results_pages()
		store_results = []
		end = False
		while not end:
			store_results.extend(self.collect_page_results(store))
			if self.end_results(self.total_result_pages):
				return store_results
			else:
				self.next_results_page()

	#collect results from all stores
	def collect_results(self):
		results = []
		for s in self.stores:
			if self.initialize_change_store(s):
				self.change_store()
				self.product_search()
				results.append(self.collect_store_results(s))
		return results

	#close webdriver
	def close(self):
		self.driver.quit()

	#run various methods for crawling website for products
	def get_products(self, store):
		try:
			self.initialize()
			self.initialize_change_store(store)
			self.change_store()
			self.product_search()
			results = self.collect_store_results(store)
			self.close()
			return results
		except:
			print 'Crash: ' + s.town + ', ' + s.state
			self.close()
			self.get_products(store)
