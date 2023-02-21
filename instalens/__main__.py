from .app import InstaLens
from .util import Util

if __name__ == '__main__':
  Util.clear_screen()

  flags = Util.get_flags()

  username = flags.get('username') or ''
  password = flags.get('password') or ''

  if not username or not password:
    username = input('Username:\n> ')
    password = input('Password:\n> ')

  try:
    InstaLens(username, password).run()
  except Exception as e:
    print(e)
  finally:
    input('\nPress any key to continue...')
