from selenium import webdriver

from os import name
from os.path import dirname, realpath, isfile

class WebBrowser:
    def __init__(self):
        self._supportedDrivers = [
            'msedgedriver.exe', 
            'geckodriver', 
            'geckodriver.exe', 
            'chromedriver', 
            'chromedriver.exe'
        ]
        self._driverPath = ''
        self._driverName = ''
        self.driverExists()

    def supportedDrivers(self):
        return self._supportedDrivers
    
    def getPath(self):
        return self._driverPath

    def driverExists(self):
        if name == 'nt':
            rootDir = f'{dirname(realpath(__file__))}\\'
        else:
            rootDir = f'{dirname(realpath(__file__))}/'
        for i in range(len(self._supportedDrivers)):
            driverExists = f'{rootDir}{self._supportedDrivers[i]}'
            if isfile(driverExists):
                self._driverPath = driverExists
                self._driverName = self._supportedDrivers[i]
                break
            if i == len(self._supportedDrivers) - 1:
                return False

    def getName(self):
        if self._driverName == self._supportedDrivers[0]:
            return webdriver.Edge
        elif self._driverName == self._supportedDrivers[1] or self._driverName == self._supportedDrivers[2]:
            return webdriver.Firefox
        elif self._driverName == self._supportedDrivers[3] or self._driverName == self._supportedDrivers[4]:
            return webdriver.Chrome
        else:
            raise Exception('\nCouldn\'t find a compatible webdriver in the source directory!')
