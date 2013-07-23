import urllib2 
from urlparse import urlparse
from bs4 import BeautifulSoup

MAX = 15
SEED_URL = "http://www.chordials.com" 

def isValidURL(url): 
	pass 

# make smarter 
def queueLinks(d,url,q):
	try: 
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		for tag in soup.find_all('a'): 
			link = tag.get('href')
			domain = urlparse(link).netloc 
			if domain in d:
				d[domain] += 1
			else: 
				q.append(link)
				d[domain] = 1  	
	except: 
		print 'MalformedURL'
	return (d,q)

def crawl(max,seed):
	count = 1   
	domains,queue = queueLinks({},seed,[])

	while (count < max): 
		if len(queue) <= 0: 
			break 
		else: 
			url = queue.pop(0)
			print(str(url))
			domains,queue = queueLinks(domains,url,queue)
			count += 1

	return domains 

crawl(MAX,SEED_URL)