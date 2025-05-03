import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



options = webdriver.ChromeOptions()
options.add_argument('--headless') # загрузка страницы без интерфейса
options.add_argument('--incognito') # загрузка страницы в инкогнито
options.add_argument('--ignore-certificate-errors') # загрузка страницы если срок сертификатов закончился
options.add_argument('--window-size=1920x1080') # загрузка страницы с разрешением экрана 1920x1080
options.add_argument('--disable-cache') # отключает кэширование в браузере
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome( service=service,options=options)

driver.get("https://demoqa.com/automation-practice-form")

time.sleep(3)




