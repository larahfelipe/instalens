from .app import InstaFollow
from .util import Util

if __name__ == '__main__':
  Util.clearScreen()
  print('█'*10, ' InstaFollow ', '█'*10, '\n')
  try:
    Util.checkWebdriverExistence()
    InstaFollow(
      Util.setAndValidateCredential('Username'),
      Util.setAndValidateCredential('Password')
    ).run()
  except Exception as e:
    print(e)
  input('\nPress any key to continue ...')
