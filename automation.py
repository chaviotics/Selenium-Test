from selenium import webdriver

chrome_browser = webdriver.Chrome('.\chromedriver.exe') # instance of a chrome browser

chrome_browser.maximize_window()
# print(chrome_browser)