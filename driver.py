from selenium.webdriver.chrome.options import Options
from selenium import webdriver


"""

This module if for creating driver and options for it

"""

def get_driver():
    options = Options()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options)
    return driver
