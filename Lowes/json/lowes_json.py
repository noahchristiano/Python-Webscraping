# lowes_json.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

import requests
import json
import re

#url = "http://www.lowes.com/IntegrationServices/resources/storeLocator/json/v2_0/stores?place=00001&count=50"
#data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.get(url, data=json.dumps(data), headers=headers)

#http://www.lowes.com/IntegrationServices/resources/storeLocator/json/v2_0/stores?langId=-1&storeId=10702&catalogId=10051&place=98164&count=1

class LowesJson():

	def file_len(self):
		f = open('store_numbers.txt')
		i = 0
		for line in f:
			i = i + 1
		f.close()
		return i

	def get_stores(self, num):
		try:
			r = requests.get('http://www.lowes.com/IntegrationServices/resources/storeLocator/json/v2_0/stores?place=' + "%05d" % num + '&count=50')
			store_numbers = []
			for n in re.finditer('"KEY":', r.text):
				store_numbers.append(r.text[n.end()+1:n.end()+5])
			return store_numbers
		except:
			return None
