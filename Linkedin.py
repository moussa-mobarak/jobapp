#import mod
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#cred
MoussaUsername = "moussamobarak@gmail.com"
MoussaPassword = "Bahadur04@0!"

#Logging into linkedin
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/")
email =  driver.find_element(By.ID,"session_key")
email.send_keys(MoussaUsername)
password = driver.find_element(By.ID,"session_password")
password.send_keys(MoussaPassword)
Signin = driver.find_element(By.CSS_SELECTOR,'button[data-id="sign-in-form__submit-btn"]')
Signin.click()

Jobtitle = 'Azure'

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=&f_AL=true&f_TPR=r86400&f_WT=2&keywords={}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R".format(Jobtitle))

#selecting jobs
JobIDs = []
time.sleep(10)
for i in range(1,25):
    try:
        Jobwait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[25]/div/div[1]/div[1]/div[2]/div[1]/a')))
        Jobfind = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[{}]/div/div[1]/div[1]/div[2]/div[1]/a'.format(i))
        Job = Jobfind.get_attribute('href')
        JobIDs.append(Job)  
    except:
	    print("path not valid")

print(JobIDs)

# Jobfind.click /html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[3]/div/div[1]/div[1]/div[2]/div[1]/a
# time.sleep (100)
# Easyapp =  driver.find_element(By.CSS_SELECTOR,'spam[class="artdeco-button__text"]')
# Easyapp.click
# /html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[1]/div/div[1]/div[1]/div[2]/div[1]/a
# /html/body/div[5]/div[3]/div[4]/div/div/main/div/div[1]/div/ul/li[25]/div/div[1]/div[1]/div[2]/div[1]/a

time.sleep(1000)
driver.close
