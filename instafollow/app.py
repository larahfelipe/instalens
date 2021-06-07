from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from explicit.waiter import find_element
from time import sleep

from .browser import Browser
from .util import Util

class InstaFollow:
  def __init__(self, accountUsername, accountPassword):
    self.__username = accountUsername
    self.__password = accountPassword
    self.browser = Browser().setDriver()(executable_path=Browser().getDriverPath())
    self.totalUserFollowx = 0
    self.notFollowingBack = []


  def __signIn(self):
    self.browser.get('https://www.instagram.com/')
    sleep(1.5)
    contextSelector = self.browser.find_element_by_xpath('//input[@name=\'username\']')
    contextSelector.send_keys(self.__username)
    contextSelector = self.browser.find_element_by_xpath('//input[@name=\'password\']')
    contextSelector.send_keys(self.__password)
    contextSelector.send_keys(Keys.RETURN)
    sleep(15.0)


  def __getFollowx(self, onPerform):
    self.browser.get(f'https://www.instagram.com/{self.__username}/')
    if onPerform == 'following':
      Util.clearScreen()
      print(f'> Watching "{self.__username}" profile.\n')
    contextSelector = self.browser.find_element_by_xpath(f'//a[@href=\'/{self.__username}/{onPerform}/\']')
    self.totalUserFollowx = int(contextSelector.find_element_by_tag_name('span').text)
    contextSelector.click()
    print(f'> Collecting users in "{onPerform.capitalize()}" list ...')
    usrXMLPath = 'ul div li:nth-child({}) a.notranslate'
    listIterator = tqdm(
      range(1, self.totalUserFollowx, 12),
      ncols=65,
      leave=False
    )
    for currUsrs in listIterator:
      for usrIndex in range(currUsrs, currUsrs+12):
        yield find_element(self.browser, usrXMLPath.format(usrIndex)).text
      lastUsrListed = find_element(self.browser, usrXMLPath.format(usrIndex))
      self.browser.execute_script("arguments[0].scrollIntoView()", lastUsrListed)


  def __handleUserIteration(self):
    k = 0
    following = []
    followers = []
    for n in range(1, 3):
      try:
        onPerform = 'following' if n == 1 else 'followers'
        for i, usr in enumerate(self.__getFollowx(onPerform), 1):
          k = i
          if onPerform == 'following':
            following.append(usr)
          else:
            followers.append(usr)
      except:
        if k < self.totalUserFollowx:
          print(f'> {self.totalUserFollowx - k} user(s) not found.\n> {k} user(s) were appended.\n')
        else:
          print(f'> {k} user(s) were appended.\n')
        k = 0
    for j in range(len(following)):
      if following[j] not in followers:
        self.notFollowingBack.append(following[j])
    self.browser.quit()


  def __getUsersNotFollowingBack(self):
    Util.clearScreen()
    print('> Not following back:\n')
    notFollowingBackSorted = sorted(self.notFollowingBack)
    for idx in range(len(notFollowingBackSorted)):
      print(f'{idx+1}- {notFollowingBackSorted[idx]}')


  def run(self):
    self.__signIn()
    self.__handleUserIteration()
    self.__getUsersNotFollowingBack()
