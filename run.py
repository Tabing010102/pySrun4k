import srun4k
import time
import os

while True:
	if os.system('ping -c 1 223.5.5.5')==0:
		print 'network is connected'
	else:
		print(srun4k.do_login('username', 'password'))
	time.sleep(10)
