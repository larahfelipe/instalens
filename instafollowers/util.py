from os import system, name, sep, listdir
from os.path import dirname, realpath, join, expanduser
from shutil import unpack_archive

from .browser import Browser

class Util:
  @staticmethod
  def clearScreen():
    if name == 'nt':
      system('cls')
    else:
      system('clear')


  @staticmethod
  def checkWebdriverExistence():
    if Browser().isDriverExists == False:
      raise Exception('\n!> Couldn\'t find any compatible webdriver!')


  @staticmethod
  def setAndValidateCredential(targetField):
    credential = str(input(f'> {targetField}: '))
    if len(credential) == 0:
      raise Exception('\n!> Cannot leave a blank field!')
    else:
      return credential


  @staticmethod
  def handleWebdriverExtraction():
    srcDir = dirname(realpath(__file__))
    downloadsPath = str(join(expanduser('~'), 'Downloads') + sep)
    try:
      for file in listdir(downloadsPath):
        if file.endswith('.zip') or file.endswith('.tar.gz'):
          unpack_archive(f'{downloadsPath}{file}', srcDir)
          print(f'\n> "{file}" was extracted and moved to "{srcDir}"\n')
          break
    except:
      print('\n!> Couldn\'t find any file in your Downloads directory!')
