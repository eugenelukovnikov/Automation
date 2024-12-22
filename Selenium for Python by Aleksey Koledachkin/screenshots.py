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
page = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
driver.get(page)
time.sleep(5)

driver.save_screenshot(os.path.join(os.getcwd(), "Google", "screenshots", "screen_1.png"))

driver.quit()