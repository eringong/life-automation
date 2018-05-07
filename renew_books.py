from selenium import webdriver
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="user_login",
    help="username for library") 
parser.add_argument("-p", dest="password_login",
    help="password for library") 

args = parser.parse_args()

user_login = args.user_login
password_login = args.password_login

driver = webdriver.Chrome(executable_path="/Users/erin/Desktop/chromedriver")
driver.get("https://rcpl.bibliocommons.com/checkedout/index/coming_due")
time.sleep(3)
user_name = driver.find_element_by_name('name')
user_name.send_keys(user_login)
password = driver.find_element_by_name('user_pin')
password.send_keys(password_login)
login_selector = driver.find_element_by_name('commit')
login_selector.click()
time.sleep(3)
try:
	check_all = driver.find_element_by_class_name('check')
	check_all.click()
	renew = driver.find_element_by_class_name('icon-cw')
	renew.click()
except:
	renew_one = driver.find_element_by_class_name('link_contextual')
	renew_one.click()

time.sleep(1)
print driver.find_element_by_class_name('checkedout_status').text

