import time
import pickle
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

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 30)
page = 'https://xn--80ajbvln7ce4bf.xn--p1ai/dlya-bani/pechi-dlya-bani/pechi-dlya-bani-na-drovah/'
driver.get(page)
time.sleep(5)
#ADD_ITEM_BNT = ("xpath", "//button[contains(@class,'14055')]")

ELEMENTS = driver.find_elements("xpath", "//button[contains(@class,'add_to_cart')]")
ELEMENTS[1].click()



page = 'https://лечьнапечь.рф/cart/'
driver.get(page)
pickle.dump(driver.get_cookies(), open(os.path.join(os.getcwd(), 
"Google", "cookies", "cookies_test.pkl"), 
"wb"))
time.sleep(3)
driver.delete_all_cookies()

driver.refresh()

time.sleep(3)

cookies = pickle.load(open(os.path.join(os.getcwd(), 
"Google", "cookies", "cookies_test.pkl"), 
"rb"))
driver.delete_all_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
time.sleep(3)

driver.quit()