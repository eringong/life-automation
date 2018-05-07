from selenium import webdriver
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", dest="recipes_to_buy",
    help="list recipes: veggies-and-orzo, grilled-meat-and-veggies, pizza, vegetable-korma, taco-salad-or-soup, ramen, spaghetti, staples, hawaiian-haystacks, pulled-pork, blt, breakfast",
    nargs='+') 
parser.add_argument("-u", dest="user_name",
    help="username for instacart") 
parser.add_argument("-p", dest="password",
    help="password for instacart") 

args = parser.parse_args()

recipe_lookup_dict = {
    "veggies-and-orzo": "7uXwMy4",
    "grilled-meat-and-veggies": "2GTWeHQ",
    "pizza": "Rl3fPuo",
    "vegetable-korma": "mgS7zoc",
    "taco-salad-or-soup": "2HycTrA",
    "ramen": "WxLAKE",
    "spaghetti": "Xpe7fy8",
    "staples": "sBxkQ0U",
    "hawaiian-haystacks": "Ct5NZk8",
    "pulled-pork": "DbvN8EU",
    "blt": "sd4Fbcw",
    "breakfast": "fKiOT4k"
}

def login_to_instacart(user_name, password):
    driver = webdriver.Chrome(executable_path="/Users/erin/Desktop/chromedriver")
    driver.get("https://www.instacart.com/store")
    login_link = driver.find_element_by_link_text('Log in')
    login_link.click()
    email = driver.find_element_by_name('email')
    email.send_keys(user_name)
    password = driver.find_element_by_name('password')
    password.send_keys(password)
    password.submit() 
    return driver

recipes_to_buy = args.recipes_to_buy
stores_to_shop_at = ["costco", "whole-foods"]
user_name = args.user_name
password = args.password

driver = login_to_instacart(user_name, password)
time.sleep(5)
# note, the sleep times below seem to help make sure that items don't get skipped in the add phase in particular
for recipe in recipes_to_buy:
    print "buying for recipe: %s" % recipe
    recipe_key = recipe_lookup_dict[recipe]
    for store in stores_to_shop_at:
        list_url = 'https://www.instacart.com/store/'+store+'/lists/'+recipe_key+'/'+recipe
        driver.get(list_url)
        time.sleep(4)
        add_items = driver.find_elements_by_class_name('instacart-list-product-add')
        print "found %s items to add" % len(add_items)
        time.sleep(4)
        for x in range(0,len(add_items)):
            if add_items[x].is_displayed():
                add_items[x].click()
                time.sleep(4)
        print "finished adding items"