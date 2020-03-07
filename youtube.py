from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
class youtube:
    def start_youtube(self,driver):
        driver.get('http://www.youtube.com')
    def search_youtube(self,driver,query):
        driver.find_element_by_id("search").send_keys(query)
        driver.find_element_by_id("video-title").click()
    def playpause(self,driver):
        driver.find_element_by_css_selector("body").send_keys(Keys.SPACE)
    def fvideo(self,driver):
        driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_RIGHT)
    def rvideo(self,driver):
        driver.find_element_by_css_selector('body').send_keys(Keys.ARROW_LEFT)

