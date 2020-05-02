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
            self.username = args.usr
            self.driver.find_element_by_xpath("//input[@name='username']").send_keys(args.usr)
            self.driver.find_element_by_xpath("//input[@name='password']").click()
            password = self.driver.find_element_by_xpath("//input[@name='password']").send_keys(args.pwd)
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
            return username[:index]
        except:
            return username

    def go_to_profile(self):
        formatted_username = self.get_formatted_username(self.username)
        hyperlink = '/' + formatted_username +'/'
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(formatted_username)).click()
        sleep(4)

    def _get_names(self):
       #sleep(1)
       #scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
       #last_ht ,ht = 0, 1
       #while last_ht != ht:
       #    last_ht = ht
       #    sleep(1)
       #    ht = self.driver.execute_script("""arguments[0], scrollTo(0,arguments[0].scrollHeight);
       #                                         return arguments[0].scrollHeight;""", scroll_box)
       links = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]').find_elements_by_tag_name('a')
       names = [name.text for name in links if name.text != ' ']
       self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
       return names

    def find_fake_followers(self):
       self.driver.find_element_by_xpath("//a[contains(@href, 'following')]").click()
       sleep(2)
       following = self._get_names()
       self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]").click()
       sleep(2)
       followers = self._get_names()
       not_following_back = [user for user in following if user not in followers]
       print(not_following_back)

def main():
    instaCop = instaCops()
    instaCop.go_to_profile()
    instaCop.find_fake_followers()
#try:
main()
#pt:
#print("Something went wrong please try again")
#exit()