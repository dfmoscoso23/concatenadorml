#scrapeador

import pandas as pd
import openpyxl as op
import os
import requests
from bs4 import BeautifulSoup

isbn=9788467022247

def busquedalibro(sku):
		url = "https://www.iberlibro.com/servlet/SearchResults?cm_sp=SearchF-_-topnav-_-Results&ds=20&kn="+str(sku)
		req=requests.get(url)
		soup = BeautifulSoup(req.text, 'lxml')
		itemlista=soup.find('div', class_='listing-item')
		return itemlista
	
print(busquedalibro(isbn))
url = "https://www.iberlibro.com/servlet/SearchResults?cm_sp=SearchF-_-topnav-_-Results&ds=20&kn="+isbn
