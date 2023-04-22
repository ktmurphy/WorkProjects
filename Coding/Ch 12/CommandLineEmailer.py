#! python3
#login to Outlook


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

recipient = input('Enter email address: ')
message = input('message: ')


browser = webdriver.Firefox()
browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1668518973&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fn1p%3d1%252c1%26nlp%3d1%26RpsCsrfState%3d381ad5f5-c542-d749-185d-271b5d69cac6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
wait = WebDriverWait(browser, 30)
userNameElem = wait.until(EC.presence_of_element_located((By.NAME, 'loginfmt')))
print(type(userNameElem))
userNameElem.send_keys('email')

nextElem = wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
nextElem.click()
time.sleep(1)
passwordElem = wait.until(EC.presence_of_element_located((By.NAME, 'passwd')))
passwordElem.send_keys("password")

nextElem = wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
nextElem.click()


''' #the following is not working right
time.sleep(1)
signInQ = wait.until(EC.element_to_be_clickable((By.ID, 'idBtn_Back')))
signInQ.click()
#time.sleep(12)
openEmail = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'New mail')))
openEmail.click()
time.sleep(3)
address = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'VbY1P')))
address.send_keys(recipient)
time.sleep(1)
address.send_keys(Keys.ENTER)

subject = nextElem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'field-422')))
subject.send_keys("New Message")
time.sleep(1)

messageElem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'elementToProof')))
messageElem.send_keys(message)
time.sleep(1)

'''

