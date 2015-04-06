import MySQLdb
from lxml import html
import requests

db = MySQLdb.connect("localhost","pse","pse","product_data" )

cursor = db.cursor()

sql = "select * from flipkart_mobile"
cursor.execute(sql)
a=cursor.fetchall()
for row in a:
  if row[0]!="" and row[2]!="":
   	id1=row[0]
   	url=row[2]
   	page = requests.get(url)
   	tree = html.fromstring(page.text)
   	price = tree.xpath('//span[@class="selling-price omniture-field"]/text()')
   	if price:
   		price=price[0]
   	sql1 = "UPDATE flipkart_mobile SET product_price = '%s' WHERE product_id = '%d'" % (price,id1)
   	cursor.execute(sql1)
   	db.commit()
   	print "done id id %s" %id1
db.commit()
db.close()