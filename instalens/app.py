from time import sleep
from typing import Generator, Literal, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tqdm import tqdm

from .browser import Browser
from .elements import Elements
from .util import Util

Collections = Literal['following', 'followers']
UnionCollections = Union[Collections, Literal['not_following_you', 'not_following_them']]

ITER_START_VALUE = 1
ITER_STEP_VALUE = 12

COLLECTIONS: Collections = ['following', 'followers']
UNION_COLLECTIONS: UnionCollections = [*COLLECTIONS, 'not_following_you', 'not_following_them']

class InstaLens:
  def __init__(self, username: str, password: str):
    self.username = username
    self.password = password
    self.authenticated = False
    self.total: int = 0
    self.following: list[str] = []
    self.followers: list[str] = []
    self.not_following_you: list[str] = []
    self.not_following_them: list[str] = []
    self.driver = Browser.get_instance()


  def navigate(self, to_route = ''):
    self.driver.get('https://www.instagram.com' + to_route)


  def sign_in(self):
    self.navigate()

    element: WebElement = lambda name: WebDriverWait(self.driver, Browser.TASK_TIMEOUT_IN_S)\
      .until(EC.presence_of_element_located((By.NAME, name)))

    element(Elements.INPUT_USERNAME).send_keys(self.username)
    element(Elements.INPUT_PASSWORD).send_keys(self.password + Keys.RETURN)

    mfa_input_element = element(Elements.INPUT_MFA)
    if mfa_input_element:
      mfa_code = input(str('Enter the 2FA code:\n> '))
      mfa_input_element.send_keys(mfa_code + Keys.RETURN)
      Util.clear_screen()

    sleep(Browser.TASK_TIMEOUT_IN_S)
    self.authenticated = True
    print('> Successfully signed in\n')


  def get_users(self, collection_ref: str) -> Generator[str, None, None]:
    if not self.authenticated:
      self.driver.delete_all_cookies()
      self.sign_in()

    if not collection_ref in [f'/{self.username}/following/', f'/{self.username}/followers/']:
      raise ValueError('Invalid collection reference')

    print(f'> Redirecting to {self.username}\'s profile\n')
    self.navigate(f'/{self.username}')

    element: WebElement = lambda href: WebDriverWait(self.driver, Browser.TASK_TIMEOUT_IN_S)\
      .until(EC.presence_of_element_located((By.XPATH, f'//a[@href="{href}"]')))

    collection_anchor_element: WebElement = element(collection_ref)
    self.total = int(collection_anchor_element.find_element(By.TAG_NAME, 'span').text)
    collection_anchor_element.send_keys(Keys.RETURN)

    sleep(Browser.TASK_TIMEOUT_IN_S)
    print(f'> Starting iteration over {self.total} users... (This may take a while)\n')

    iterator = tqdm(
      range(ITER_START_VALUE, self.total, ITER_STEP_VALUE),
      ncols=60,
      leave=False
    )

    element: WebElement = lambda selector: WebDriverWait(self.driver, Browser.TASK_TIMEOUT_IN_S)\
      .until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    CSS_SELECTORS = {
      f'/{self.username}/following/': Elements.DIALOG_FOLLOWING,
      f'/{self.username}/followers/': Elements.DIALOG_FOLLOWERS
    }

    for us in iterator:
      for u in range(us, us + ITER_STEP_VALUE):
        yield element(CSS_SELECTORS[collection_ref].format(u)).text

      last_item_element = element(CSS_SELECTORS[collection_ref].format(u))
      self.driver.execute_script('arguments[0].scrollIntoView()', last_item_element)


  def compose_collection(self, collection_name: Collections, collection: list):
    if not collection_name in COLLECTIONS:
      raise ValueError('Invalid collection name')

    counter: int = 0
    try:
      for i, u in enumerate(self.get_users(f'/{self.username}/{collection_name}/'), ITER_START_VALUE):
        counter = i
        fmt_username = u.removesuffix('Verified').strip()
        collection.append(fmt_username)
    except:
      if counter != self.total:
        print(f'> {self.total - counter} user(s) could not be found. {counter} user(s) were collected\n')
        return

      print(f'> Successfully collected {self.total} user(s) from {self.username}\'s {collection_name}\n')
    finally:
      counter = 0

      if len(self.following) and len(self.followers):
        print(f'> Comparing {self.username}\'s following and followers collections...\n')

        self.not_following_you = list(set(self.following) - set(self.followers))
        self.not_following_them = list(set(self.followers) - set(self.following))


  def run(self):
    self.sign_in()
    self.compose_collection('following', self.following)
    self.compose_collection('followers', self.followers)

    Util.write_to_file('Following.txt', self.following)
    Util.write_to_file('Followers.txt', self.followers)
    Util.write_to_file('NotFollowingYou.txt', self.not_following_you)
    Util.write_to_file('NotFollowingThem.txt', self.not_following_them)
