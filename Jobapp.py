 #Import Modules 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Credentials 
# MoussaDiceUser =
# MoussaDicePass = 


#Signing Into Dice :)
driver = webdriver.Chrome()
driver.get("https://www.dice.com/dashboard/login")
email = driver.find_element(By.ID,"email")
email.send_keys("moussamobarak44@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("Bahadur04@0")
Submit = driver.find_element(By.XPATH, '//*[@id="loginDataSubmit"]/div[3]/div/button')
Submit.click()

time.sleep(2)
#Switching to Job page :)
JobPage = driver.find_element(By.XPATH, '/html/body/div[3]/dhi-job-search-bar/div/div/js-search-input/div/form/div/div[3]/button')
JobPage.click()

JobPageWait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="singleCheckbox"]/span/button/i')))

#Selecting Quick Apply :)
EasyApply = driver.find_element(By.XPATH, '//*[@id="singleCheckbox"]/span/button/i')
EasyApply.click()

#Filtering for roles :)
Role = driver.find_element(By.XPATH, '//*[@id="typeaheadInput"]')
Role.send_keys("Azure")
SubmitRole = driver.find_element(By.XPATH, '//*[@id="submitSearch-button"]')
SubmitRole.click() 

#Filtering by Date
Date = driver.find_element(By.XPATH, '//*[@id="facets"]/dhi-accordion[2]/div[2]/div/js-single-select-filter/div/div/button[2]')
Date.click()

#Set Page to 100 Jobs
JobCount = driver.find_element(By.XPATH, '//*[@id="pageSize_2"]')
JobCount.click()

JobCount100 = driver.find_element(By.XPATH, '//*[@id="pageSize_2"]/option[4]')
JobCount100.click()

#itteration for going through jobs


# //*[@id="searchDisplay-div"]/div[3]/dhi-search-cards-widget/div/dhi-search-card[3]
# t = 
# test = '//*[@id="searchDisplay-div"]/div[3]/dhi-search-cards-widget/div/dhi-search-card[{}]'.format(t)

# //*[@id="bea9373d-eba5-4046-813d-d0f34efd07f0"]

# test = driver.find_elements(By.CLASS_NAME, "card-title-link bold viewed")
# print(test) 

job = driver.find_element(By.XPATH, "/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/js-search-display/div/div[3]/dhi-search-cards-widget/div/dhi-search-card[1]/div/div[1]/div/div[2]/div[1]/h5/a")
JobId = print(job.get_attribute('id'))
time.sleep(1000)
driver.get("https://www.dice.com/job-detail/{}".format(JobId))

time.sleep(3)
driver.close()
