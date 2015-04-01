import MySQLdb
from lxml import html
import requests

db = MySQLdb.connect("localhost","pse","pse","product_data" )

cursor = db.cursor()

sql = "select * from priceupdate"
try:
   cursor.execute(sql)
   a=cursor.fetchall()
   for row in a:
   	  id1=row[0]
   	  url=row[1]
   	  email=row[2]
   	  if "flipkart" in url:
   	  	page = requests.get(url)
   	  	tree = html.fromstring(page.text)
   	  	price = tree.xpath('//span[@class="selling-price omniture-field"]/text()')
   	  	price=price[0]
   	  	sql1 = "UPDATE priceupdate SET price = '%s' WHERE id = '%d'" % (price,id1)
   	  	try:
   	  		cursor.execute(sql1)
   	  		db.commit()
   	  	except:
   	  		db.rollback()
   	  elif "snapdeal" in url:
   	  	page = requests.get(url)
   	  	tree = html.fromstring(page.text)
   	  	price = tree.xpath('//span[@itemprop="price"]/text()')
   	  	price=price[0]
   	  	sql1 = "UPDATE priceupdate SET price = '%s' WHERE id = '%d'" % (price,id1)
   	  	try:
   	  		cursor.execute(sql1)
   	  		db.commit()
   	  	except:
   	  		db.rollback()
   	  elif "amazon" in url:
   	  	page = requests.get(url)
   	  	tree = html.fromstring(page.text)
   	  	price = tree.xpath('//span[@id="priceblock_saleprice"]/text()')
   	  	price=price[0]
   	  	sql1 = "UPDATE priceupdate SET price = '%s' WHERE id = '%d'" % (price,id1)
   	  	try:
   	  		cursor.execute(sql1)
   	  		db.commit()
   	  	except:
   	  		db.rollback()
   db.commit()
except:
   db.rollback()
db.close()