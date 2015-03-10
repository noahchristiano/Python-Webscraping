# store.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

class Store():
	country = ''
	state = ''
	town = ''
	address = ''
	store_number = ''

	def set_state(self, string):
		self.state = string
		canada = ['Alberta', 'Ontario', 'British Columbia', 'Saskatchewan']
		if string in canada:
			self.country = 'Canada'
		else:
			self.country = 'United States'
