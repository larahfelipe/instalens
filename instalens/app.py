from time import sleep
from typing import Generator, Tuple, TypeVar

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

from .browser import Browser
from .elements import Elements
from .util import Util

following = TypeVar('following')
followers = TypeVar('followers')
Collections = Tuple[following, followers]

ITER_START_VALUE = 1
ITER_STEP_VALUE = 12

class InstaLens:
  def __init__(self, username: str, password: str):
    self.username = username
    self.password = password
    self.authenticated = False
    self.total: int = 0
    self.following, self.followers, self.not_following_you, self.not_following_them = [], [], [], []
    self.browser = Browser.get_instance()


  def change_route(self, to: str = ''):
    self.browser.navigate('https://www.instagram.com' + to)


  def sign_in(self):
    self.change_route()

    element = lambda name: self.browser.wait_find_element(By.NAME, name)

    element(Elements.INPUT_AUTH_USERNAME).send_keys(self.username)
    element(Elements.INPUT_AUTH_PASSWORD).send_keys(self.password + Keys.RETURN)

    mfa_input_element = element(Elements.INPUT_AUTH_MFA)
    if mfa_input_element:
      mfa_code = input(str('\nEnter the 2FA code:\n> '))
      mfa_input_element.send_keys(mfa_code + Keys.RETURN)
      Util.clear_screen()

    sleep(self.browser.get_task_timeout())
    self.authenticated = True
    print('> Successfully signed in\n')


  def sign_out(self):
    self.change_route('/' + self.username)

    element = lambda selector: self.browser.wait_find_element(By.CSS_SELECTOR, selector)
    element(Elements.BTN_ACCOUNT_SETTINGS).send_keys(Keys.RETURN)

    element = lambda text: self.browser.wait_find_element(By.LINK_TEXT, text)
    element(Elements.DIALOG_ACCOUNT_SETTINGS_BTN_LOGOUT).send_keys(Keys.RETURN)

    self.authenticated = False
    self.browser.quit()
    print('> Successfully signed out\n')


  def get_users(self, collection_ref: str) -> Generator[str, None, None]:
    collections_ref = (f'/{self.username}/following/', f'/{self.username}/followers/')

    if not collection_ref in collections_ref:
      raise ValueError('Invalid collection reference')

    print(f'> Redirecting to {self.username}\'s profile\n')

    self.change_route('/' + self.username)

    element = lambda href: self.browser.wait_find_element(By.XPATH, f'//a[@href="{href}"]')

    collection_anchor_element = element(collection_ref)
    self.total = int(collection_anchor_element.find_element(By.TAG_NAME, 'span').text)
    collection_anchor_element.send_keys(Keys.RETURN)

    print(f'> {self.total} user(s) identified\n')
    sleep(self.browser.get_task_timeout())

    print(f'> Collecting user(s) from {self.username}\'s {collection_ref.split("/")[2]}. Please wait...\n')

    element = lambda selector: self.browser.wait_find_element(By.CSS_SELECTOR, selector)

    iter = tqdm(
      range(ITER_START_VALUE, self.total, ITER_STEP_VALUE),
      ncols=60,
      leave=False
    )

    CSS_SELECTORS = {
      collections_ref[0]: Elements.DIALOG_ACCOUNT_FOLLOWING,
      collections_ref[1]: Elements.DIALOG_ACCOUNT_FOLLOWERS
    }

    for a in iter:
      for b in range(a, a + ITER_STEP_VALUE):
        yield element(CSS_SELECTORS[collection_ref].format(b)).text

      lli_element = element(CSS_SELECTORS[collection_ref].format(b))
      self.browser.execute('arguments[0].scrollIntoView()', lli_element)


  def compose_collection(self, collection_name: Collections, collection: list[str]):
    if not self.authenticated:
      self.browser.delete_cookies()
      self.sign_in()

    collections: Collections = ('following', 'followers')

    if not collection_name in collections:
      raise ValueError('Invalid collection name')

    if not type (collection) is list:
      raise TypeError('Invalid collection argument type')

    c: int = 0
    try:
      for i, u in enumerate(self.get_users(f'/{self.username}/{collection_name}/'), ITER_START_VALUE):
        c = i
        fmt_u = u.removesuffix('Verified').strip()
        collection.append(fmt_u)
    except:
      if c != self.total:
        print(f'> {self.total - c} user(s) could not be found. {c} user(s) were collected\n')
        return

      print(f'> Successfully collected {self.total} user(s) from {self.username}\'s {collection_name}\n')
    finally:
      c = 0

      if len(self.following) and len(self.followers):
        print(f'> Comparing {self.username}\'s following and followers collections...\n')

        self.not_following_you = list(set(self.following) - set(self.followers))
        self.not_following_them = list(set(self.followers) - set(self.following))


  def run(self):
    self.sign_in()
    self.compose_collection('following', self.following)
    self.compose_collection('followers', self.followers)
    # self.sign_out()

    Util.write_to_file('Following.txt', self.following)
    Util.write_to_file('Followers.txt', self.followers)
    Util.write_to_file('NotFollowingYou.txt', self.not_following_you)
    Util.write_to_file('NotFollowingThem.txt', self.not_following_them)
