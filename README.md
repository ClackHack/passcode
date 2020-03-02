# passcode\n
Pythonista passcode\n
Use to lock your scripts with fingerprint or touch-id\n
Use the following code:\n\n

import passcode,sys,importlib\n
importlib.reload(passcode)\n
if not passcode.auth_completed: sys.exit()\n
