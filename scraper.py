import urllib2 
import threading 
from urlparse import urlparse
from bs4 import BeautifulSoup

MAX = 50
SEED_URL = "http://www.reddit.com"  

def getImages(page): 
	pass 

def queueLinks(cache,page,q):
	soup = BeautifulSoup(page)
	for tag in soup.find_all('a'): 
		url = tag.get('href')
		try:
			domain = urlparse(url).netloc 
			if domain in cache:
				cache[domain] += 1
			else: 
				q.append(url)
				cache[domain] = 1
		except: 
			continue    	
	return (cache,q)

def crawl(max,seed):
	count = 1  
	page = urllib2.urlopen(seed).read()
	cache,queue = queueLinks({},page,[])
	while (count <= max): 
		if len(queue) <= 0: 
			break 
		else: 
			url = queue.pop(0)
			try:
				response = urllib2.urlopen(url)
				page = response.read()
				print count, "\t", response.code, ": ", str(url)
				cache,queue = queueLinks(cache,page,queue)
				count += 1
			except:				
				domain = urlparse(url).netloc
				if cache[domain] == 1: del cache[domain]
	return cache 

c = crawl(MAX,SEED_URL)
