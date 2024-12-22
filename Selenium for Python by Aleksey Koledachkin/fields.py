import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'
options.add_argument('--no-sandbox')
#options.add_argument("start-maximized")
#options.add_argument('--headless')
#options.add_argument("disable-infobars")
#options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
#options.add_argument("--disable-dev-shm-usage")
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
#options.add_argument("--window-size=800,600")
options.add_argument("--disable-cache")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

page = 'http://the-internet.herokuapp.com/status_codes'
driver.get(page)

time.sleep(5)

list_a = driver.find_elements("xpath", "//ul//a")

for i in list_a:
    i.click()
    time.sleep(5)
    driver.back()
    time.sleep(5)

driver.quit()