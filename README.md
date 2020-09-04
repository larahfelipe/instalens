<p align="center">
  <img width="566" height="113" src="https://github.com/felpshn/insta-watch/blob/master/img/instawatch-logo.png">
</p>

<p align="center">
    <a href="https://github.com/felpshn/insta-watch">
        <img src="https://img.shields.io/badge/version-2.0-lightgrey">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python%203-yellow">
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
        <img src="https://img.shields.io/badge/built%20with-Selenium-brightgreen">
    </a>
    <a href="https://github.com/felpshn/insta-watch/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/license-GPLv3-blue">
    </a>
</p>

## :scroll: About

Automated tool to list the users who don't follow you back on Instagram.

### Supported WebDrivers (for now)
- **Google Chrome (Linux & Windows)** - WebDriver download link: https://bit.ly/2EEkcpK
- **Microsoft Edge Chromium Based (Windows)** - WebDriver download link: https://bit.ly/3hOeeRq
- **Mozilla Firefox (Linux & Windows)** - WebDriver download link: https://bit.ly/2EO4ojZ

## :question: How to use

### :baby: Setting up for the first time

**1)** Check out your browser version and download the corresponding version of the supported webdrivers listed above.

**2)** On your sys terminal:
```elm
git clone https://github.com/felpshn/insta-watch.git

cd insta-watch
```
**2.1)** If you're in one of the supported linux distros, you can simple run the ```setup.sh``` for setting everything up.
```elm
sudo ./setup.sh
```
**2.2)** If you're in Windows or any other OS:

**2.2.1)** With ```pip```, please install the following libs:
- **selenium**
- **explicit**

**2.2.2)** Run the ```handleWdFile.py``` to automatically extract and move the downloaded webdriver file to the project's root folder.
```elm
-- Linux:
python3 handleWdFile.py

-- Windows:
py handleWdFile.py
```

### :running: Running
```elm
-- Linux:
python3 insta_watch.py

-- Windows:
py insta_watch.py
```

### :tada: That's it!
Thanks for using InstaWatch!, if you have experienced any runtime issues, please let me know. Also, don't forget to read the **Additional Info** section for more details about this little project.

## :loudspeaker: Additional Info

> If you're using 2FA (two-factor authentication) you will need to manually enter the auth code (rly?! xD), for that I've set a 15s sleep, after this time, the program will go on its execution. 

> **Disclaimer:** I am by no means responsible for any usage of this tool, and I'm also not responsible if your account get banned due to extensive use of this tool. Use on your own behalf.
