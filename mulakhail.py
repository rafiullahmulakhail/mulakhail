#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To shabirbaloch
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:B4_Baloch
##### LOGO #####
logo = """
      \033[1;91m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦИтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦИтЦИтЦИ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;92m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦТтЦТ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;93m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦИтЦИтЦТ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;94m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦТтЦТ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;95m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦИтЦИтЦТтЦИтЦИтЦИтЦТтЦТтЦИтЦТтЦТтЦИтЦИтЦИтЦИ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд : 
      \033[1;96m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд      тЦЗЁЯД╡ЁЯД░ЁЯД▓ЁЯД┤ЁЯД▒ЁЯД╛ЁЯД╛ЁЯД║тЦЗ     тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;91m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд        тЦВтЦЗЁЯД║ЁЯД╕ЁЯД╜ЁЯД╢тЦЗтЦВ     тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;94m:  
@@@  @@                                  @@  @@@
 @@@@@@                                 @@@@@@
  @@@@@           88888888888           @@@@@
    @@@@        888888888888888        @@@@
      @@@@    8888888888888888888    @@@@
        @@@@888 88888888888888 8888@@@@
           8888  888888888888  88888@
          88888    88888888    888888
          88888      8888      888888
          888888888888888888888888888
           88888888888  888888888888
            88888888      888888888
             8888888888888888888888
              88888888888888888888
                8888888888888888
             @@@@ ||||||||||| @@@@
           @@@@   |||||||||||  @@@@
          @@@@                   @@@@ 
        @@@@@                      @@@@@
     @@ @@@        rafiullah        @@@ @@

\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mBalochhacker\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;93m                 тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд BalochHacker тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;93m                 тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  WhatsApp  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;93m                 тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд 03232132362тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mBalochHacker\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тХ▒тЦФтЦФтЦФтЦФтХ▓  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд 
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦХтЦХтХ▓тФКтФКтХ▒тЦПтЦП тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦХтЦХтЦВтХ▒тХ▓тЦВтЦПтЦП тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
 \033[1;96m           тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тХ▓тФКтФКтФКтФКтХ▒  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
 \033[1;96m           тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тЦХтХ▓тЦВтЦВтХ▒тЦП  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
 \033[1;96m           тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тХ▒тЦФтЦФтЦФтЦФтФКтФКтФКтФКтЦФтЦФтЦФтЦФтХ▓  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
       \033[1;93m    тЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦТтЦТWelcome To BlackMafiaтЦТтЦТтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИ
\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mB4Baloch\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;94mAuthor    \033[1;91m: \033[1;91mB4Baloch
\033[1;94mB4Baloch\033[1;91m: \033[1;91тЦТтЦУтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦИ]99.9
\033[1;94mFacebook  \033[1;91m: \033[1;91mShabir Baloch
\033[1;94mWhatsapp  \033[1;91m: \033[1;91m+923232132362
\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mBlackMafia\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд"""
jalan('\033[1;92m   .........................B4Baloch.........................:')
jalan("\033[1;93m   тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд Welcome to B4Baloch тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд   ")
jalan('\033[1;93m тШЮ тФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИLogin New AcountтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИ  ')
jalan('\033[1;93m тШЮ тФИтФИтФИтФИтФИтФИтФИ CP Acount Open After 7 Days тФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИ  ')
jalan("\033[1;93m тШЮ тФИтФИFrends Cloning k liy sirf indian id ka link us├и karainтФИ ")
jalan("\033[1;93m тШЮ тФИтФИтФИтФИтФИтФИтФИтФИWhatsApp Num :  +923232132362тФИтФИтФИтФИтФИтФИтФИтФИтФИтФИтФИ")
print "\033[1;95m   тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mLogin B4Baloch\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд"

CorrectUsername = "rafiullah"
CorrectPassword = "mulakhail"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;94mтЧетЧдтЧетЧдЁЯУЛ \x1b[1;91mTool Username \x1b[1;91m┬╗┬╗ \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94mтЧетЧдтЧетЧдЁЯФС\x1b[1;91mTool Password \x1b[1;91m┬╗┬╗ \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/ https://www.youtube.com/channel/UCAGKWM8EwDFZ9sP8CdJhGBA')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;92m     Notice:тШЮ \033[1;93mStay Home Stay Safe Save lives Save Pakistan' )
                jalan(' \033[1;92m     Notice:тШЮ \033[1;97mPray NAMAZ five time Daily' )
                jalan(' \033[1;92m     Notice:тШЮ \033[1;97mwear mask on your mouth every time ' )
                jalan(' \033[1;92m     Notice:тШЮ \033[1;97mDont go to in markets ' )
		jalan(' \033[1;92m     Notice:тШЮ \033[1;97mwash your hands every 1 hour' )
                jalan(' \033[1;92m    Warning:тШЮ \033[1;95mCloning k liay sirf indian link use karain' )
		print "\033[1;95m      тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАв\033[1;96mB4Baloch\033[1;95mтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд"
		print('\033[1;93mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдLOGIN WITH FACEBOOKтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд' )
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
		
