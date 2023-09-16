from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

website_url = 'https://twitter.com/home?lang=en'
email = ''
password = ''

driver = webdriver.Chrome()
driver.get(website_url)


def web_driver_wait(driver, path: str):
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, path)))


cookie_button = web_driver_wait(driver, '//div[@role="button"][1]').click()
login = web_driver_wait(driver, '//a[@href="/login"]').click()
sleep(5)
input_email = web_driver_wait(driver, '//input')
input_email.send_keys(email)
web_driver_wait(driver, '//div[contains(@dir, "ltr") and (@style="color: rgb(255, 255, 255);")][1]').click()

input_password = web_driver_wait(driver, '//input[@name="password"]')
input_password.send_keys(password)
web_driver_wait(driver, '//div[contains(@dir, "ltr") and (@style="color: rgb(255, 255, 255);")][1]').click()

sleep(10)
driver.quit()
