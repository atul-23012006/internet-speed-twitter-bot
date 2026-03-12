from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        # Accept cookies if popup appears
        try:
            accept = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept.click()
            time.sleep(2)
        except:
            pass

        start = self.driver.find_element(By.CLASS_NAME, "start-text")
        start.click()

        time.sleep(60)

        self.down = float(
            self.driver.find_element(By.CLASS_NAME, "download-speed").text
        )

        self.up = float(
            self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        )

    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        # Enter email
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, '//span[text()="Next"]')
        next_button.click()

        time.sleep(5)

        # Enter password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(By.XPATH, '//span[text()="Log in"]')
        login_button.click()

        time.sleep(5)

        tweet_text = f"Hey ISP, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        tweet_box = self.driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")
        tweet_box.send_keys(tweet_text)

        time.sleep(2)

        tweet_button = self.driver.find_element(By.XPATH, '//span[text()="Post"]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()