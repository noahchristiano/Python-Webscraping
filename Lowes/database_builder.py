# database_builder.py
# Lowes
# Created by Noah Christiano on 7/21/2014.
# noahchristiano@rochester.edu

import sqlite3

class DatabaseBuilder():
	
	#initialize database
	def initialize(self):
		conn = sqlite3.connect('pella_lowes.db')
		c = conn.cursor()
		c.execute('CREATE TABLE listings (country text, state text, town text, store_number int, address text, name text, item_number int, model_number int, price money);')
		conn.commit()
		conn.close()
		
	#add a listing to the database
	def add(self, p):
		conn = sqlite3.connect('pella_lowes.db')
		c = conn.cursor()
		product_values = [(p.country, p.state, p.town, p.store_number, p.address, p.name, p.item_number, p.model_number, p.price),]
		c.executemany('INSERT INTO listings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);', product_values)
		conn.commit()
		conn.close()
