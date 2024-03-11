from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_Path = r"C:\Users\USER\Documents\PYTHON\DOWNLOADS\chromedriver.exe"
s = Service(chrome_driver_Path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.python.org/")
dict = {}
for i in range(0,5):
    date = driver.find_element(By.XPATH , f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time").text
    print(date)
    name= driver.find_element(By.XPATH , f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a").text
    print(name)
    new_value = {"time":date,"name":name}
    dict[i] = new_value
print(dict)
driver.quit()