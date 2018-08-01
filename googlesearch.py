#! python3
#Opens the first five Google search results in different tabs. Search query is supplied in command prompt.

import requests, sys, webbrowser, bs4
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"html.parser")
# Open a browser tab for each result.
linkElems = soup.select('.r a') #returns a list of all the elements that matched your '.r a' selector
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))