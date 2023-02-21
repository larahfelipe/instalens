from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from .util import Util


class Browser:
  INSTANCE = None
  webdrivers = {
    'Chrome': 'chromedriver',
    'Firefox': 'geckodriver',
    'Edge': 'msedgedriver'
  }
  TASK_TIMEOUT_IN_S = 10

  def __init__(self):
    self.wd_name = self.webdrivers.get('Chrome') + (Util.get_os() == 'Windows' and '.exe' or '')
    self.abs_path = Util.get_dir_path()
    self.wd_path = Util.check_file_exists(self.wd_name) and self.abs_path + self.wd_name or None


  @staticmethod
  def get_instance():
    if not Browser.INSTANCE:
      Browser.INSTANCE = Browser().__bootstrap()
    return Browser.INSTANCE


  def __bootstrap(self):
    if not self.wd_path:
      raise Exception('No webdriver was found in the current directory')

    service = Service(
      executable_path=self.wd_path,
      service_args=['--verbose', f'--log-path={self.abs_path}/logs/{self.wd_name}.log']
    )
    return webdriver.Chrome(service=service)
