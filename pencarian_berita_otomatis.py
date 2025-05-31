import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for item in soup.select('.titleline a')[:5]:
    print(item.text)
