from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('http://13.232.10.254/register.php')
driver.maximize_window()

#test case 1 user signup

driver.find_element(By.XPATH,'*//a[@href="register.php"]').click()
driver.find_element(By.XPATH,'*//input[@name="name"]').send_keys('mno')

driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('mno@gmail.com')

driver.find_element(By.XPATH,'*//input[@placeholder="enter your password"]').send_keys('mano')
driver.find_element(By.XPATH,'*//input[@placeholder="confirm your password"]').send_keys('mano')
time.sleep(2)

driver.find_element(By.XPATH,'*//input[@value="register now"]').click()
