from sys import exit
from objc_util import * 
def lock():
	check_identity = True
	global v
	v = False
	global m
	m = False
	



	if check_identity:
		

		ObjCClass('NSBundle').bundleWithPath_('/System/Library/Frameworks/LocalAuthentication.framework').load()
		context = ObjCClass('LAContext').alloc().init()
		policy = 1 #put 1 if you want to auth with password, 2 with passcode
		reason = 'Authenticate'
		def funct(_cmd,success,error):
			global v
			global m
			if success:
			
				v = True
			else:
				autherr= ObjCInstance(error).localizedDescription()

				if str(autherr).startswith('Fallback'):
					if console.input_alert('Password') == 'Itsme':
					
						v=True
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
					print(autherr)
					m = True
		handler=ObjCBlock(funct,restype=None,argtypes=[c_void_p,c_void_p,c_void_p])
		context.evaluatePolicy_localizedReason_reply_(policy,reason,handler)	
	while True:
		if v: break
		if m: exit()
if __name__ == '__main__':
	lock()
