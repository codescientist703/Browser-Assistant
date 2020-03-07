from facebook import facebook
from common import common
from youtube import youtube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver.exe',options=options)
driver.maximize_window()
PROMPT_LIMIT = 5
youtube().start_youtube(driver)
youtube().search_youtube(driver,"haha")