from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
from auth import *
from driver import get_driver

"""

This module is created for first authentification into site and getting cookies.
Don't forget to input your actual logging information into auth.py

"""


def first_auth():
    try:
        driver = get_driver()

        driver.get('https://www.linkedin.com/home')




        login_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "session_key"))
        )
        login_field.send_keys(login)



        password_field = driver.find_element(By.ID, "session_password")
        password_field.send_keys(password)



        password_field.send_keys(Keys.ENTER)


        # Wait for the avatar element to confirm successful login
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "share-box-feed-entry__avatar"))
            )
            print("Logged in. \nDownloading cookie.")
        except Exception as ex:
            return False


        # Save cookies to a file
        pickle.dump(driver.get_cookies(), open("cookies", 'wb'))
        print('Cookie downloaded successfully.')

    except Exception as ex:
        print(ex)




