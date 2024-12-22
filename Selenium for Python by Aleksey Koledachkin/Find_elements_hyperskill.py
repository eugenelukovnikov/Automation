import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("start-maximized")
#options.add_argument('--headless')
#options.add_argument("disable-infobars")
#options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
#options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--incognito")
#options.add_argument("--ignore-certificate-errors")
#options.add_argument("--window-size=800,600")
#options.add_argument("--disable-cache")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

page = 'https://hyperskill.org/courses'
driver.get(page)
time.sleep(5)

tabs_all = driver.find_elements('xpath', '//section[contains(@class, "max-lg:py-12")]//a[contains(@class, "active-route")]')

nav_links = driver.find_elements('xpath', '//a[contains(@class, "nav-link")]')

wdywtd = driver.find_elements('xpath', '//a[contains(@click-event-part, "hero_section")]')

select_prjct_headers = driver.find_elements('xpath', '//div[contains(@class, "text-ellipsis")]')


for header in select_prjct_headers:
    print(header.text)




driver.quit()
