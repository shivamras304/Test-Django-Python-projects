import requests
from bs4 import BeautifulSoup as BS

url = 'https://news.ycombinator.com/'

r = requests.get(url)
html = r.text

soup = BS(html, "html.parser")

tbody = soup.find_all('tr', 'athing')

for x in range(len(tbody)):
	a = tbody[x].find_all('a','storylink')
	print x+1, "---", a[0].text