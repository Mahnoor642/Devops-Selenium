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

driver.get('http://13.232.10.254/login.php')
driver.maximize_window()

#test case 2 admin login
driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('mahnoor@gmail.com')
driver.find_element(By.XPATH,'*//input[@name="password"]').send_keys('tahir123')
driver.find_element(By.XPATH,'*//input[@value="login now"]').click()
#test case 3 delete user
time.sleep(3)
driver.find_element(By.XPATH,'*//a[@href="admin_users.php"]').click()

time.sleep(3)


driver.find_element(By.XPATH,'*//a[@href="admin_users.php?delete=1"]').click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)
