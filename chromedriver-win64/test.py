from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('http://localhost/project/login.php')
driver.maximize_window()

#test case 1
driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('tahir@gmail.com')
driver.find_element(By.XPATH,'*//input[@name="password"]').send_keys('tahir')
driver.find_element(By.XPATH,'*//input[@value="login now"]').click()

#test case 2
time.sleep(3)
driver.find_element(By.XPATH,'*//a[@href="admin_users.php"]').click()

time.sleep(3)


driver.find_element(By.XPATH,'*//a[@href="admin_users.php?delete=4"]').click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)




# #test case 3

# driver.find_element(By.XPATH,'*//a[@href="register.php"]').click()
# driver.find_element(By.XPATH,'*//input[@name="name"]').send_keys('mahnoor')

# driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('mahnoor@gmail.com')

# driver.find_element(By.XPATH,'*//input[@placeholder="enter your password"]').send_keys('mano')
# driver.find_element(By.XPATH,'*//input[@placeholder="confirm your password"]').send_keys('mano')
# time.sleep(2)

# driver.find_element(By.XPATH,'*//input[@value="register now"]').click()


# #test case 4

# driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('mahnoor@gmail.com')
# driver.find_element(By.XPATH,'*//input[@name="password"]').send_keys('mano')
# driver.find_element(By.XPATH,'*//input[@value="login now"]').click()



# driver.find_element(By.XPATH,'*//a[@href="contact.php"]').click()
# time.sleep(2)

# driver.find_element(By.XPATH,'*//input[@placeholder="enter your name"]').send_keys('mahnoor')
# time.sleep(2)

# driver.find_element(By.XPATH,'*//input[@name="email"]').send_keys('mahnoor@gmail.com')
# time.sleep(2)

# driver.find_element(By.XPATH,'*//input[@placeholder="enter your number"]').send_keys('111')

# time.sleep(2)

# driver.find_element(By.XPATH,'*//textarea[@placeholder="enter your message"]').send_keys('hellow')


# time.sleep(2)
# driver.find_element(By.XPATH,'*//input[@value="send message"]').click()




time.sleep(60)

