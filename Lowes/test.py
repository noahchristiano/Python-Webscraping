# test.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

from lowes_automator import LowesAutomator
import sys
sys.path.append('~/Lowes/locations')
from collector import LocationsCollector

collector = LowesAutomator()

def get_stores():
	stores = []
	collector = LocationsCollector()
	locations  = collector.get_locations()
	for l in locations:
		if l.country != 'Canada':
			stores.append(l)
	return stores

for store in get_stores():
	collector.get_products(store)
