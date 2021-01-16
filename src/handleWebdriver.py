from os import name, getlogin, sep, listdir, remove
from os.path import  abspath, isfile, dirname, realpath

from shutil import unpack_archive, move

from Browser import WebBrowser

def handleFileExtraction(relPath):
    try:
        for file in listdir(relPath):
            if file.endswith('.zip') or file.endswith('.tar.gz'):
                unpack_archive(f'{relPath}{file}', relPath)
                #remove(f'{relPath}{file}')
                print('// The file was successful unpacked.')
                break
    except:
        print(f'\n// Couldn\'t find any ".rar" or ".tar.gz" file in "{downloadsPath}"!')


compatibleWebdrivers = WebBrowser().supportedDrivers()
rootDir = f'{dirname(realpath(__file__))}'

if name == 'nt':
    downloadsPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads'
    webdriverPath = f'{downloadsPath}\\'
else:
    downloadsPath = f'/home/{getlogin()}/Downloads'
    webdriverPath = f'{downloadsPath}/'
handleFileExtraction(webdriverPath)

try:
    for j in range(len(compatibleWebdrivers)):
        webdriverExecutable = f'{webdriverPath}{compatibleWebdrivers[j]}'
        if isfile(webdriverExecutable):
            move(webdriverExecutable, rootDir)
            print(f'\n// "{compatibleWebdrivers[j]}" moved to "{rootDir}" folder.')
            break
except:
    print('\n// Couldn\'t find a compatible webdriver in your "Downloads" directory!')
