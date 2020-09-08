from selenium import webdriver

from os import name
from os.path import dirname, realpath, isfile


class GetWebDriver:
    def __init__(self):
        self.supportedWebDrivers = [
            'msedgedriver.exe', 'geckodriver', 'geckodriver.exe', 'chromedriver', 'chromedriver.exe'
        ]
        self.webDriverExists = ''
        self.webDriverName = ''
        self.isDriverExists()


    def isDriverExists(self):
        if name == 'nt':
            projRootPath = f'{dirname(realpath(__file__))}\\'
        else:
            projRootPath = f'{dirname(realpath(__file__))}/'
        for i in range(len(self.supportedWebDrivers)):
            webDriverPath = f'{projRootPath}{self.supportedWebDrivers[i]}'
            if isfile(webDriverPath):
                self.webDriverExists = webDriverPath
                self.webDriverName = self.supportedWebDrivers[i]
                break


    def supportedDrivers(self):
        return self.supportedWebDrivers


    def driverPath(self):
        return self.webDriverExists


    def driverName(self):
        if self.webDriverName == self.supportedWebDrivers[0]:
            return webdriver.Edge
        elif self.webDriverName == self.supportedWebDrivers[1] or self.webDriverName == self.supportedWebDrivers[2]:
            return webdriver.Firefox
        elif self.webDriverName == self.supportedWebDrivers[3] or self.webDriverName == self.supportedWebDrivers[4]:
            return webdriver.Chrome
        else:
            raise RuntimeError
