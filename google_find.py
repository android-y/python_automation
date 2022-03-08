from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

CHROMEDRIVER = r"C:\Users\pando\Desktop\python_automation\chromedriver.exe"

options = webdriver.ChromeOptions()
# options.add_argument("--headless")

chrome_service = fs.Service(executable_path= CHROMEDRIVER)
driver = webdriver.Chrome(service= chrome_service)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")

text_box = driver.find_element(by=By.NAME, value="q")
text_box.send_keys("株式会社ヘルスベイシス")
text_box.submit()
driver.implicitly_wait(10)

"//*[@class='LrzXr']/span"
address = driver.find_element(by=By.CLASS_NAME, value="LrzXr")
print(address.text)