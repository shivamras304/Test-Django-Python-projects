import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.producthunt.com/'

r = requests.get(url)
html = r.text

soup = BS(html, "html.parser")

ul = soup.find_all('ul', 'postsList_3n2Ck')
headers_all = soup.find_all('span', 'title_viAcO featured_2PenR default_25TkV base_3LqBu')

for x in range(len(headers_all)):
	print headers_all[x].text
	print ''

	print len(ul)
	span_titles = ul[0].find_all('span', 'title_24w6f featured_2PenR default__25TkV base_3LqBu')

	span_subtitles = ul[0].find_all('span', 'text_quJvV subtle_fyrho base_3LqBu')

	for y in range(len(span_titles)):
		print y+1, '---', span_titles[y].text
		print span_subtitles[y].text
		print ''



# for x in range(len(tbody)):
# 	a = tbody[x].find_all('a','storylink')
# 	print x+1, "---", a[0].text
