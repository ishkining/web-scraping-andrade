from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd

website_url = 'https://www.adamchoi.co.uk/overs/detailed'

driver = webdriver.Chrome()
driver.get(website_url)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

sleep(3)

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
scores = []
opponent_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    scores.append(match.find_element(By.XPATH, './td[3]').text)
    opponent_team.append(match.find_element(By.XPATH, './td[4]').text)
driver.quit()

df = pd.DataFrame(
    {'date': date,
     'home_team': home_team,
     'scores': scores,
     'opponent_team': opponent_team
     }
)
df.to_csv('football_data.csv', index=False)
