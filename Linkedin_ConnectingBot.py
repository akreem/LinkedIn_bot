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


keyword="ux"
link = "https://www.linkedin.com/search/results/people/?keywords=ux&origin=SWITCH_SEARCH_VERTICAL&page=13&sid=%3BE~"
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

num_pages=4
for _ in range(num_pages):
  clicks()


