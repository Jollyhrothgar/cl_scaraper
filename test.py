"""
Manage the webdriver
"""
import os
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

chrome_driver = os.path.join(os.getcwd(),"chromedriver")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()

# capture the screen
nowstr = str(datetime.datetime.now())
shotname = "test_successful_{}.png".format(nowstr)
driver.get_screenshot_as_file(shotname)
print("test run successfully! - created screenshot with selnium, {}".format(shotname))
