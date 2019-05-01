from sys import exit
from objc_util import *

global auth_completed
auth_completed= False
def lock():
	
	check_identity = True
	global auth_completed
	auth_completed= False
	global m
	m = False
	



	if check_identity:
		

		ObjCClass('NSBundle').bundleWithPath_('/System/Library/Frameworks/LocalAuthentication.framework').load()
		context = ObjCClass('LAContext').alloc().init()
		policy = 1 #put 1 if you want to auth with password, 2 with passcode
		reason = 'Authenticate'
		def funct(_cmd,success,error):
			global auth_completed
			global m
			if success:
				
				auth_completed=True
				
				
			else:
				autherr= ObjCInstance(error).localizedDescription()

				if str(autherr).startswith('Fallback'):
					if console.input_alert('Password') == 'Itsme':
						auth_completed=True
						
					else:
						m = True
						pass
				if str(autherr).startswith('Application retry'):
				
				
					m = True
				
				'''passcode = raw_input('Passcode: ')
		if not passcode == 'pyhess':
			exit()'''
				if str(autherr).startswith('Biometry'):
					
					m = True
					pass
				else:
					
					m = True
		handler=ObjCBlock(funct,restype=None,argtypes=[c_void_p,c_void_p,c_void_p])
		context.evaluatePolicy_localizedReason_reply_(policy,reason,handler)	
	while True:
		if auth_completed: break
		if m: exit()
if __name__ == '__main__':
	lock()
