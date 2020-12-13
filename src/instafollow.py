from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from WebDriver import GetWebDriver

from itertools import count
from explicit.waiter import find_element

from os import name, system
from time import sleep


def clearScreen():
    system('cls') if name == 'nt' else system('clear')


def signIn(driver, accData):
    driver.get('https://www.instagram.com/')
    sleep(1.5)
    findField = driver.find_element_by_xpath('//input[@name=\'username\']')
    findField.send_keys(accData[0])
    findField = driver.find_element_by_xpath('//input[@name=\'password\']')
    findField.send_keys(accData[1])
    findField.send_keys(Keys.RETURN)
    sleep(15.0)


def getProfile(accName, runtimeHandler):
    driver.get(f'https://www.instagram.com/{accName}')
    if runtimeHandler == 'following':
        clearScreen()
        print(f'> Watching "{accName}" profile.\n')
    print(f'> Catching usernames in "{runtimeHandler.capitalize()}" list ...')
    findField = driver.find_element_by_xpath(f'//a[@href=\'/{accName}/{runtimeHandler}/\']')
    totalAccFollowx = findField.find_element_by_tag_name('span').text
    accData.append(int(totalAccFollowx))
    findField.click()
    usrElmtXPosition = 'ul div li:nth-child({}) a.notranslate'
    for listedUsrs in count(start=1, step=12):
        for usrIndex in range(listedUsrs, listedUsrs+12):
            yield find_element(driver, usrElmtXPosition.format(usrIndex)).text
        lastUsrListed = find_element(driver, usrElmtXPosition.format(usrIndex))
        driver.execute_script("arguments[0].scrollIntoView()", lastUsrListed)


def watchAcc(driver, accData):
    k = 0
    followingList = []
    followersList = []
    notFollowingBack = []
    for a in range(1, 3):
        try:
            runtimeHandler = 'following' if a == 1 else 'followers'
            for i, usr in enumerate(getProfile(accData[0], runtimeHandler), 1):
                k = i
                if runtimeHandler == 'following':
                    followingList.append(usr)
                else:
                    followersList.append(usr)
        except:
            if k < accData[a+1]:
                print(f'> {accData[a+1]-k} user(s) not found.\n> {k} username(s) appended.\n')
            else:
                print(f'> {k} username(s) appended.\n')
            k = 0

    print('> Iterating over lists ...\n')
    for j in range(len(followingList)):
        if followingList[j] not in followersList:
            notFollowingBack.append(followingList[j])

    sleep(2.5)
    clearScreen()
    print('> Not following you back:\n')
    notFollowingBackSorted = sorted(notFollowingBack)
    for k in range(len(notFollowingBackSorted)):
        print(f'({k+1})- {notFollowingBackSorted[k]}')

    driver.quit()


if __name__ == "__main__":
    clearScreen()
    print('='*8, '<> InstaFollow <>', '='*8)
    accData = []
    accData.append(str(input('\n> Username: ')))
    accData.append(str(input('> Password: ')))
    try:
        driver = GetWebDriver().driverName()(executable_path=GetWebDriver().driverPath())
        print('-'*34, '\nDone!\n> Starting WebDriver ...')
        print('-'*34)
        signIn(driver, accData)
        watchAcc(driver, accData)
    except Exception as e:
        print(e)
    input('\nPress any key to continue ...')
