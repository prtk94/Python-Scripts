#NOT COMPLETE
#Opens the first five Amazon.in search results in different tabs. 
#Product search query is supplied in command prompt.

#https://www.amazon.in/s/url=search-alias%3Daps&field-keywords=watches
import requests, sys, webbrowser, bs4
print('Searching on Amazon.in...')
res = requests.get('https://www.amazon.in/s/url=search-alias%3Daps&field-keywords=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")

#linkElems = soup.select("div > div > div > div[class=fee] > span > span > a")
#a-link-normal a-text-normal
#linkElems=soup.findAll('a', attrs={'class': ['a-link-normal', 'a-text-normal']})
print("List has:")
#print(*linkElems, sep='\n***')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	print(linkElems[i].get('href'))
	#webbrowser.open(linkElems[i].get('href'))
