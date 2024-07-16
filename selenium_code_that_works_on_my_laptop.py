from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')# its for maximizing the screen of the website
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)#inside the options=options is the reason why the code works and makes the website stays open
driver.get('https://www.naver.com/')
