import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome( service=service)

driver.get("https://www.google.co.uk/?pli=1")

time.sleep(5)

driver.back() # Возврат на предыдущую страницу

time.sleep(3)

driver.forward() # Переход на другую страницу
time.sleep(5)
driver.refresh() # обновления страницы
time.sleep(5)