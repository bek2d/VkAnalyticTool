from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

article_title = []

PATH = "/home/bek/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&salary=355000&only_with_salary=true&text=golang&hhtmFrom=vacancy_search_list")
element = driver.find_element_by_css_selector("a[data-qa='pager-next']")
while True:
    try:
        titles = driver.find_elements_by_css_selector(
            "a[data-qa='vacancy-serp__vacancy-title']")
        for title in titles:
            article_title.append(title.get_attribute("href"))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a[data-qa='pager-next']")))
        next = driver.find_element_by_css_selector(
            "a[data-qa='pager-next']").click()
    except:
        print(article_title)
        break
