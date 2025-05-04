import time
# основной модуль Selenium, используется для запуска браузера (например, webdriver.Chrome()).
from selenium import webdriver
# автоматически скачивает нужную версию ChromeDriver для твоей версии браузера. Упрощает настройку.
from webdriver_manager.chrome import ChromeDriverManager
# Service — указывает путь до ChromeDriver и используется для явного управления процессом драйвера.
from selenium.webdriver.chrome.service import Service
# By — перечисление способов поиска элементов на странице (по ID, XPath, CSS-селектору и др.). Например, By.XPATH.
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Создаём объект options, в который можно добавлять аргументы:
options = webdriver.ChromeOptions()
# Запускаем ChromeDriver, используя путь, автоматически предоставленный ChromeDriverManager.
service = Service(executable_path=ChromeDriverManager().install())
# Запускаем браузер Chrome, передавая в него: service — путь к драйверу options — настройки браузера
driver = webdriver.Chrome( service=service,options=options)