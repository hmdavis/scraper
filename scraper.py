import urllib2 
from bs4 import BeautifulSoup

MAX = 
SEED_URL = 

# make smarter 
def queueLinks(d,url,q):
	try: 
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		for tag in soup.find_all('a'): 
			link = tag.get('href')
			if link in d: 
				d[link] += 1
			else: 
				q.append(link)
				d[link] = 1  	
	except: 
		print 'exception encountered'
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