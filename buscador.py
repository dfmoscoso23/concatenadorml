#scrapeador
import requests
from bs4 import BeautifulSoup
import re

#isbn=9788467022247

def busquedalibro(sku):
		url = "https://www.iberlibro.com/servlet/SearchResults?cm_sp=SearchF-_-topnav-_-Results&ds=20&kn="+str(sku)
		req=requests.get(url)
		soup = BeautifulSoup(req.text, 'lxml')
		lista=soup.find('li', class_='cf result-item')
		titulo=lista.find('meta', itemprop="name")['content']
		preautor=lista.find('meta', itemprop="author")['content']
		preeditorial=lista.find('meta', itemprop="publisher")['content']
		año=lista.find('meta', itemprop="datePublished")['content']
		autor=funerariaautor(preautor)
		editorial=funerariaeditorial(preeditorial)

		return titulo,autor,editorial, año
	

def funerariaautor(autor):
	if re.search(r'\w*, \w*', autor):
		return(autor)
	else:
		autordesarmado=re.sub(r'(\w*) ([\w ]*)',r'\2, \1' , autor)
		return(autordesarmado)
def funerariaeditorial(editorial):
	if re.search(r'\w*, \w*', editorial):
		edi=re.search(r'(\w*), \w*', editorial)
		return(edi[1])
	else:
		return(editorial)