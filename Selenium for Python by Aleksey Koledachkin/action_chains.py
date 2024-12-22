import time
import pickle
import os
import platform

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

#PROXY = "77.37.122.227:3128"
options = Options()
options.page_load_strategy = 'eager'
#options.add_argument(f"--proxy-server={PROXY}")
#options.add_argument('--no-sandbox')
#options.add_argument('--start-maximized')
#options.add_argument('--headless')
#options.add_argument('--disable-infobars')
#options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument('--window-size=800,600')
options.add_argument('--disable-cache')
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "Google", "downloads") # Универсальный путь для всех систем
#   "download.default_directory" : f"{os.getcwd()}\Google\downloads"
}
options.add_experimental_option("prefs", preferences)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

wait = WebDriverWait(driver, 30)

action = ActionChains(driver)

page = 'https://demoqa.com/sortable'

driver.get(page)

SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source) # Находим source-элемент
    TARGET = driver.find_element(*target) # Находим target-элемент
    wait.until(ec.element_to_be_clickable(SOURCE)) # Ждем кликабельности source-элемента
    action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскиваем

drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR) # Использование функции
time.sleep(3)

driver.quit()