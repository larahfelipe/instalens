from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Browser import WebBrowser

from tqdm import tqdm
from explicit.waiter import find_element

from os import name, system
from time import sleep


def clearScreen():
    system('cls') if name == 'nt' else system('clear')


def signIn(browser, accData):
    browser.get('https://www.instagram.com/')
    sleep(1.5)
    findField = browser.find_element_by_xpath('//input[@name=\'username\']')
    findField.send_keys(accData[0])
    findField = browser.find_element_by_xpath('//input[@name=\'password\']')
    findField.send_keys(accData[1])
    findField.send_keys(Keys.RETURN)
    sleep(15.0)


def fetchAccFollowx(accName, runtimeHandler):
    browser.get(f'https://www.instagram.com/{accName}')
    if runtimeHandler == 'following':
        clearScreen()
        print(f'> Watching "{accName}" profile.\n')
    findField = browser.find_element_by_xpath(f'//a[@href=\'/{accName}/{runtimeHandler}/\']')
    totalAccFollowx = int(findField.find_element_by_tag_name('span').text)
    accData.append(totalAccFollowx)
    findField.click()
    print(f'> Catching usernames in "{runtimeHandler.capitalize()}" list ...')
    usrElmtXPosition = 'ul div li:nth-child({}) a.notranslate'
    listIterator = tqdm(
        range(1, totalAccFollowx, 12),
        ncols=65,
        leave=False
    )
    for listedUsrs in listIterator:
        for usrIndex in range(listedUsrs, listedUsrs+12):
            yield find_element(browser, usrElmtXPosition.format(usrIndex)).text
        lastUsrListed = find_element(browser, usrElmtXPosition.format(usrIndex))
        browser.execute_script("arguments[0].scrollIntoView()", lastUsrListed)


def performIteration(browser, accData):
    k = 0
    following = []
    followers = []
    notFollowingBack = []
    for a in range(1, 3):
        try:
            runtimeHandler = 'following' if a == 1 else 'followers'
            for i, usr in enumerate(fetchAccFollowx(accData[0], runtimeHandler), 1):
                k = i
                if runtimeHandler == 'following':
                    following.append(usr)
                else:
                    followers.append(usr)
        except:
            if k < accData[a+1]:
                print(f'> {accData[a+1]-k} user(s) not found.\n> {k} username(s) appended.\n')
            else:
                print(f'> {k} username(s) appended.\n')
            k = 0

    for j in range(len(following)):
        if following[j] not in followers:
            notFollowingBack.append(following[j])

    sleep(2.5)
    clearScreen()
    print('> Not following you back:\n')
    notFollowingBackSorted = sorted(notFollowingBack)
    for k in range(len(notFollowingBackSorted)):
        print(f'{k+1}- {notFollowingBackSorted[k]}')

    browser.quit()


if __name__ == "__main__":
    clearScreen()
    print('█'*8, '| InstaFollow |', '█'*8)
    accData = []
    try:
        if WebBrowser().driverExists() == False:
            raise Exception('\n> Couldn\'t find the webdriver\'s executable!')
        accData.append(str(input('\n> Username: ')))
        accData.append(str(input('> Password: ')))
        if len(accData[0]) > 0 and len(accData[1]) > 0:
            browser = WebBrowser().getName()(executable_path=WebBrowser().getPath())
            print('-'*34, '\nDone!\n> Opening Browser ...')
            signIn(browser, accData)
            performIteration(browser, accData)
        else:
            print('\n> Cannot entry empty values!')
    except Exception as e:
        print(e)
    input('\nPress any key to continue ...')
