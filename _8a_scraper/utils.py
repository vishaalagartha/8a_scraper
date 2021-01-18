import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(
        '--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=1280,800")
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://www.8a.nu/')
    driver.find_element_by_link_text('Log in').click()
    driver.find_element_by_id('username').send_keys(os.getenv('_8A_USERNAME'))
    driver.find_element_by_id('password').send_keys(os.getenv('_8A_PASSWORD'))
    driver.find_element_by_id('kc-login').submit()
    return driver
