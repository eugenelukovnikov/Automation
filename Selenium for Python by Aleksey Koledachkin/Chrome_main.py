from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service

#service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
#service = webdriver.ChromeService(port=1234)
#driver = webdriver.Chrome(service=service)


#рабочий варик:

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

driver.get('https://google.com')
html = driver.page_source
driver.quit()
print(html.count('o3j99'))
