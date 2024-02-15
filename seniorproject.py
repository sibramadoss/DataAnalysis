from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
browser.maximize_window()
browser.get('http://reddit.com/')


