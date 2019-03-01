from selenium import webdriver
import time

if __name__ == '__main__':
	browser = webdriver.Chrome('chromedriver.exe')
	browser.get('http://orteil.dashnet.org/cookieclicker/')

	time.sleep(5)
	
	cookie = browser.find_element_by_id('bigCookie')
	products = browser.find_elements_by_class_name('enabled')

	while True:
		cookie.click()

		for product in products:
			try:
				product.click()
			except:
				pass

		products = browser.find_elements_by_class_name('enabled')
