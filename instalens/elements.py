class Elements:
  INPUT_USERNAME = 'username'

  INPUT_PASSWORD = 'password'

  INPUT_MFA = 'verificationCode'

  DIALOG_FOLLOWING = 'div[role="dialog"] div div[role="dialog"] div[role="tablist"] + div div div:nth-child({}) a.notranslate'

  DIALOG_FOLLOWERS = 'div[role="dialog"] div div[role="dialog"] div div:nth-child(2) div div:nth-child({}) a.notranslate'
