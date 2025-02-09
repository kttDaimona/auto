
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Настройка Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
service = Service('D:\prog\chromedriver-win64\chromedriver.exe')  # Укажите путь к chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)  # Используем webdriver из selenium

try:
    # Открытие главной страницы сайта
    driver.get("https://only.digital/")
    time.sleep(3)  # Ожидание загрузки страницы

    # Поиск футера
    footer = driver.find_element(By.TAG_NAME, "footer")
    if footer:
        print("Футер найден.")
    else:
        print("Футер не найден.")
        exit(1)

    # Проверка наличия элементов в футере
    
    try:
        # Пример: проверка наличия ссылки на "Условия использования"
        terms_of_use_link = footer.find_element(By.LINK_TEXT, "Условия использования")
        print("Ссылка на 'Условия использования' найдена.")
    except:
        print("Ссылка на 'Условия использования' не найдена.")

    try:
        # Пример: проверка наличия копирайта
        copyright_text = footer.find_element(By.XPATH, "//*[contains(text(), '©')]")
        print("Копирайт найден.")
    except:
        print("Копирайт не найден.")

finally:
    # Закрытие браузера
    driver.quit()