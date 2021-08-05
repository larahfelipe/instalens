from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from explicit.waiter import find_element
from time import sleep

from .browser import Browser
from .util import Util

class InstaFollowers:
  def __init__(self, accountUsername, accountPassword):
    self.__username = accountUsername
    self.__password = accountPassword
    if Browser().isFirefox:
      self.browser = Browser().onSet()(
        executable_path=Browser().getDriverPath(),
        firefox_profile=Browser().getCustomFirefoxOptions()
      )
    else:
      self.browser = Browser().onSet()(
        executable_path=Browser().getDriverPath()
      )
    self.totalUserFollowx = 0
    self.following = []
    self.followers = []
    self.notFollowingBack = []


  def __signIn(self):
    self.browser.get('https://www.instagram.com/')
    sleep(1.5)
    ctxSelector = self.browser.find_element_by_xpath('//input[@name=\'username\']')
    ctxSelector.send_keys(self.__username)
    ctxSelector = self.browser.find_element_by_xpath('//input[@name=\'password\']')
    ctxSelector.send_keys(self.__password)
    ctxSelector.send_keys(Keys.RETURN)
    sleep(15)


  def __getFollowx(self, onPerform):
    self.browser.get(f'https://www.instagram.com/{self.__username}/')
    sleep(2.5)
    if onPerform == 'following':
      Util.clearScreen()
      print(f'> Watching "{self.__username}" profile.\n')
    ctxSelector = self.browser.find_element_by_xpath(f'//a[@href=\'/{self.__username}/{onPerform}/\']')
    self.totalUserFollowx = int(ctxSelector.find_element_by_tag_name('span').text)
    ctxSelector.send_keys(Keys.ENTER)
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
    for n in range(1, 3):
      try:
        onPerform = 'following' if n == 1 else 'followers'
        for idx, usr in enumerate(self.__getFollowx(onPerform), 1):
          k = idx
          if onPerform == 'following':
            self.following.append(usr)
          else:
            self.followers.append(usr)
      except:
        if k < self.totalUserFollowx:
          print(f'> {self.totalUserFollowx - k} user(s) not found.\n> {k} user(s) were appended.\n')
        else:
          print(f'> {k} user(s) were appended.\n')
        k = 0
    self.browser.quit()


  def __getUsersNotFollowingBack(self):
    Util.clearScreen()
    for _, usr in enumerate(self.following):
      if usr not in self.followers:
        self.notFollowingBack.append(usr)

    print('> Not following back:\n')
    notFollowingBackSorted = sorted(self.notFollowingBack)
    for idx, usr in enumerate(notFollowingBackSorted, 1):
      print(f'{idx}. {usr}')


  def run(self):
    self.__signIn()
    self.__handleUserIteration()
    self.__getUsersNotFollowingBack()
