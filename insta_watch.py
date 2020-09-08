from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import count
from explicit.waiter import find_element
from os import name, system
from os.path import isfile, dirname, realpath
from time import sleep


def clearDisplay():
    if name == 'nt':
        system('cls')
    else:
        system('clear')



class GetWebdriver:
    def __init__(self):
        self.supportedWebdrivers = [
            'msedgedriver.exe', 'geckodriver', 'geckodriver.exe', 'chromedriver', 'chromedriver.exe'
        ]
        self.webdriverExists = ''
        self.webdriverName = ''


    def isDriverExists(self):
        if name == 'nt':
            projRootPath = f'{dirname(realpath(__file__))}\\'
        else:
            projRootPath = f'{dirname(realpath(__file__))}/'
        for i in range(0, len(self.supportedWebdrivers)):
            webdriverPath = f'{projRootPath}{self.supportedWebdrivers[i]}'
            if isfile(webdriverPath):
                self.webdriverExists = webdriverPath
                self.webdriverName = self.supportedWebdrivers[i]
                break
            if i == len(self.supportedWebdrivers[i])-1:
                print('-'*34, '\n!> Compatible webdriver not found!')


    def supportedDrivers(self):
        return self.supportedWebdrivers


    def driverPath(self):
        self.isDriverExists()
        return self.webdriverExists


    def driverName(self):
        self.isDriverExists()
        if self.webdriverName == self.supportedWebdrivers[0]:
            return webdriver.Edge
        elif self.webdriverName == self.supportedWebdrivers[1] or self.webdriverName == self.supportedWebdrivers[2]:
            return webdriver.Firefox
        elif self.webdriverName == self.supportedWebdrivers[3] or self.webdriverName == self.supportedWebdrivers[4]:
            return webdriver.Chrome
        else:
            raise RuntimeError



def signIn(driver, instaUsr, instaPass):
    driver.get('https://www.instagram.com/')
    sleep(1.5)
    findField = driver.find_element_by_xpath("//input[@name='username']")
    findField.send_keys(instaUsr)
    findField = driver.find_element_by_xpath("//input[@name='password']")
    findField.send_keys(instaPass)
    findField.send_keys(Keys.RETURN)
    sleep(15.0)
    driver.get(f'https://www.instagram.com/{instaUsr}')
    clearDisplay()
    print(f'> Watching "{instaUsr}" profile.\n')


def getFollowg(driver, instaUsr):
    findField = driver.find_element_by_xpath(f"//a[@href='/{instaUsr}/following/']")
    findField.click()
    print('> Catching usernames in "Following" list ...')
    sleep(2.5)
    getFollowingCSS = 'ul div li:nth-child({}) a.notranslate'
    for listedUsers in count(start=1, step=12):
        for usrIndex in range(listedUsers, listedUsers+12):
            yield find_element(driver, getFollowingCSS.format(usrIndex)).text
        lastUserListed = find_element(driver, getFollowingCSS.format(usrIndex))
        driver.execute_script("arguments[0].scrollIntoView()", lastUserListed)


def getFollowr(driver, instaUsr):
    driver.get(f'https://www.instagram.com/{instaUsr}')
    findField = driver.find_element_by_xpath(f"//a[@href='/{instaUsr}/followers/']")
    findField.click()
    print('> Catching usernames in "Followers" list ...')
    sleep(2.5)
    getFollowerCSS = 'ul div li:nth-child({}) a.notranslate'
    for listedUsers in count(start=1, step=12):
        for usrIndex in range(listedUsers, listedUsers+12):
            yield find_element(driver, getFollowerCSS.format(usrIndex)).text
        lastUserListed = find_element(driver, getFollowerCSS.format(usrIndex))
        driver.execute_script("arguments[0].scrollIntoView()", lastUserListed)


def watchLists(driver, instaUsr, totalFollowing, totalFollowers):
    k = 0
    followingList = []
    followersList = []
    notFollowingBack = []
    try:
        sleep(7.5)
        try:
            for i, usr in enumerate(getFollowg(driver, instaUsr), 1):
                #print(f'({i})- {usr}')
                k = i
                followingList.append(usr)
                if i >= totalFollowing:
                    break
        except:
            pass
        if k < totalFollowing:
            print(f'> {totalFollowing-k} user(s) not found.\n> {k} username(s) appended.\n')
        else:
            print(f'> {k} username(s) appended.\n')

        k = 0
        sleep(7.5)
        try:
            for i, usr in enumerate(getFollowr(driver, instaUsr), 1):
                #print(f'({i})- {usr}')
                k = i
                followersList.append(usr)
                if i >= totalFollowers:
                    break
        except:
            pass
        if k < totalFollowers:
            print(f'> {totalFollowers-k} user(s) not found.\n> {k} username(s) appended.\n')
        else:
            print(f'> {k} username(s) appended.\n')

        sleep(2.5)
        print('> Iterating over lists ...\n')
        sleep(5.0)
        for j in range(0, len(followingList)):
            if followingList[j] not in followersList:
                notFollowingBack.append(followingList[j])

        clearDisplay()
        print('-'*34, '\n> Not following you back:\n')
        for k in range(0, len(notFollowingBack)):
            print(f'({k+1})- {notFollowingBack[k]}')

    finally:
        driver.quit()



if __name__ == "__main__":
    clearDisplay()
    print('='*8, '<> InstaWatch <>', '='*8)
    instaUsr = str(input('\n> Username: '))
    instaPass = str(input('> Password: '))
    totalFollowing = int(input('\n> Num of users that you follow: '))
    totalFollowers = int(input('> Num of users that follows you: '))
    try:
        driver = GetWebdriver().driverName()(executable_path=GetWebdriver().driverPath())
        print('-'*34, '\n> Done!\n> Starting browser ...')
        print('-'*34)
        sleep(2.5)
        signIn(driver, instaUsr, instaPass)
        watchLists(driver, instaUsr, totalFollowing, totalFollowers)
    except Exception as e:
        print(e)
    input('\nPress any key to continue ...')
