import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating'
	source_code = requests.get(url)
	html = source_code.text
	interpret(html)

def interpret(html):
	soup = BeautifulSoup(html, 'html.parser')
	print(soup.title)
	items = soup.find_all('td', {'class': 'titleColumn'})
	print(items)
	d = {}
	for item in items:
		movie_name = item.a.text
		year = item.span.text
		print(movie_name, year)
		if year in d:
			d[year] += 1
		else:
			d[year] = 1
	for key in d:
		print(key, d[key])


if __name__ == '__main__':
	main()