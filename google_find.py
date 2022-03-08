from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(r"C:\Users\pando\Desktop\python_automation\chromedriver.exe", options=options)
driver.implicitly_wait(10)
driver.get("https://www.google.com")

text_box = driver.find_element_by_name("q")
text_box.send_keys("株式会社ヘルスベイシス")
text_box.submit()
driver.implicitly_wait(10)


address = driver.find_element_by_xpath("//div[@class='BOu6vf']/span")
print(address.text)