# check out on this cheat sheet
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

from selenium import webdriver

chrome_browser = webdriver.Chrome('.\chromedriver.exe') # instance of a chrome browser

# chrome_browser.maximize_window()
# print(chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button =  chrome_browser.find_element_by_class_name("btn-default") # selecting the button
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn') # finds the styling
print(user_button2)

user_message.clear() # makes sure that there's no message
user_message.send_keys("I am Chaviotics!")

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
print(output_message)

assert 'I am Chaviotics!' in output_message.text

# closing the web browsers

chrome_browser.close()