import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

useremail = input("Введите email пользователя, который хотите добавить:")

driver = webdriver.Firefox()

# write  printer's IP instead "IP_printer"
driver.get("https://IP_printer/hp/device/SignIn/Index")

passwordfield = driver.find_element(By.ID, 'PasswordTextBox')

# write password fo printer instead "Password_for_admin"
passwordfield.send_keys("Password_for_admin")

enterfield = driver.find_element(By.ID, 'signInOk')
enterfield.click()
scanfield = driver.find_element(By.ID, 'SendPages')
scanfield.click()
time.sleep(3)
contactfield = driver.find_element(By.ID, 'AddressBook')
contactfield.click()
addcontactfield = driver.find_element(By.ID, 'DeviceContactAddContactButton')
addcontactfield.click()
emailfield = driver.find_element(By.ID, 'Email')
emailfield.send_keys(useremail)
displaynamefield = driver.find_element(By.ID, 'DisplayName')
displaynamefield.send_keys(useremail)
okfield = driver.find_element(By.ID, 'FormButtonSubmit')
okfield.click()
#driver.close()

print("Добавлено на 1-ую МФУ")

time.sleep(4)

# write  printer's IP instead "IP_printer"
driver.get("https://IP_printer/hp/device/SignIn/Index")
passwordfield = driver.find_element(By.ID, 'PasswordTextBox')

# write password fo printer instead "Password_for_admin"
passwordfield.send_keys("Password_for_admin")

enterfield = driver.find_element(By.ID, 'signInOk')
enterfield.click()
scanfield = driver.find_element(By.ID, 'SendPages')
scanfield.click()
time.sleep(3)
contactfield = driver.find_element(By.ID, 'AddressBook')
contactfield.click()
addcontactfield = driver.find_element(By.ID, 'DeviceContactAddContactButton')
addcontactfield.click()
emailfield = driver.find_element(By.ID, 'Email')
emailfield.send_keys(useremail)
displaynamefield = driver.find_element(By.ID, 'DisplayName')
displaynamefield.send_keys(useremail)
okfield = driver.find_element(By.ID, 'FormButtonSubmit')
okfield.click()

print("Добавлено на 2-ую МФУ")