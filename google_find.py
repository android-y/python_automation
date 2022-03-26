from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

CHROMEDRIVER = r"C:\Users\pando\Desktop\python_automation\chromedriver.exe"

def google_find_func(cam):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    chrome_service = fs.Service(executable_path= CHROMEDRIVER)
    driver = webdriver.Chrome(service= chrome_service, options= options)
    driver.implicitly_wait(10)
        
    driver.get("https://www.google.com/")
    text_box = driver.find_element(by=By.NAME, value="q")
    text_box.send_keys(cam)
    text_box.submit()
    driver.implicitly_wait(10)
    
    alists = driver.find_elements(by=By.XPATH, value="//*[@id='rso']/div[1]")
    # print(alists)
    for i in alists:
        if len(i.find_elements(by=By.TAG_NAME, value="h3")) > 0:
            company_name = i.find_elements(by=By.TAG_NAME, value="h3")[0].text
        else:
            company_name = None
        
        if len(i.find_elements(by=By.CLASS_NAME, value="IsZvec")) > 0:
            company_overview = i.find_elements(by=By.CLASS_NAME, value="IsZvec")[0].text
        else:
            company_overview = None

        if len(i.find_elements(by=By.CLASS_NAME, value="yuRUbf")) > 0:
            company_link = i.find_element(by=By.CLASS_NAME, value="yuRUbf").find_element(by=By.TAG_NAME, value='a').get_attribute('href')
        else:
            company_link = None
            
        pre_result_list = [company_name, company_overview, company_link]
    
    driver.quit()    
    return pre_result_list
   

if __name__ == "__main__":
    google_find_func()