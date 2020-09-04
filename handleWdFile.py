from os import name, getlogin, sep, listdir, remove
from os.path import  abspath, isfile, dirname, realpath
from shutil import unpack_archive, move
from insta_watch import GetWebdriver


def extractFile(relPath):
    try:
        for elmt in listdir(relPath):
            if elmt.endswith('.zip') or elmt.endswith('.tar.gz'):
                unpack_archive(f'{relPath}{elmt}', relPath)
                remove(f'{relPath}{elmt}')
                print('\n// Webdriver executable file was successful unpacked.')
                break
    except:
        print('\n// Packed webdriver archive not found!')


supportedWebdrivers = GetWebdriver().supportedDrivers()
wdExecDestPath = f'{dirname(realpath(__file__))}'
if name == 'nt':
    downloadsPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads'
    wdPackedRelPath = f'{downloadsPath}\\'
    extractFile(wdPackedRelPath)
    try:
        for i in range(0, len(supportedWebdrivers)):
            wdExecOriginPath = isfile(f'{downloadsPath}\\{supportedWebdrivers[i]}')
            if isfile(wdExecOriginPath):
                move(wdExecOriginPath, wdExecDestPath)
                print(f'\n// "{supportedWebdrivers[i]}" moved to the project\'s root folder.')
                break
    except:
        print('\n// Webdriver executable file not found!')
else:
    downloadsPath = f'/home/{getlogin()}/Downloads'
    wdPackedRelPath = f'{downloadsPath}/'
    extractFile(wdPackedRelPath)
    try:
        for i in range(0, len(supportedWebdrivers)):
            wdExecOriginPath = f'{downloadsPath}/{supportedWebdrivers[i]}'
            if isfile(wdExecOriginPath):
                move(wdExecOriginPath, wdExecDestPath)
                print(f'\n// "{supportedWebdrivers[i]}" moved to the project\'s root folder.')
                break
    except:
        print('\n// Webdriver executable file not found!')
