from selenium import webdriver
import os

def login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://vlatka.vertical-life.info/auth/realms/Vertical-Life/protocol/openid-connect/auth?client_id=8a-nu&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fwww.8a.nu%2Fcallback&resource=https%3A%2F%2Fwww.8a.nu&code_challenge=xBL05X4o7XhZ9mN1VGAjfT1HU2baawHrUqYJZT1Vrr4&code_challenge_method=S256')
    driver.find_element_by_id('username').send_keys(os.getenv('_8A_USERNAME'))
    driver.find_element_by_id('password').send_keys(os.getenv('_8A_PASSWORD'))
    driver.find_element_by_id('kc-login').submit()
    driver.find_elements_by_class_name('sign-in')[1].click()
    return driver
