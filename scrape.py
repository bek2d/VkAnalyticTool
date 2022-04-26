import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
# #command to create a structure of csv file in which we will populate our scraped data
# with open('data.csv', mode='w') as csv_file:
#    fieldnames = ['Title']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()
# #Creating an empty lists of variables
article_title = []

PATH = "/home/bek/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://hh.ru/auth/applicant")


expand = driver.find_element_by_css_selector("button[data-qa='expand-login-by-password']").click()


WebDriverWait(driver, 300).until(EC.invisibility_of_element((By.CSS_SELECTOR, "button[data-qa='account-login-submit']")))

driver.get("https://hh.ru/applicant/favorite_vacancies")


while WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-qa='pager-next']"))):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-qa='vacancy-serp__vacancy-title']")))
    titles = driver.find_elements_by_css_selector("a[data-qa='vacancy-serp__vacancy-title']")
    for title in titles:
        article_title.append(title.text)
    next = driver.find_element_by_css_selector("a[data-qa='pager-next']").click()


print(article_title)