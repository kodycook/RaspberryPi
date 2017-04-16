from selenium import webdriver
import os

# initiate
chromedriver = webdriver.Chrome("C:/Users/maste/Downloads/chromedriver_win32/chromedriver.exe")
#os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver.get("http://stackoverflow.com")

#driver = webdriver.Firefox() # initiate a driver, in this case Firefox
driver.get("https://toolbox3.iinet.net.au/login") # go to the url

# log in
username_field = driver.find_element_by_name("Username") # get the username field
password_field = driver.find_element_by_name("Password") # get the password field
username_field.send_keys("thecooks5@ozemail.com.au") # enter in your username
password_field.send_keys("family5") # enter in your password
password_field.submit() # submit it

# print HTML
html = driver.page_source
print(html)

driver.quit()