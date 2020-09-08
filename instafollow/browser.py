from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from os import sep, name
from os.path import dirname, realpath, isfile

class Browser:
  def __init__(self):
    self.__supportedDrivers = [
      'chromedriver',
      'geckodriver',
      'msedgedriver'
    ]
    self.isDriverExists = False
    self.__driverPath = ''
    self.__driverName = ''
    self.__retrieveDriverInfo()


  def getSupportedDrivers(self):
    return self.__supportedDrivers


  def getDriverPath(self):
    return self.__driverPath


  def __retrieveDriverInfo(self):
    srcDir = dirname(realpath(__file__)) + sep
    fileExtension = ''
    if name == 'nt':
      fileExtension = '.exe'
    for idx, _ in enumerate(self.__supportedDrivers):
      possibDriverPath = f'{srcDir}{self.__supportedDrivers[idx]}{fileExtension}'
      if isfile(possibDriverPath):
        self.isDriverExists = True
        self.__driverPath = possibDriverPath
        self.__driverName = self.__supportedDrivers[idx]
        break


  def onSet(self):
    if self.__driverName == self.__supportedDrivers[0]:
      return webdriver.Chrome
    elif self.__driverName == self.__supportedDrivers[1]:
      return webdriver.Firefox
    elif self.__driverName == self.__supportedDrivers[2]:
      return webdriver.Edge
    else:
      raise Exception('\n!> Unexpected case!')


  def getCustomFirefoxOptions(self):
    firefoxOptions = FirefoxProfile()
    firefoxOptions.set_preference('permissions.default.stylesheet', 2)
    firefoxOptions.set_preference('permissions.default.image', 2)
    return firefoxOptions
