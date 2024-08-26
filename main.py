import random
import time
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
SIMILAR_ACCOUNT = ['designer__blouse___']
USERNAME = 'roopa.shopping'
PASSWORD = 'pass#'
ALPHABET_LIST = list(string.ascii_lowercase)

class INSTABOT():
    def __init__(self):
        chromeoptions= webdriver.ChromeOptions()
        chromeoptions.add_experimental_option('detach',True)

        self.driver = webdriver.Chrome(options=chromeoptions)
        self.driver.get('https://instagram.com')
        self.popup = None
        self.buttons = []

    def login(self):
        time.sleep(2)
        username_box = self.driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(1) > div > label > input')
        time.sleep(2)
        password_box = self.driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(2) > div > label > input')

        username_box.send_keys(USERNAME)
        password_box.send_keys(PASSWORD)

        time.sleep(2)
        login_button = self.driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3) > button')
        login_button.click()

    def identify_buttons(self):
        self.buttons = []
        self.buttons = self.popup.find_elements(By.TAG_NAME, 'button')[1:]
        for button in self.buttons:
            if button not in self.buttons:
                self.buttons.append(button)
        print(len(self.buttons),self.buttons)


    def follow(self,target):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{target}/followers')
        time.sleep(5)
        self.popup = self.driver.find_element(By.XPATH,'//div[@role="dialog"]')
        # Get all buttons on popup
        search_box = self.driver.find_element(By.XPATH,'//input[@aria-label="Search input"]')
        time.sleep(5)

        def real_follow():
            self.buttons=[]
            self.identify_buttons()
            p=0
            for button in self.buttons:
                number = random.randint(7,10)
                if p > 0 and p % number == 0:
                    time.sleep(10)
                try:
                    button.click()
                    time.sleep(1.5)
                except ElementClickInterceptedException:
                    try:
                        time.sleep(3)
                        print(f'CANCELLING{button}')
                        cancel_button = self.driver.find_element(By.XPATH,"//button[text()='Cancel']")
                        cancel_button.click()
                    except:
                        print('ERROR')
                        pass
                    pass
                p+=1

        for i in ALPHABET_LIST:
            search_box.clear()
            search_box.send_keys(i)
            time.sleep(5)
            real_follow()
instabot = INSTABOT()
instabot.login()
for account in SIMILAR_ACCOUNT:
    instabot.follow(target=account)


# Seems an error where it skipped a account trailing a already followed one
