from selenium import webdriver as sl
from time import sleep
import argparse

parser = argparse.ArgumentParser(description='Bot to see users that don\'t follow you back')
parser.add_argument('--usr', help='username', type=str, required=True)
parser.add_argument('--pwd', help='Account password', type=str, required=True)
args = parser.parse_args()

class instaCops:
    def __init__(self):
        driver = self.driver
        driver = sl.Chrome("D:\Drivers\chromedriver.exe")
        driver.get("https://instagram.com")
        sleep(2)
        driver.find_element_by_xpath("//input[@name='username']").click()
        sleep(2)
        username = self.driver.find_element_by_xpath("//input[@name='username']").send_keys(args.usr)
        driver.find_element_by_xpath("//input[@name='password']").click()
        password = driver.find_element_by_xpath("//input[@name='password']").send_keys(args.pwd)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)
        driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
   
    def get_formatted_username(username):
        try:
            index = username.index('@')
            return username[index]
        except:
            return username

    def go_to_profile():
        formatted_username = get_formatted_username(username)
        hyperlink = '/' + formatted_username +'/'
        driver.find_element_by_link_text(hyperlink).click()
        sleep(4)

    def find_fake_followers():
       pass