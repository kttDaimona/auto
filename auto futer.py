
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  
service = Service('D:\prog\chromedriver-win64\chromedriver.exe')  
driver = webdriver.Chrome(service=service, options=chrome_options)  
try:
    driver.get("https://only.digital/")
    time.sleep(3)  

    footer = driver.find_element(By.TAG_NAME, "footer")
    if footer:
        print("Футер найден.")
    else:
        print("Футер не найден.")
        exit(1)

    try:
        terms_of_use_link = footer.find_element(By.LINK_TEXT, "Условия использования")
        print(" 'Условия использования' найдена.")
    except:
        print(" 'Условия использования' не найдена.")

    try:
        copyright_text = footer.find_element(By.XPATH, "//*[contains(text(), '©')]")
        print("Копирайт найден.")
    except:
        print("Копирайт не найден.")

finally:
    driver.quit()