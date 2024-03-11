from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_Path = r"C:\Users\USER\Documents\PYTHON\DOWNLOADS\chromedriver.exe"
s= Service(chrome_driver_Path)
driver = webdriver.Chrome(service=s)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("ONAFOWOKAN")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("TESTAMENT")
email = driver.find_element(By.NAME, "email")
email.send_keys("onafowokantestament631@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
button.click()
