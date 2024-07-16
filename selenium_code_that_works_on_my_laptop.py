from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)
driver.get('https://www.naver.com/')
