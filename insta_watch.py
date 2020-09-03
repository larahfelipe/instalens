from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import count
from explicit.waiter import find_element
from os import name, system, getlogin, sep
from os.path import abspath
from time import sleep


def clearDisplay():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


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
        except Exception as e:
            #print(e)
            pass
        if k < totalFollowing:
            print(f'> {totalFollowing-k} user(s) not found.\n> {k} username(s) appended.\n')
        else:
            print(f'> {k} username(s) appended.\n')

        sleep(7.5)
        try:
            for i, usr in enumerate(getFollowr(driver, instaUsr), 1):
                #print(f'({i})- {usr}')
                k = i
                followersList.append(usr)
                if i >= totalFollowers:
                    break
        except Exception as e:
            #print(e)
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
        print('\n')

    finally:
        driver.quit()


clearDisplay()
print('='*8, '<> InstaWatch <>', '='*8)
print(' '*7, 'written by felpshn')
instaUsr = str(input('\n> Username: '))
instaPass = str(input('> Password: '))
totalFollowing = int(input('\n> Num of users that you follow: '))
totalFollowers = int(input('> Num of users that follows you: '))
sleep(2.5)
print('-'*34, '\n> Done!\n> Starting browser ...')
print('-'*34)
if name == 'nt':
    try:
        driver = webdriver.Edge(executable_path=f"{abspath(sep)}Users\\{getlogin()}\\Documents\\msedgedriver")
    except:
        driver = webdriver.Chrome(executable_path=f"{abspath(sep)}Users\\{getlogin()}\\Documents\\chromedriver")
else:
    try:
        driver = webdriver.Firefox(executable_path=f"/home/{getlogin()}/Documents/geckodriver")
    except:
        driver = webdriver.Chrome(executable_path=f"/home/{getlogin()}/Documents/chromedriver")
signIn(driver, instaUsr, instaPass)
watchLists(driver, instaUsr, totalFollowing, totalFollowers)
input('Press any key to continue ...')
