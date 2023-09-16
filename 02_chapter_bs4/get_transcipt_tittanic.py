from bs4 import BeautifulSoup
import requests

url = 'https://subslikescript.com/movie/Titanic-120338'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

article = soup.find('article', class_='main-article')
title = article.find('h1').get_text()
transcript = article.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)

print(title)
print(transcript)