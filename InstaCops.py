from selenium import webdriver as sl
from time import sleep
import argparse
import getpass

parser = argparse.ArgumentParser(description='Bot to see users that don\'t follow you back')
parser.add_argument('--usr', help='username', type=str)
parser.add_argument('--pwd', help='Account password', type=str)
args = parser.parse_args()

class instaCops:
    def __init__(self):
        self.driver = sl.Chrome("D:\Drivers\chromedriver.exe")
        self.driver.get("https://instagram.com")
        sleep(2)
        if (args.usr != None and args.pwd != None):
            self.driver.find_element_by_xpath("//input[@name='username']").click()
            sleep(2)
            self.username = self.driver.find_element_by_xpath("//input[@name='username']").send_keys(args.usr)
            self.driver.find_element_by_xpath("//input[@name='password']").click()
            password = driver.find_element_by_xpath("//input[@name='password']").send_keys(args.pwd)
        if(args.usr == None):
            self.username = input("Enter your username: ")
            self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        if(args.pwd == None):
            password = getpass.getpass(prompt="enter your password: ", stream=None)
            self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
       
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click() 

    def get_formatted_username(self,username):
        try:
            index = username.index('@')
            return username[index]
        except:
            return username

    def go_to_profile(self):
        formatted_username = self.get_formatted_username(self.username)
        hyperlink = '/' + formatted_username +'/'
        self.driver.find_element_by_link_text(hyperlink).click()
        sleep(4)

    def find_fake_followers():
       pass

def main():
    instaCop = instaCops()
    instaCop.go_to_profile()

main()