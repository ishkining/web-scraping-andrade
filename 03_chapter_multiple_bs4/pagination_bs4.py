from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
movies = f'{root}/movies_letter-A'

response = requests.get(movies)

soup = BeautifulSoup(response.text, 'lxml')

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

for page in range(1, int(last_page) + 1)[:1]:
    url = f'{movies}?page={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    article = soup.find('article', class_='main-article')

    links = []
    for link in article.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            website = f'{root}/{link}'
            response = requests.get(website)
            soup = BeautifulSoup(response.text, 'lxml')

            article = soup.find('article', class_='main-article')
            title = article.find('h1').get_text()
            transcript = article.find('div', class_='full-script').get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print('link not working')

