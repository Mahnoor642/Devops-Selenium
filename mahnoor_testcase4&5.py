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

#test case 4 add cart

driver.get('http://13.232.10.254/login.php')
driver.maximize_window()


driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('mno@gmail.com')
driver.find_element(By.XPATH,'*//input[@name="password"]').send_keys('mano')
driver.find_element(By.XPATH,'*//input[@value="login now"]').click()

driver.find_element(By.XPATH,'*//a[@href="shop.php"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'*//input[@name="add_to_cart"]').click()


#test case 5 send message


driver.find_element(By.XPATH,'*//a[@href="contact.php"]').click()
time.sleep(2)

driver.find_element(By.XPATH,'*//input[@placeholder="enter your name"]').send_keys('mano')
time.sleep(2)

driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('avc@gmail.com')
time.sleep(2)

driver.find_element(By.XPATH,'*//input[@placeholder="enter your number"]').send_keys('111')

time.sleep(2)

driver.find_element(By.XPATH,'*//textarea[@placeholder="enter your message"]').send_keys('hellow')


time.sleep(2)
driver.find_element(By.XPATH,'*//input[@value="send message"]').click()

