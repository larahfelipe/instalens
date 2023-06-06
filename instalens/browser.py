from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .util import Util


class Browser:
  _INSTANCE = None

  def __init__(self):
    self._abs_path = Util.get_dir_path()
    self._wd_name = 'chromedriver' + (Util.get_os() == 'Windows' and '.exe' or '')
    self._wd_path = Util.check_file_exists(self._wd_name) and self._abs_path + self._wd_name or None

    self._TASK_TIMEOUT_IN_S = 10

    self._wd = self._bootstrap()


  def _bootstrap(self):
    if not self._wd_path:
      raise Exception('No webdriver was found in the current directory')

    logs_dir_exists = Util.check_dir_exists('logs')
    if not logs_dir_exists:
      Util.create_dir('logs')

    service = Service(
      executable_path=self._wd_path,
      service_args=['--verbose', f'--log-path={self._abs_path}/logs/{self._wd_name}.log']
    )
    return webdriver.Chrome(service=service)


  @staticmethod
  def get_instance():
    if not Browser._INSTANCE:
      Browser._INSTANCE = Browser()
    return Browser._INSTANCE


  def get_task_timeout(self):
    return self._TASK_TIMEOUT_IN_S


  def set_task_timeout(self, timeout_in_s: int):
    if not isinstance(timeout_in_s, int):
      raise TypeError('Timeout must be an integer')

    self._TASK_TIMEOUT_IN_S = timeout_in_s


  def navigate(self, route: str = ''):
    self._wd.get(route)


  def wait_find_element(self, by: By, value: str, timeout_in_s: int | None=None) -> WebElement:
    return WebDriverWait(self._wd, timeout_in_s or self._TASK_TIMEOUT_IN_S)\
      .until(EC.presence_of_element_located((by, value)))


  def execute(self, script: str, *args):
    return self._wd.execute_script(script, *args)


  def delete_cookies(self):
    self._wd.delete_all_cookies()


  def quit(self):
    self._wd.quit()
