from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://quotes.toscrape.com/')

driver.find_element_by_css_selector('.header-box p a').click()
username = driver.find_element_by_css_selector('#username')
username.send_keys('admin')
time.sleep(3)
password = driver.find_element_by_css_selector('#password')
password.send_keys('password')
time.sleep(3)

driver.find_element_by_css_selector('[value="Login"]').click()

# driver.quit()

while True:

    for div in driver.find_elements_by_css_selector('.quote'):
         print(div.find_element_by_css_selector('.text').text)
         print(div.find_element_by_css_selector('.author').text)
         for tag in div.find_elements_by_css_selector('.tag'):
             print(tag.text)
         print('-------------------')

    try:
        driver.find_element_by_css_selector('.next a').click()
    except:
        print('---------------------')
        print('This is the last page.')
        driver.quit()
        break



# print(type(driver.find_element_by_css_selector('.text')))
# print(driver.find_element_by_css_selector('.text').text)
#
# print('--------------------------------')
#
# print(type(driver.find_elements_by_css_selector('.text')))
#
# for tag in driver.find_elements_by_css_selector('.text'):
#     print(tag.text)


