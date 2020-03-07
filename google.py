import time
from selenium.webdriver.common.keys import Keys
class google:
	def start_google(self,driver):
		driver.get('http://google.com')
	def search_google(self,driver,query):
		self.element = driver.find_element_by_name("q")
		self.element.clear()
		self.element.send_keys(query)
		time.sleep(1)
		self.element.send_keys(Keys.RETURN)
		time.sleep(1)
		self.element = driver.find_element_by_class_name('LC20lb').click()




