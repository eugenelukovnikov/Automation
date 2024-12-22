import time
import pickle
import os


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

page = 'https://demoqa.com/selectable'
driver.get(page)

grid = ["xpath","//a[@id='demo-tab-grid']"]
driver.find_element(*grid).click()
time.sleep(3)


one = ["xpath", "//li[text()='One']"]
two = ["xpath", "//li[text()='Two']"]
three = ["xpath", "//li[text()='Three']"]
four = ["xpath", "//li[text()='Four']"]
five = ["xpath", "//li[text()='Five']"]
six = ["xpath", "//li[text()='Six']"]
seven = ["xpath", "//li[text()='Seven']"]
eight = ["xpath", "//li[text()='Eight']"]
nine = ["xpath", "//li[text()='Nine']"]

driver.find_element(*one).click()
driver.find_element(*two).click()
driver.find_element(*three).click()
driver.find_element(*four).click()
driver.find_element(*five).click()
driver.find_element(*six).click()
driver.find_element(*seven).click()
driver.find_element(*eight).click()
driver.find_element(*nine).click()

if ("active" in driver.find_element(*one).get_attribute("class")):
    print("Element 'One' is active now")
else:
    print("Element 'One' is not active now")

if ("active" in driver.find_element(*two).get_attribute("class")):
    print("Element 'Two' is active now")
else:
    print("Element 'Two' is not active now")

if ("active" in driver.find_element(*three).get_attribute("class")):
    print("Element 'Three' is active now")
else:
    print("Element 'Three' is not active now")

if ("active" in driver.find_element(*four).get_attribute("class")):
    print("Element 'Four' is active now")
else:
    print("Element 'Four' is not active now")

if ("active" in driver.find_element(*five).get_attribute("class")):
    print("Element 'Five' is active now")
else:
    print("Element 'Five' is not active now")

if ("active" in driver.find_element(*six).get_attribute("class")):
    print("Element 'Six' is active now")
else:
    print("Element 'Six' is not active now")

if ("active" in driver.find_element(*seven).get_attribute("class")):
    print("Element 'Seven' is active now")
else:
    print("Element 'Seven' is not active now")

if ("active" in driver.find_element(*eight).get_attribute("class")):
    print("Element 'Eight' is active now")
else:
    print("Element 'Eight' is not active now")

if ("active" in driver.find_element(*nine).get_attribute("class")):
    print("Element 'Nine' is active now")
else:
    print("Element 'Nine' is not active now")

print("")
time.sleep(3)

driver.find_element(*nine).click()
driver.find_element(*eight).click()
driver.find_element(*seven).click()
driver.find_element(*six).click()
driver.find_element(*five).click()
driver.find_element(*four).click()
driver.find_element(*three).click()
driver.find_element(*two).click()
driver.find_element(*one).click()


if ("active" in driver.find_element(*one).get_attribute("class")):
    print("Element 'One' is active now")
else:
    print("Element 'One' is not active now")

if ("active" in driver.find_element(*two).get_attribute("class")):
    print("Element 'Two' is active now")
else:
    print("Element 'Two' is not active now")

if ("active" in driver.find_element(*three).get_attribute("class")):
    print("Element 'Three' is active now")
else:
    print("Element 'Three' is not active now")

if ("active" in driver.find_element(*four).get_attribute("class")):
    print("Element 'Four' is active now")
else:
    print("Element 'Four' is not active now")

if ("active" in driver.find_element(*five).get_attribute("class")):
    print("Element 'Five' is active now")
else:
    print("Element 'Five' is not active now")

if ("active" in driver.find_element(*six).get_attribute("class")):
    print("Element 'Six' is active now")
else:
    print("Element 'Six' is not active now")

if ("active" in driver.find_element(*seven).get_attribute("class")):
    print("Element 'Seven' is active now")
else:
    print("Element 'Seven' is not active now")

if ("active" in driver.find_element(*eight).get_attribute("class")):
    print("Element 'Eight' is active now")
else:
    print("Element 'Eight' is not active now")

if ("active" in driver.find_element(*nine).get_attribute("class")):
    print("Element 'Nine' is active now")
else:
    print("Element 'Nine' is not active now")

time.sleep(3)

driver.quit()



