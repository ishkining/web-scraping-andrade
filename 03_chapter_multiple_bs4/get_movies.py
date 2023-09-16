from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
url = f'{root}/movies'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

article = soup.find('article', class_='main-article')

links = []
for link in article.find_all('a', href=True):
    links.append(link['href'])

for link in links:
    website = f'{root}/{link}'
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'lxml')

    article = soup.find('article', class_='main-article')
    title = article.find('h1').get_text()
    transcript = article.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)