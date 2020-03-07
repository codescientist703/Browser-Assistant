from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
class common:
    def back(self,driver):
        driver.back()
    def forward(self,driver):
        driver.forward()
    def quit(self,driver):
        driver.close()
    def scrolldown(self,driver):
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    def scrollup(self,driver):
        ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
    def refreshpage(self,driver):
        driver.refresh()



