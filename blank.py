from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Akram Issaoui/Desktop/chromedriver.exe')
driver.get('https://www.linkedin.com')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys('x@gmail.com')
password.send_keys('pass')
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()

#***************** ADD CONTACTS ***********************

#driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=15")
keyword="ceh"
link = "https://www.linkedin.com/search/results/people/?keywords="+keyword+"&origin=SWITCH_SEARCH_VERTICAL"
driver.get(link)
time.sleep(2)


def clicks():
#scroll down to load all the page
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
 all_buttons = driver.find_elements_by_tag_name("button")
 connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
 for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(3)

 time.sleep(10)
 next = driver.find_element_by_xpath("//button[@aria-label='Next']").click()
 time.sleep(6)

clicks()

#scroll down to load all the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
all_buttons2 = driver.find_elements_by_tag_name("button")
connect_buttons2 = [btn for btn in all_buttons2 if btn.text == "Connect"]
for btn in connect_buttons2:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(3)
time.sleep(10)
next = driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(6)


#scroll down to load all the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
all_buttons3 = driver.find_elements_by_tag_name("button")
connect_buttons3 = [btn for btn in all_buttons3 if btn.text == "Connect"]
for btn in connect_buttons3:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(3)    
time.sleep(10)
next = driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(6)


#scroll down to load all the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
all_buttons4 = driver.find_elements_by_tag_name("button")
connect_buttons4 = [btn for btn in all_buttons4 if btn.text == "Connect"]
for btn in connect_buttons4:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(3)       
time.sleep(10)
next = driver.find_element_by_xpath("//button[@aria-label='Next']").click()
time.sleep(6)


#scroll down to load all the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
all_buttons5 = driver.find_elements_by_tag_name("button")
connect_buttons5 = [btn for btn in all_buttons5 if btn.text == "Connect"]

for btn in connect_buttons5:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(3)       
