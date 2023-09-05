from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

############Test 1 ####################
#give credentials
size = "1650"
bedroom = "3"
#get the website
driver.get("http://127.0.0.1:5000")
time.sleep(3)
#find the input text boxes
driver.find_element("id", "fnum").send_keys(size)
time.sleep(3)
driver.find_element("id", "lnum").send_keys(bedroom)
time.sleep(3)
#click the predict button
driver.find_element( "xpath",  "/html/body/form/strong/strong/button").click()
time.sleep(5)




###############Test 2 ############################
size = "A"
bedroom = "A"
driver.get("http://127.0.0.1:5000")
time.sleep(3)
driver.find_element("id", "fnum").send_keys(size)
time.sleep(3)
driver.find_element("id", "lnum").send_keys(bedroom)
time.sleep(3)
driver.find_element( "xpath",  "/html/body/form/strong/strong/button").click()
time.sleep(5)

###############Test 3 ############################
size = ""
bedroom = ""
driver.get("http://127.0.0.1:5000")
time.sleep(3)
driver.find_element("id", "fnum").send_keys(size)
time.sleep(3)
driver.find_element("id", "lnum").send_keys(bedroom)
time.sleep(3)
driver.find_element( "xpath",  "/html/body/form/strong/strong/button").click()
time.sleep(5)

###############Test 4 ############################
size = "1500"
bedroom = "2"
driver.get("http://127.0.0.1:5000")
time.sleep(3)
driver.find_element("id", "fnum").send_keys(size)
time.sleep(3)
driver.find_element("id", "lnum").send_keys(bedroom)
time.sleep(3)
driver.find_element( "xpath",  "/html/body/form/strong/strong/button").click()
time.sleep(5)


driver.close()