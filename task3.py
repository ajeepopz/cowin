import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains

class labour:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(5)

    def wait(self, secs):
        sleep(secs)

    def quit(self):
        self.driver.quit()



    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def download(self):
        try:
            self.boot()
            self.findElementByXpath('/html/body/nav/div/div/div/ul/li[7]/a').click()
            time.sleep(5)
            self.findElementByXpath('//*[@id="nav"]/li[7]').click()
            time.sleep(5)
            self.findElementByXpath('//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
            time.sleep(5)

        except NoSuchElementException as e:
            print(e)


url = 'https://labour.gov.in/'
obj = labour(url)
obj.download()
