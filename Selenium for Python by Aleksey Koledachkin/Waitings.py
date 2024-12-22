import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'
#options.add_argument('--no-sandbox')
#options.add_argument('--start-maximized')
#options.add_argument('--headless')
#options.add_argument('--disable-infobars')
#options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--window-size=800,600')
options.add_argument('--disable-cache')
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "Google", "downloads") # Универсальный путь для всех систем
#   "download.default_directory" : f"{os.getcwd()}\Google\downloads"
}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 30)
page = 'https://omayo.blogspot.com/'
driver.get(page)

text_disappear = ("xpath", "//div[@id='deletesuccess']")
wait.until(ec.invisibility_of_element_located(text_disappear), message = "Текст еще не пропал!") # Ждем и проверяем, что текст пропал

text_appearance = ("xpath", "//div[@id='delayedText']")
wait.until(ec.visibility_of_element_located(text_appearance), message = "Текст еще не появился!") # Ждем и проверяем, что текст появился

button_clickable = ("xpath", "//input[@id='timerButton']")
wait.until(ec.element_to_be_clickable(text_appearance), message = "Кнопка не стала кликабельна!") # Ждем и проверяем, что кнопка кликабельна

try_it = ("xpath", "//button[@onclick='setTimeout(myFunctionABC,3000)']")
driver.find_element(*try_it).click()
my_button= ("xpath", "//button[@id='myBtn' and @disabled='']")
wait.until(ec.presence_of_element_located(my_button), message='Элемент так и не стал disabled') # Ждем и проверяем, что кнопка изменила состояние на disabled

driver.quit()