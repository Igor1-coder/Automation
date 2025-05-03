import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome( service=service)

driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)
checkbox = driver.find_elements("xpath","//input[@type='checkbox']")
checkbox[0].click()
print ("Первый чекбокс выбран:", checkbox[0].is_selected())

assert checkbox[0].is_selected() == True
time.sleep(2)

checkbox1 = driver.find_elements("xpath","//input[@type='checkbox']")

checkbox[1].click()
print("второй чек бокс", checkbox[1].is_selected())  # is_selected определяем тип элемента
assert checkbox[1].is_selected() == False
time.sleep(2)