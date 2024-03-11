import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_Path = r"C:\Users\USER\Documents\PYTHON\DOWNLOADS\chromedriver.exe"
s = Service(chrome_driver_Path)
driver = webdriver.Chrome(service = s)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
