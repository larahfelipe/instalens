class Elements:
  INPUT_AUTH_USERNAME = 'username'

  INPUT_AUTH_PASSWORD = 'password'

  INPUT_AUTH_MFA = 'verificationCode'

  DIALOG_ACCOUNT_FOLLOWING = 'div[role="dialog"] div div[role="dialog"] div[role="tablist"] + div div div:nth-child({}) a.notranslate'

  DIALOG_ACCOUNT_FOLLOWERS = 'div[role="dialog"] div div[role="dialog"] div div:nth-child(2) div div:nth-child({}) a.notranslate'

  BTN_ACCOUNT_SETTINGS = 'main[role="main"] header section div:nth-child(3) button[@type="button"]'

  DIALOG_ACCOUNT_SETTINGS_BTN_LOGOUT = 'Log Out'
