<p align="center">
    <a href="https://github.com/felpshn/InstaFollowers">
        <img src="https://github.com/felpshn/InstaFollowers/blob/master/.github/instafollowers-logo.png">
    </a>
</p>

<p align="center">
    <a href="https://github.com/felpshn/InstaFollowers/releases/">
        <img src="https://img.shields.io/badge/version-4.x-lightgrey">
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

If you like to know which users are not following you back on Instagram, you just have found a great tool to help you out with that. InstaFollowers is a tiny automated tool built with Python and Selenium to list all the users that aren't following you back.

## How to use

Before we begin, make sure that you have `Python 3` and `pip` installed in your machine. Also, check out if you have any of the supported web browsers listed below and it's current version as well (it may be useful).

**Supported browsers**
- [Google Chrome (Linux & Windows)](https://chromedriver.chromium.org/downloads)
- [Microsoft Edge Chromium Based (Windows)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
- [Mozilla Firefox (Linux & Windows)](https://github.com/mozilla/geckodriver/releases) [Recommended]

After that, download your browser's webdriver by clicking in his name above. When you're up to download the webdriver, if were offered many versions, choose that one who matches your browser's current version or some previous version that are most close to it, for better compatibility and to avoid unexpected behavior.

### Clone this repo and cd into project's folder

```elm
git clone https://github.com/felpshn/InstaFollowers.git

cd InstaFollowers
```

### Installation

Before we move on to the installation process, make sure that you have downloaded one of the compatible webdriver, and also, check if he's in your **Downloads** directory. Then, run the `setup.py` to automatically set all dependencies required and the webdriver as well.

```elm
-- Linux:
python3 setup.py

-- Windows:
py setup.py
```

### Running

Now notice, if you use the **2FA (two-factor authentication)**, you will need to type the auth code after logging to your account, for that I've set 15s sleep, after this time, the program will continue it's execution.

```elm
-- Linux:
python3 -m instafollowers

-- Windows:
py -m instafollowers
```

## Final considerations

#### That's pretty much it!

Thanks for using InstaFollowers! If you have experienced any issues, please let me know or in case if you know how to solve it, feel free to help fix that out.

Also, in case you wanna contribute to this tool by writing more efficient code or fixing typos, feel welcomed to do that as well, any kind of contribution is valid! Just keep in mind that he's a **tiny** tool, and therefore, let's try not to lose our focus about the program's main purpose.

> **DISCLAIMER:** This is a research project. I am by no means responsible for any usage of this tool, and I'm also not responsible if your accounts get banned due to the use of this tool. Use on your own behalf.

> **This project is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License](https://github.com/felpshn/instafollowers/blob/master/LICENSE)**