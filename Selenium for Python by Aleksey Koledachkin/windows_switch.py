import time
import pickle
import os
import platform

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys

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

page_1 = 'https://hyperskill.org/login'
page_2 = 'https://www.avito.ru/'
page_3 = 'https://td-prometey.ru/auth/?register=yes'

driver.get(page_1)
time.sleep(5)
driver.switch_to.new_window('tab')
driver.get(page_2)
driver.switch_to.new_window('tab')
driver.get(page_3)

windows = driver.window_handles
i=0
for window in windows:
    driver.switch_to.window(windows[i])
    print(driver.title)
    i=i+1

driver.switch_to.window(windows[0])
BUTTON = ['xpath', '//button[contains(@class, "btn btn-primary btn-block !p-2")]']
driver.find_element(*BUTTON).click()

time.sleep(5)

driver.switch_to.window(windows[1])
BUTTON = ['xpath', '//button[@data-marker="search-form/submit-button"]']
driver.find_element(*BUTTON).click()

time.sleep(5)

driver.switch_to.window(windows[2])
BUTTON = ['xpath', '//input[@name="Register"]']
driver.find_element(*BUTTON).click()

time.sleep(5)

driver.quit()