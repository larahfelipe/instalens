<p align="center">
    <a href="https://github.com/felpshn/instafollow">
        <img src="https://github.com/felpshn/instafollow/blob/master/.github/instafollow-logo.png">
    </a>
</p>

<p align="center">
    <a href="https://github.com/felpshn/instafollow/releases/">
        <img src="https://img.shields.io/badge/version-3.0-lightgrey">
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python%203-blue">
    </a>
    <a href="https://github.com/SeleniumHQ/selenium">
        <img src="https://img.shields.io/badge/built%20with-Selenium-brightgreen">
    </a>
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
        <img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%20v4.0-orange">
    </a>
    <a href="https://makeapullrequest.com/">
        <img src="https://img.shields.io/badge/PRs-welcome-blueviolet">
    </a>
</p>

## About

InstaFollow is a tiny automated tool built with Selenium to list all the users which are not following you back on Instagram.

## How to use

### Getting started

Check out if you have any of the supported browsers and its version, after this, download the corresponding webdriver listed below.

**Supported webdrivers**
- [Google Chrome (Linux & Windows)](https://chromedriver.chromium.org/downloads)
- [Microsoft Edge Chromium Based (Windows)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
- [Mozilla Firefox (Linux & Windows)](https://github.com/mozilla/geckodriver/releases)

#### Clone this repo and cd into project's folder

```elm
git clone https://github.com/felpshn/instafollow.git

cd instafollow
```

#### Auto installation

If you're using one of the supported linux distros listed below, you can simply run the `setup.sh` with `sudo` for setting up all dependencies needed. After this, you should be able to run already (Jump to **Running** section).

**Supported Linux distros**
- Debian/Ubuntu
- Arch Linux
- Fedora

#### Manual installation

If you're in Windows or any other OS, with `pip`, please install the following libs:
- **selenium**
- **explicit**
- **tqdm**

Now make sure that you have downloaded one of the webdrivers mentioned before and check if he is in your **Downloads** directory. After that, run the `handleWebdriver.py` located in `src` to automatically extract and move the webdriver to the project's folder.

```elm
cd src

-- Linux:
python3 handleWebdriver.py

-- Windows:
py handleWebdriver.py
```

#### Everything settled up. ready to go!

### Running

Before you run, if you're using **2FA (two-factor authentication)** you will need to type the auth code after logging to your account, for that I've set 15s sleep, after this time, the program will continue its execution. 

```elm
-- Linux:
python3 instafollow.py

-- Windows:
py instafollow.py
```

## Final considerations

#### That's pretty much it!

Thanks for using InstaFollow! If you have experienced any issues, please let me know or in case if you know how to solve it, feel welcomed to help to fix that out.

Also, if you wanna contribute to this tool, feel welcomed to do that as well. Our main goals are make the program execution more faster and reduce the code without compromising its readability. You can also contribute by writing more efficient code or fixing typos, I just ask you to keep in mind that he's a **tiny** tool, and therefore, let's try not to lose our focus about the program's main purpose.

> **DISCLAIMER:** This is a research project. I am by no means responsible for any usage of this tool, and I'm also not responsible if your accounts get banned due to the use of this tool. Use on your own behalf.

> **This project is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License](https://github.com/felpshn/instafollow/blob/master/LICENSE)**