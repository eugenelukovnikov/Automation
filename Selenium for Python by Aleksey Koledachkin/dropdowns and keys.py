import time
import pickle
import os
import platform


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys

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

os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

page = 'https://demoqa.com/select-menu'
driver.get(page)

# for http://the-internet.herokuapp.com/dropdown:
# DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
# DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
# DROPDOWN.select_by_visible_text("Option 2")
# DROPDOWN.select_by_index(1)

# for https://demoqa.com/select-menu:
# DROPDOWN_LOCATOR = ['xpath', '//select[@id="oldSelectMenu"]']
# DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR))
# all_options = DROPDOWN.options
# for option in all_options:
#     time.sleep(1)
    #DROPDOWN.select_by_value(option.get_attribute('value'))
    #DROPDOWN.select_by_visible_text(option.text)
    #DROPDOWN.select_by_index(all_options.index(option))

# Work with Keys in http://the-internet.herokuapp.com/key_presses:
# INPUT_FIELD = ['xpath', '//input[@id="target"]']

# driver.find_element(*INPUT_FIELD).send_keys(Keys.ENTER)
# time.sleep(1)
# driver.find_element(*INPUT_FIELD).send_keys('Hello')
# time.sleep(1)
# driver.find_element(*INPUT_FIELD).send_keys(Keys.BACKSPACE)
# time.sleep(1)
# driver.find_element(*INPUT_FIELD).send_keys(CMD_CTRL +'A')
# time.sleep(1)
# driver.find_element(*INPUT_FIELD).send_keys(Keys.BACKSPACE)
# time.sleep(1)

# for field Select One in https://demoqa.com/select-menu:
# INPUT_FIELD = ['xpath', '//input[@id="react-select-3-input"]']
# driver.find_element(*INPUT_FIELD).send_keys('Other')
# driver.find_element(*INPUT_FIELD).send_keys(Keys.ENTER)
# time.sleep(2)


# for field Select Value in https://demoqa.com/select-menu:
# INPUT_FIELD = ['xpath', '//div[@id="withOptGroup"]']
# driver.find_element(*INPUT_FIELD).click()
# driver.find_element("xpath", "//div[@id='withOptGroup']//div[text()='Another root option']").click()
# time.sleep(3)


# for field Multiselect Drop down in https://demoqa.com/select-menu:
# INPUT_FIELD = ['xpath', '//input[@id="react-select-4-input"]']
# driver.find_element(*INPUT_FIELD).send_keys('Green' + Keys.ENTER)
# time.sleep(3)
# driver.find_element(*INPUT_FIELD).send_keys('Blue' + Keys.ENTER)
# time.sleep(3)
driver.quit()