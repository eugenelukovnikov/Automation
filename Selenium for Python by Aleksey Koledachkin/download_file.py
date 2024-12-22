import time
import os

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
#options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
#options.add_argument("--window-size=800,600")
options.add_argument("--disable-cache")
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "Google", "downloads") # Универсальный путь для всех систем
#   "download.default_directory" : f"{os.getcwd()}\Google\downloads"
}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

page = 'http://the-internet.herokuapp.com/download'
driver.get(page)

time.sleep(5)

download_files = driver.find_elements("xpath", "//div[@class='example']//a")

# можно скачать как все скопом:
#for i in download_files:
#    i.click()
#    time.sleep(5)

#либо скачать определенный файл:
download_files[1].click()
time.sleep(5)

driver.quit()