<p align="center">
    <a href="https://github.com/felpshn/insta-watch">
        <img width="566" height="113" src="https://github.com/felpshn/insta-watch/blob/master/.github/instawatch-logo.png">
    </a>
</p>

<p align="center">
    <a href="https://github.com/felpshn/insta-watch">
        <img src="https://img.shields.io/badge/version-3.0-lightgrey">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python%203-yellow">
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
        <img src="https://img.shields.io/badge/built%20with-Selenium-brightgreen">
    </a>
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
        <img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%20v4.0-orange">
    </a>
</p>

## :scroll: About

Automated tool built with Selenium to list the users who don't follow you back on Instagram.

### Supported WebDrivers
- **Google Chrome (Linux & Windows)** - WebDriver download link: https://bit.ly/2EEkcpK
- **Microsoft Edge Chromium Based (Windows)** - WebDriver download link: https://bit.ly/3hOeeRq
- **Mozilla Firefox (Linux & Windows)** - WebDriver download link: https://bit.ly/2EO4ojZ

### Supported Linux distros (for auto install)
- **Debian/Ubuntu**
- **Arch Linux**
- **Fedora**

## :question: How to use

### :baby: Setting up for the first time

**1)** Check out your browser version and download the corresponding version of the supported webdrivers listed above.

**2)** On your sys terminal:
```elm
git clone https://github.com/felpshn/insta-watch.git

cd insta-watch
```
#### Automatic installation
**3)** If you're in one of the supported linux distros, you can simple run the ```setup.sh``` for setting everything up. After this, you should be able to run already.
```elm
sudo ./setup.sh
```
#### Manual installation
**3)** If you're in Windows or any other OS:

**3.1)** With ```pip```, please install the following libs:
- **selenium**
- **explicit**

**3.2)** Run the ```setDriverFile.py``` located in ```src``` to automatically extract and move the downloaded webdriver file to the project's root folder.
```elm
cd src

-- Linux:
python3 setDriverFile.py

-- Windows:
py setDriverFile.py
```

### :running: Running
```elm
-- Linux:
python3 insta_watch.py

-- Windows:
py insta_watch.py
```

### :tada: That's it!
Thanks for using InstaWatch!, if you have experienced any issues, please let me know. Also, don't forget to read the **Additional Info** section for more details about this little tool.

## :loudspeaker: Additional Info

> If you're using 2FA (two-factor authentication) you will need to manually enter the auth code, for that I've set a 15s sleep, after this time, the program will go on its execution. 

> **DISCLAIMER:** This is a research project. I am by no means responsible for any usage of this tool, and I'm also not responsible if your accounts get banned due to the use of this tool. Use on your own behalf.

> **This project is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License](https://github.com/felpshn/insta-watch/blob/master/LICENSE).**