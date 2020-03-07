import time
class facebook:
	username = "8140189833"
	password = "testaccount123"
	def start(self,driver):
		driver.get('http://www.facebook.com')
		obj = driver.find_element_by_name("email")
		#obj.clear()
		obj.send_keys(facebook.username)
		time.sleep(1)
		obj = driver.find_element_by_name("pass")
		obj.send_keys(facebook.password)
		time.sleep(1)
		obj = driver.find_element_by_id('loginbutton').click()
		time.sleep(3)
	def logout(self,driver):
		#self.driver.close()
		self.log = driver.find_element_by_id('userNavigationLabel').click()
		time.sleep(2)
		self.log = driver.find_element_by_xpath("//span[text()='Log Out']").click()
	def profile(self,driver):
		self.log = driver.find_element_by_class_name("_1vp5").click()
	def message(self,driver):
		self.log = driver.find_element_by_xpath('//*[@id="u_0_e"]/a').click()
	def notification(self,driver):
		self.log = driver.find_element_by_xpath('//*[@id="fbNotificationsJewel"]/a/div').click()




	








