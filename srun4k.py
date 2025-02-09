import password
import requests


class pySrun4kError(Exception):
	def __init__(self,reason):
		Exception.__init__(self)
		self.reason = reason

def do_login(username,pwd,mbytes=0,minutes=0):
	pwd = password.encrypt(pwd)
	payload = {
		'action':'login',
		'username':username,
		'password':pwd,
		'drop':0,
		'pop':0,
		'type':2,
		'n':117,
		'mbytes':0,
		'minutes':0,
		'ac_id':1
	}
	header = {
		'user-agent':'pySrun4k'
	}
	r = requests.post("http://202.201.252.10/cgi-bin/srun_portal",data=payload,headers=header)
	if ('login_error' in r.text):
		ret = {
			'success':False,
			'code':int(r.text[13:17]),
			'reason':r.text[19:]
		}
		return ret;
	elif ('login_ok' in r.text):
		ret = {
			'success':True,
			'data':r.text.split(',')[1:]
		}
		return ret;
	else:
		raise pySrun4kError(r.text)

def check_online():
	header = {
		'user-agent':'pySrun4k'
	}
	r = requests.get("http://202.201.252.10/cgi-bin/rad_user_info",headers=header)
	if ('not_online' in r.text):
		ret = {
			'online':False
		}
		return ret
	else:
		raw = r.text.split(',')
		ret = {
			'online':True,
			'username':raw[0],
			'login_time':raw[1],
			'now_time':raw[2],
			'used_bytes':raw[6],
			'used_second':raw[7],
			'ip':raw[8],
			'balance':raw[11],
			'auth_server_version':raw[21]
		}
		return ret

def do_logout(username):
	header = {
		'user-agent':'pySrun4k'
	}
	payload = {
		'action':'logout',
		'ac_id':1,
		'username':username, 
		'type':2
	}
	r = requests.post('http://202.201.252.10/cgi-bin/srun_portal',data=payload,headers=header)
	if ('logout_ok' in r.text):
		ret = {
			'success':True,
		}
		return ret;
	elif ('login_error' in r.text):
		ret = {
			'success':False,
			'reason':r.text.split('#')[1]
		}
		return ret
	else:
		raise pySrun4kError(r.text)

def force_logout(username,pwd):
	payload = {
		'action':'logout',
		'username':username,
		'password':pwd,
		'drop':0,
		'type':1,
		'n':117,
		'ac_id':1
	}
	header = {
		'user-agent':'pySrun4k'
	}
	r = requests.post('http://202.201.252.10/cgi-bin/srun_portal',data=payload,headers=header)
	if ('logout_ok' in r.text):
		ret = {
			'success':True
		}
		return ret
	elif ('login_error' in r.text):
		ret = {
			'success':False,
			'reason':r.text.split('#')[1]
		}
		return ret
	else:
		raise pySrun4kError(r.text)
