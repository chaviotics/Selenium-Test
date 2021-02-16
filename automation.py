# check out on this cheat sheet
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

from selenium import webdriver

chrome_browser = webdriver.Chrome('.\chromedriver.exe') # instance of a chrome browser

# chrome_browser.maximize_window()
# print(chrome_browser)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

button =  chrome_browser.find_element_by_class_name("btn-default")
print(button.get_attribute('innerHTML'))
