from os import name, system

pip = 'pip'

if name != 'nt':
  pip += '3'

def installRequiredDependcs():
  system(f'{pip} install selenium')
  system(f'{pip} install explicit')
  system(f'{pip} install tqdm')


installRequiredDependcs()

from instafollowers.util import Util

Util.handleWebdriverExtraction()
