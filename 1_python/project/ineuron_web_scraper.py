import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PATH = r'chromedriver.exe'
USERNAME = input('Enter your username')
PASSWORD = input('Enter your password')
driver = webdriver.Chrome(PATH)
driver.get('https://internship.ineuron.ai/')

sign_in = driver.find_element_by_link_text('Sign In')
sign_in.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email_m'))
    )
    input_tag = driver.find_element_by_name('email_m')
    password_tag = driver.find_element_by_name("password_m")
    sig_in_button = driver.find_element_by_xpath('//button[text()="Sign In"]')

    input_tag.send_keys(USERNAME)
    password_tag.send_keys(PASSWORD)
    password_tag.send_keys(Keys.RETURN)
except Exception as e:
    print('error occured', e)
    driver.quit()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'MuiButton-contained'))
    )
    start_new_project= driver.find_element_by_class_name('MuiButton-contained')
    start_new_project.click()
except Exception as e:
    print(e)


try:
    tech = driver.find_element_by_xpath("//input[@id='project-tech']")
    tech.click()
    driver.execute_script('document.getElementById('dt_a_length')')

except Exception as e:
    print(e)
time.sleep(5)

driver.quit()
