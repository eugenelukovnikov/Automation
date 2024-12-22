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

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

page = 'https://demoqa.com/upload-download'
driver.get(page)

time.sleep(5)

upload_btn = driver.find_element("xpath", "//input[@type='file']")

#upload_btn.send_keys(f"{os.getcwd()}\Google\downloads\Paprika.png")
upload_btn.send_keys(os.path.join(os.getcwd(), "Google", "downloads", "Paprika.png"))

time.sleep(5)

driver.quit()