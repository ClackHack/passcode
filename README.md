# passcode
Pythonista passcode
Use to lock your scripts with fingerprint or touch-id
Use the following code:

import passcode,sys,importlib
importlib.reload(passcode)
if not passcode.auth_completed: sys.exit()
