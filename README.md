<p align="center">
    <a href="https://github.com/felpshn/instafollow">
        <img src="https://github.com/felpshn/instafollow/blob/master/.github/instafollow-logo.png">
    </a>
</p>

<p align="center">
    <a href="https://github.com/felpshn/instafollow/releases/">
        <img src="https://img.shields.io/badge/version-3.x-lightgrey">
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

If you're the kind of person that cares about the people that aren't following you back on Instagram, you've come into the right repo. InstaFollow is a tiny automated tool built with Python and Selenium to list all the users which are not following you back.

## How to use

Before we begin, make sure that you have `git`, `python 3` and `pip` installed in your machine. Also, check out if you have any of the supported web browsers listed below and it's current version as well (it may be useful).

**Supported browsers**
- [Google Chrome (Linux & Windows)](https://chromedriver.chromium.org/downloads)
- [Microsoft Edge Chromium Based (Windows)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
- [Mozilla Firefox (Linux & Windows)](https://github.com/mozilla/geckodriver/releases) [Recommended]

After that, download your browser's webdriver by clicking in his name above. When you're up to download the webdriver, if were offered many versions, choose that one who matches your browser's current version or some previous version that are most close to it, for better compatibility and to avoid unexpected behavior.

### Clone this repo and cd into project's folder

```elm
git clone https://github.com/felpshn/instafollow.git

cd instafollow
```

### Auto installation

If you're using one of the supported linux distros listed below, you can simply run the `setup.sh` with `sudo` for automatically set all required modules. 

**Compatible Linux distros to auto install**
- Debian/Ubuntu
- Arch Linux
- Fedora

```elm
sudo ./setup.sh
```

After that, you should be able to run InstaFollow already (Jump to **Running** section).

### Manual installation

If you're on Windows or any other OS though, with `pip`, please install the following libs:

- **selenium**
- **explicit**
- **tqdm**

Now, make sure that you have downloaded one of the compatible webdriver of your choice and also, check if he's in your **Downloads** directory. Then, go at the InstaFollow's folder and run the `handleWebdriver.py` located inside of `src` to automatically extract and move the webdriver itself to the project's folder.

```elm
cd src

-- Linux:
python3 setDriverFile.py

-- Windows:
py setDriverFile.py
```

#### Everything settled up. ready to go!

### Running

Before you run, if have the **2FA (two-factor authentication)** turned on, you will need to type the auth code after logging to your account, for that I've set 15s sleep, after this time, the program will continue it's execution.

```elm
-- Linux:
python3 instafollow.py

-- Windows:
py instafollow.py
```

## Final considerations

#### That's pretty much it!

Thanks for using InstaFollow! If you have experienced any issues, please let me know or in case if you know how to solve it, feel free to help fix that out.

Also, if you wanna contribute to this tool, feel welcomed to do that as well. Our main goals are make the program execution more faster and reduce the code without compromising it's readability. You can also contribute by writing more efficient code or fixing typos, any contribuition is valid! I just ask you to keep in mind that he's a **tiny** tool, and therefore, let's try not to lose our focus about the program's main purpose.

> **DISCLAIMER:** This is a research project. I am by no means responsible for any usage of this tool, and I'm also not responsible if your accounts get banned due to the use of this tool. Use on your own behalf.

> **This project is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License](https://github.com/felpshn/instafollow/blob/master/LICENSE)**
