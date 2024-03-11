from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import threading
import time
def big_cookie_click_thread():
    while True:
        cookie_button = driver.find_element(By.ID, "bigCookie")
        cookie_button.click()

def click_on_store():
    while True:
        upgrades =driver.find_elements(By.XPATH,'//*[@id="product0"]')
        if upgrades:
            random.choice(upgrades).click()
        products = driver.find_elements(By.XPATH,'//*[@id="product0"]')
        if products:
            products[-1].click()
        time.sleep(5)
chrome_driver_Path = r"C:\Users\USER\Documents\PYTHON\DOWNLOADS\chromedriver.exe"
from selenium.webdriver.chrome.service import Service
s = Service(chrome_driver_Path)
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
time.sleep(5)
language_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]  ")
language_button.click()
close_cookies = driver. find_element(By.XPATH, "/html/body/div[1]/div/a[1]")
time.sleep(3)
close_cookies.click()

click_on_cookies = threading.Thread(target=big_cookie_click_thread)
click_on_cookies.start()
click_on_upgrade = threading.Thread(target= click_on_store)
click_on_upgrade.start()
while True:
    time.sleep(10)
pass
