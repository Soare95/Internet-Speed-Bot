from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 1000
PROMISED_UP = 800
CHROME_DRIVER_PATH = r"D:/chromedriver.exe"
TWITTER_EMAIL = "YOUR_EMAIL"
TWITTER_PASSWORD = "YOUR_PASSWORD"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.download_speed = 0
        self.upload_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        self.consent_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        self.consent_button.click()

        self.go_button = self.driver.find_element_by_class_name("js-start-test ")
        self.go_button.click()

        time.sleep(40)
        self.download_speed = self.driver.find_element_by_class_name("download-speed")
        self.upload_speed = self.driver.find_element_by_class_name("upload-speed")
        print(self.download_speed.text)
        print(self.upload_speed.text)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        time.sleep(5)
        self.log_in_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a[2]')
        self.log_in_button.click()

        time.sleep(1)
        self.email_twiter = self.driver.find_element_by_name("session[username_or_email]")
        self.email_twiter.send_keys(TWITTER_EMAIL)

        time.sleep(1)
        self.password_twitter = self.driver.find_element_by_name("session[password]")
        self.password_twitter.send_keys(TWITTER_PASSWORD)
        self.password_twitter.send_keys(Keys.ENTER)

        time.sleep(1)
        self.tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]')
        self.tweet_button.click()

        time.sleep(1)
        self.tweet_message = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        self.tweet_message.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        time.sleep(1)
        self.post_message = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        self.post_message.click()


interned_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
interned_bot.get_internet_speed()
interned_bot.tweet_at_provider()



