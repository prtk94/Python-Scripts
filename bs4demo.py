import bs4,requests,sys
search_query = sys.argv[1:]
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:])+ 'amazon')
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElems = soup.select('.r a')
link1 = requests.get('http://google.com' + linkElems[1].get('href'))
soup2 = bs4.BeautifulSoup(link1.text,"html.parser")
print(soup2)
 

