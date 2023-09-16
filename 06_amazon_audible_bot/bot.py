from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import pandas as pd

web_url = 'https://www.audible.com/adblbestsellers?ref=a_search_b1_desktop_footer_column_2_0&pf_rd_p=6a55a63d-48d3-4d5e-857f-ae6682380e4d&pf_rd_r=VTEACM2Y5MKC2ABFGFHZ&pageLoadId=3r1PFvd6v9Lkv0am&creativeId=2d835e86-1f10-4f6e-a4c6-33d2001684e6'

# setting chrome
options = Options()
# options.add_argument('--headless')
# options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=options)
driver.get(web_url)
driver.maximize_window()

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1
book_titles = []
book_authors = []
book_lengths = []

while current_page <= last_page:
    container = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))
    products = WebDriverWait(container, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, './div/span[2]/ul/li/*')))

    for product in products:
        book_titles.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_authors.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_lengths.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    current_page += 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df = pd.DataFrame(
    {
        'title': book_titles,
        'author': book_authors,
        'length': book_lengths
    }
)
df.to_csv('books.csv', index=False)
