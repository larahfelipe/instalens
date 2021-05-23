from selenium import webdriver
from os import sep
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
    self.__getDriver()


  def getSupportedDrivers(self):
    return self.__supportedDrivers


  def getDriverPath(self):
    return self.__driverPath


  def __getDriver(self):
    srcDir = dirname(realpath(__file__)) + sep
    for i in range(len(self.__supportedDrivers)):
      verifyDriver = f'{srcDir}{self.__supportedDrivers[i]}'
      if isfile(verifyDriver):
        self.isDriverExists = True
        self.__driverPath = verifyDriver
        self.__driverName = self.__supportedDrivers[i]
        break


  def setDriver(self):
    if self.__driverName == self.__supportedDrivers[0]:
      return webdriver.Chrome
    elif self.__driverName == self.__supportedDrivers[1]:
      return webdriver.Firefox
    elif self.__driverName == self.__supportedDrivers[2]:
      return webdriver.Edge
    else:
      raise Exception('\n!> Unexpected case!')
