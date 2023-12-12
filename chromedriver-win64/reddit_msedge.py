from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv
import os
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

x=1
time_delay=5
edge_options = EdgeOptions()
edge_options.use_chromium = True  # Ensure Chromium-based Edge is used
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--detach")
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))  # Your msedgedriver path


output_filename = "output.csv"
count = 1
while os.path.exists(output_filename):
    output_filename = f"output_{count}.csv"
    count += 1

with open(output_filename, 'w', newline='') as csvfile:
    fieldnames = ['Username', 'Password', 'Comment', 'Upvoted','Commented']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()

    with open("Accounts.csv", 'r',encoding='utf-8-sig') as file:
        csvreaders = csv.reader(file, delimiter=':')
        data1 = list(csvreaders)
    for row in data1:
        check_comment=0

        search = data1[x][0].split(',')
        link = data1[1][0].split(',')
        links= link[3]
        print(links)
        username = search[0]
        password = search[1]
        comment = search[2]
        
        driver.get('https://www.reddit.com/login')
        driver.maximize_window()
        time.sleep(time_delay)
        
        try:
            driver.find_element(By.XPATH,'//input[@name="username"]').send_keys(username)
            time.sleep(time_delay)
        except:
            driver.find_element(By.XPATH,'//input[@id="loginUsername"]').send_keys(username)
            time.sleep(time_delay)
            
        try:
            driver.find_element(By.XPATH,'//input[@name="password"]').send_keys(password)
            time.sleep(time_delay)
        except: 
            driver.find_element(By.XPATH,'//input[@id="loginPassword"]').send_keys(password)
            time.sleep(time_delay)
        
        
        
        
        driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        print('Login Successfully!....')
        time.sleep(time_delay)
        url = 'https://'+links
        driver.get(url)
        
        time.sleep(time_delay)
        
        try:
            driver.find_element(By.XPATH,'//button[@aria-label="upvote"]').click()
            print("Upvote Done!....")
        except:
            driver.find_element(By.XPATH,'//i[@class="icon icon-upvote _2Jxk822qXs4DaXwsN7yyHA"]').click()
            print("Upvote Done!....")

    
        time.sleep(time_delay)
        
        if comment!='':
            try:
                driver.find_element(By.XPATH,'//div[@class="_3LuG0YVLLHE2azRNVaKz7O"]').send_keys(comment)
                time.sleep(time_delay)
            except:
                driver.find_element(By.XPATH,'//div[@role="textbox"]').send_keys(comment)
                time.sleep(time_delay)
            driver.find_element(By.XPATH,'//button[@type="submit"]').click()
            print("Comment Done!...")
            check_comment=1
            time.sleep(time_delay)
            
        try:
            driver.find_element(By.XPATH,'//button[@id="USER_DROPDOWN_ID"]').click()
            time.sleep(time_delay)

        except:
            driver.find_element(By.XPATH,'//i[@class="_3x3dhQasGAuYcXVQ02QUzy icon icon-caret_down"]').click()
            time.sleep(time_delay)

        
        try:
            driver.find_element(By.XPATH,'//i[@class="icon icon-logout"]').click()
            print('Logout Successfully!....')
        except:
            driver.find_element(By.XPATH,'//button[@class="_3fbofimxVp_hpVM6I1TGMS GCltVwsXPu5lE-gs4Nucu"]').click()
            print('Logout Successfully!....')
            
        time.sleep(time_delay)
        upvoted='Done'
        
        if check_comment==1:
            commented='Done'
        elif check_comment==0:
            commented='Not'
        
        csvwriter.writerow({'Username':username, 'Password':password, 'Comment':comment, 'Upvoted':upvoted,'Commented':commented})

        time.sleep(time_delay)
        x=x+1
    
driver.quit()

