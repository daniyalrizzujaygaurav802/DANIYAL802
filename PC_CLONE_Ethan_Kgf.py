#____ DECODER : ETHAN BRO 👋
#______ TG : KGF CYBER TEAM 
#____ SEND BY : Kalyan KING
import time
import os
import shutil
import random
import hashlib
import requests
import sys
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock, Semaphore
from colorama import Fore, Style, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import threading
import subprocess
from datetime import datetime, timedelta
LICENSE_FILE = '/data/data/com.termux/files/home/.ariyan_license'
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/119.0.0.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/118.0.0.0',
    'Mozilla/5.0 (X11; CentOS; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 9_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 8_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/117.0.0.0',
    'Mozilla/5.0 (X11; OpenBSD x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 7_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 6_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 5_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 4_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/116.0.0.0',
    'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 3_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 2_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/115.0.0.0',
    'Mozilla/5.0 (X11; Arch; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/114.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/113.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/112.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/111.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/110.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/109.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/108.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/107.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/106.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/105.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/104.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/103.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/102.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/101.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/99.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/98.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/97.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/96.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/95.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/94.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/93.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36']
WINDOW_SIZES = [
    '1920,1080',
    '1366,768',
    '1440,900',
    '1536,864',
    '1280,720',
    '1024,768',
    '1920,1200',
    '2560,1440',
    '1360,768',
    '1280,800',
    '2560,1600',
    '1680,1050',
    '1280,960',
    '1152,864',
    '1600,1200',
    '1400,1050',
    '1440,810',
    '1440,1080',
    '1600,900',
    '2048,1536',
    '1024,600',
    '1920,1440',
    '1280,1024',
    '1728,1080',
    '1600,768',
    '1280,854',
    '1440,720',
    '1024,576',
    '1920,960',
    '2560,1080',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1920,1440',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1920,1080',
    '1366,1024',
    '1440,1050',
    '1920,1200',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1280,720',
    '1920,1440',
    '1440,900',
    '1600,1200',
    '1024,768',
    '1920,1080',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152',
    '1680,1050',
    '1440,900',
    '1024,768',
    '1280,1024',
    '1600,1200',
    '2048,1536',
    '1366,768',
    '1920,1200',
    '1360,768',
    '1280,800',
    '1152,864',
    '1600,900',
    '1400,1050',
    '1440,810',
    '1728,1080',
    '1920,960',
    '1280,720',
    '2560,1440',
    '1280,854',
    '1024,600',
    '1920,1440',
    '2560,1600',
    '1280,960',
    '1600,768',
    '1440,720',
    '1024,576',
    '1536,1024',
    '1280,800',
    '1600,1024',
    '1440,960',
    '1024,640',
    '1728,972',
    '1600,1280',
    '1366,1024',
    '1440,1050',
    '1536,960',
    '1600,640',
    '2048,1152']
FINGERPRINTS = [][{
    'lang': 'en-US',
    'timezone': 'America/New_York',
    'platform': 'Win32' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/London',
    'platform': 'Win32' }][{
    'lang': 'fr-FR',
    'timezone': 'Europe/Paris',
    'platform': 'Linux' }][{
    'lang': 'de-DE',
    'timezone': 'Europe/Berlin',
    'platform': 'MacIntel' }][{
    'lang': 'es-ES',
    'timezone': 'Europe/Madrid',
    'platform': 'Win32' }][{
    'lang': 'it-IT',
    'timezone': 'Europe/Rome',
    'platform': 'Linux' }][{
    'lang': 'pt-BR',
    'timezone': 'America/Sao_Paulo',
    'platform': 'Win32' }][{
    'lang': 'ja-JP',
    'timezone': 'Asia/Tokyo',
    'platform': 'MacIntel' }][{
    'lang': 'zh-CN',
    'timezone': 'Asia/Shanghai',
    'platform': 'Linux' }][{
    'lang': 'ru-RU',
    'timezone': 'Europe/Moscow',
    'platform': 'Win32' }][{
    'lang': 'ko-KR',
    'timezone': 'Asia/Seoul',
    'platform': 'Win32' }][{
    'lang': 'en-AU',
    'timezone': 'Australia/Sydney',
    'platform': 'MacIntel' }][{
    'lang': 'en-CA',
    'timezone': 'America/Toronto',
    'platform': 'Linux' }][{
    'lang': 'nl-NL',
    'timezone': 'Europe/Amsterdam',
    'platform': 'Win32' }][{
    'lang': 'pl-PL',
    'timezone': 'Europe/Warsaw',
    'platform': 'Win32' }][{
    'lang': 'tr-TR',
    'timezone': 'Europe/Istanbul',
    'platform': 'Linux' }][{
    'lang': 'ar-SA',
    'timezone': 'Asia/Riyadh',
    'platform': 'Win32' }][{
    'lang': 'hi-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Linux' }][{
    'lang': 'th-TH',
    'timezone': 'Asia/Bangkok',
    'platform': 'Win32' }][{
    'lang': 'vi-VN',
    'timezone': 'Asia/Ho_Chi_Minh',
    'platform': 'MacIntel' }][{
    'lang': 'id-ID',
    'timezone': 'Asia/Jakarta',
    'platform': 'Win32' }][{
    'lang': 'ms-MY',
    'timezone': 'Asia/Kuala_Lumpur',
    'platform': 'Linux' }][{
    'lang': 'ph-PH',
    'timezone': 'Asia/Manila',
    'platform': 'Win32' }][{
    'lang': 'en-SG',
    'timezone': 'Asia/Singapore',
    'platform': 'MacIntel' }][{
    'lang': 'en-ZA',
    'timezone': 'Africa/Johannesburg',
    'platform': 'Linux' }][{
    'lang': 'en-NZ',
    'timezone': 'Pacific/Auckland',
    'platform': 'Win32' }][{
    'lang': 'sv-SE',
    'timezone': 'Europe/Stockholm',
    'platform': 'Win32' }][{
    'lang': 'no-NO',
    'timezone': 'Europe/Oslo',
    'platform': 'Linux' }][{
    'lang': 'da-DK',
    'timezone': 'Europe/Copenhagen',
    'platform': 'MacIntel' }][{
    'lang': 'fi-FI',
    'timezone': 'Europe/Helsinki',
    'platform': 'Win32' }][{
    'lang': 'el-GR',
    'timezone': 'Europe/Athens',
    'platform': 'Linux' }][{
    'lang': 'hu-HU',
    'timezone': 'Europe/Budapest',
    'platform': 'Win32' }][{
    'lang': 'cs-CZ',
    'timezone': 'Europe/Prague',
    'platform': 'MacIntel' }][{
    'lang': 'sk-SK',
    'timezone': 'Europe/Bratislava',
    'platform': 'Linux' }][{
    'lang': 'ro-RO',
    'timezone': 'Europe/Bucharest',
    'platform': 'Win32' }][{
    'lang': 'bg-BG',
    'timezone': 'Europe/Sofia',
    'platform': 'Win32' }][{
    'lang': 'hr-HR',
    'timezone': 'Europe/Zagreb',
    'platform': 'Linux' }][{
    'lang': 'sr-RS',
    'timezone': 'Europe/Belgrade',
    'platform': 'MacIntel' }][{
    'lang': 'uk-UA',
    'timezone': 'Europe/Kyiv',
    'platform': 'Linux' }][{
    'lang': 'he-IL',
    'timezone': 'Asia/Jerusalem',
    'platform': 'Win32' }][{
    'lang': 'fa-IR',
    'timezone': 'Asia/Tehran',
    'platform': 'Linux' }][{
    'lang': 'ur-PK',
    'timezone': 'Asia/Karachi',
    'platform': 'Win32' }][{
    'lang': 'bn-BD',
    'timezone': 'Asia/Dhaka',
    'platform': 'MacIntel' }][{
    'lang': 'ta-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Linux' }][{
    'lang': 'te-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Win32' }][{
    'lang': 'ml-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Win32' }][{
    'lang': 'kn-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Linux' }][{
    'lang': 'my-MM',
    'timezone': 'Asia/Yangon',
    'platform': 'MacIntel' }][{
    'lang': 'km-KH',
    'timezone': 'Asia/Phnom_Penh',
    'platform': 'Linux' }][{
    'lang': 'lo-LA',
    'timezone': 'Asia/Vientiane',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Chicago',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Denver',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Los_Angeles',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Anchorage',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Pacific/Honolulu',
    'platform': 'Linux' }][{
    'lang': 'fr-CA',
    'timezone': 'America/Toronto',
    'platform': 'Win32' }][{
    'lang': 'es-MX',
    'timezone': 'America/Mexico_City',
    'platform': 'MacIntel' }][{
    'lang': 'de-AT',
    'timezone': 'Europe/Vienna',
    'platform': 'Linux' }][{
    'lang': 'de-CH',
    'timezone': 'Europe/Zurich',
    'platform': 'Win32' }][{
    'lang': 'fr-CH',
    'timezone': 'Europe/Zurich',
    'platform': 'Win32' }][{
    'lang': 'it-CH',
    'timezone': 'Europe/Zurich',
    'platform': 'Linux' }][{
    'lang': 'pt-PT',
    'timezone': 'Europe/Lisbon',
    'platform': 'MacIntel' }][{
    'lang': 'es-AR',
    'timezone': 'America/Argentina/Buenos_Aires',
    'platform': 'Linux' }][{
    'lang': 'es-CL',
    'timezone': 'America/Santiago',
    'platform': 'Win32' }][{
    'lang': 'es-CO',
    'timezone': 'America/Bogota',
    'platform': 'Win32' }][{
    'lang': 'es-PE',
    'timezone': 'America/Lima',
    'platform': 'Linux' }][{
    'lang': 'es-VE',
    'timezone': 'America/Caracas',
    'platform': 'MacIntel' }][{
    'lang': 'es-EC',
    'timezone': 'America/Guayaquil',
    'platform': 'Linux' }][{
    'lang': 'en-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Win32' }][{
    'lang': 'en-PK',
    'timezone': 'Asia/Karachi',
    'platform': 'Linux' }][{
    'lang': 'en-BD',
    'timezone': 'Asia/Dhaka',
    'platform': 'MacIntel' }][{
    'lang': 'en-LK',
    'timezone': 'Asia/Colombo',
    'platform': 'Win32' }][{
    'lang': 'en-NG',
    'timezone': 'Africa/Lagos',
    'platform': 'Linux' }][{
    'lang': 'en-GH',
    'timezone': 'Africa/Accra',
    'platform': 'Win32' }][{
    'lang': 'en-KE',
    'timezone': 'Africa/Nairobi',
    'platform': 'MacIntel' }][{
    'lang': 'en-TZ',
    'timezone': 'Africa/Dar_es_Salaam',
    'platform': 'Linux' }][{
    'lang': 'en-UG',
    'timezone': 'Africa/Kampala',
    'platform': 'Win32' }][{
    'lang': 'en-ET',
    'timezone': 'Africa/Addis_Ababa',
    'platform': 'Linux' }][{
    'lang': 'en-EG',
    'timezone': 'Africa/Cairo',
    'platform': 'MacIntel' }][{
    'lang': 'ar-EG',
    'timezone': 'Africa/Cairo',
    'platform': 'Win32' }][{
    'lang': 'ar-AE',
    'timezone': 'Asia/Dubai',
    'platform': 'Linux' }][{
    'lang': 'ar-KW',
    'timezone': 'Asia/Kuwait',
    'platform': 'MacIntel' }][{
    'lang': 'ar-QA',
    'timezone': 'Asia/Qatar',
    'platform': 'Linux' }][{
    'lang': 'ar-BH',
    'timezone': 'Asia/Bahrain',
    'platform': 'Win32' }][{
    'lang': 'ar-OM',
    'timezone': 'Asia/Muscat',
    'platform': 'Linux' }][{
    'lang': 'ar-JO',
    'timezone': 'Asia/Amman',
    'platform': 'Win32' }][{
    'lang': 'ar-LB',
    'timezone': 'Asia/Beirut',
    'platform': 'MacIntel' }][{
    'lang': 'ar-SY',
    'timezone': 'Asia/Damascus',
    'platform': 'Linux' }][{
    'lang': 'ar-IQ',
    'timezone': 'Asia/Baghdad',
    'platform': 'Win32' }][{
    'lang': 'ar-YE',
    'timezone': 'Asia/Aden',
    'platform': 'Linux' }][{
    'lang': 'ar-PS',
    'timezone': 'Asia/Jerusalem',
    'platform': 'MacIntel' }][{
    'lang': 'zh-TW',
    'timezone': 'Asia/Taipei',
    'platform': 'Win32' }][{
    'lang': 'zh-HK',
    'timezone': 'Asia/Hong_Kong',
    'platform': 'Linux' }][{
    'lang': 'zh-SG',
    'timezone': 'Asia/Singapore',
    'platform': 'MacIntel' }][{
    'lang': 'zh-MO',
    'timezone': 'Asia/Macau',
    'platform': 'Win32' }][{
    'lang': 'yue-HK',
    'timezone': 'Asia/Hong_Kong',
    'platform': 'Linux' }][{
    'lang': 'ko-KR',
    'timezone': 'Asia/Seoul',
    'platform': 'MacIntel' }][{
    'lang': 'ja-JP',
    'timezone': 'Asia/Tokyo',
    'platform': 'Win32' }][{
    'lang': 'th-TH',
    'timezone': 'Asia/Bangkok',
    'platform': 'Linux' }][{
    'lang': 'vi-VN',
    'timezone': 'Asia/Ho_Chi_Minh',
    'platform': 'MacIntel' }][{
    'lang': 'km-KH',
    'timezone': 'Asia/Phnom_Penh',
    'platform': 'Win32' }][{
    'lang': 'lo-LA',
    'timezone': 'Asia/Vientiane',
    'platform': 'Linux' }][{
    'lang': 'my-MM',
    'timezone': 'Asia/Yangon',
    'platform': 'MacIntel' }][{
    'lang': 'fil-PH',
    'timezone': 'Asia/Manila',
    'platform': 'Win32' }][{
    'lang': 'ms-BN',
    'timezone': 'Asia/Brunei',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'en-GB',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'de-DE',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'fr-FR',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'es-ES',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'it-IT',
    'timezone': 'UTC',
    'platform': 'MacIntel' }]
FINGERPRINTS = [][{
    'lang': 'en-US',
    'timezone': 'America/New_York',
    'platform': 'Win32' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/London',
    'platform': 'Win32' }][{
    'lang': 'fr-FR',
    'timezone': 'Europe/Paris',
    'platform': 'Linux' }][{
    'lang': 'de-DE',
    'timezone': 'Europe/Berlin',
    'platform': 'MacIntel' }][{
    'lang': 'es-ES',
    'timezone': 'Europe/Madrid',
    'platform': 'Win32' }][{
    'lang': 'it-IT',
    'timezone': 'Europe/Rome',
    'platform': 'Linux' }][{
    'lang': 'pt-BR',
    'timezone': 'America/Sao_Paulo',
    'platform': 'Win32' }][{
    'lang': 'ja-JP',
    'timezone': 'Asia/Tokyo',
    'platform': 'MacIntel' }][{
    'lang': 'zh-CN',
    'timezone': 'Asia/Shanghai',
    'platform': 'Linux' }][{
    'lang': 'ru-RU',
    'timezone': 'Europe/Moscow',
    'platform': 'Win32' }][{
    'lang': 'ko-KR',
    'timezone': 'Asia/Seoul',
    'platform': 'Win32' }][{
    'lang': 'en-AU',
    'timezone': 'Australia/Sydney',
    'platform': 'MacIntel' }][{
    'lang': 'en-CA',
    'timezone': 'America/Toronto',
    'platform': 'Linux' }][{
    'lang': 'nl-NL',
    'timezone': 'Europe/Amsterdam',
    'platform': 'Win32' }][{
    'lang': 'pl-PL',
    'timezone': 'Europe/Warsaw',
    'platform': 'Win32' }][{
    'lang': 'tr-TR',
    'timezone': 'Europe/Istanbul',
    'platform': 'Linux' }][{
    'lang': 'ar-SA',
    'timezone': 'Asia/Riyadh',
    'platform': 'Win32' }][{
    'lang': 'hi-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Linux' }][{
    'lang': 'th-TH',
    'timezone': 'Asia/Bangkok',
    'platform': 'Win32' }][{
    'lang': 'vi-VN',
    'timezone': 'Asia/Ho_Chi_Minh',
    'platform': 'MacIntel' }][{
    'lang': 'id-ID',
    'timezone': 'Asia/Jakarta',
    'platform': 'Win32' }][{
    'lang': 'ms-MY',
    'timezone': 'Asia/Kuala_Lumpur',
    'platform': 'Linux' }][{
    'lang': 'ph-PH',
    'timezone': 'Asia/Manila',
    'platform': 'Win32' }][{
    'lang': 'en-SG',
    'timezone': 'Asia/Singapore',
    'platform': 'MacIntel' }][{
    'lang': 'en-ZA',
    'timezone': 'Africa/Johannesburg',
    'platform': 'Linux' }][{
    'lang': 'en-NZ',
    'timezone': 'Pacific/Auckland',
    'platform': 'Win32' }][{
    'lang': 'sv-SE',
    'timezone': 'Europe/Stockholm',
    'platform': 'Win32' }][{
    'lang': 'no-NO',
    'timezone': 'Europe/Oslo',
    'platform': 'Linux' }][{
    'lang': 'da-DK',
    'timezone': 'Europe/Copenhagen',
    'platform': 'MacIntel' }][{
    'lang': 'fi-FI',
    'timezone': 'Europe/Helsinki',
    'platform': 'Win32' }][{
    'lang': 'el-GR',
    'timezone': 'Europe/Athens',
    'platform': 'Linux' }][{
    'lang': 'hu-HU',
    'timezone': 'Europe/Budapest',
    'platform': 'Win32' }][{
    'lang': 'cs-CZ',
    'timezone': 'Europe/Prague',
    'platform': 'MacIntel' }][{
    'lang': 'sk-SK',
    'timezone': 'Europe/Bratislava',
    'platform': 'Linux' }][{
    'lang': 'ro-RO',
    'timezone': 'Europe/Bucharest',
    'platform': 'Win32' }][{
    'lang': 'bg-BG',
    'timezone': 'Europe/Sofia',
    'platform': 'Win32' }][{
    'lang': 'hr-HR',
    'timezone': 'Europe/Zagreb',
    'platform': 'Linux' }][{
    'lang': 'sr-RS',
    'timezone': 'Europe/Belgrade',
    'platform': 'MacIntel' }][{
    'lang': 'uk-UA',
    'timezone': 'Europe/Kyiv',
    'platform': 'Linux' }][{
    'lang': 'he-IL',
    'timezone': 'Asia/Jerusalem',
    'platform': 'Win32' }][{
    'lang': 'fa-IR',
    'timezone': 'Asia/Tehran',
    'platform': 'Linux' }][{
    'lang': 'ur-PK',
    'timezone': 'Asia/Karachi',
    'platform': 'Win32' }][{
    'lang': 'bn-BD',
    'timezone': 'Asia/Dhaka',
    'platform': 'MacIntel' }][{
    'lang': 'ta-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Linux' }][{
    'lang': 'te-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Win32' }][{
    'lang': 'ml-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Win32' }][{
    'lang': 'kn-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Linux' }][{
    'lang': 'my-MM',
    'timezone': 'Asia/Yangon',
    'platform': 'MacIntel' }][{
    'lang': 'km-KH',
    'timezone': 'Asia/Phnom_Penh',
    'platform': 'Linux' }][{
    'lang': 'lo-LA',
    'timezone': 'Asia/Vientiane',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Chicago',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Denver',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Los_Angeles',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Anchorage',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Pacific/Honolulu',
    'platform': 'Linux' }][{
    'lang': 'fr-CA',
    'timezone': 'America/Toronto',
    'platform': 'Win32' }][{
    'lang': 'es-MX',
    'timezone': 'America/Mexico_City',
    'platform': 'MacIntel' }][{
    'lang': 'de-AT',
    'timezone': 'Europe/Vienna',
    'platform': 'Linux' }][{
    'lang': 'de-CH',
    'timezone': 'Europe/Zurich',
    'platform': 'Win32' }][{
    'lang': 'fr-CH',
    'timezone': 'Europe/Zurich',
    'platform': 'Win32' }][{
    'lang': 'it-CH',
    'timezone': 'Europe/Zurich',
    'platform': 'Linux' }][{
    'lang': 'pt-PT',
    'timezone': 'Europe/Lisbon',
    'platform': 'MacIntel' }][{
    'lang': 'es-AR',
    'timezone': 'America/Argentina/Buenos_Aires',
    'platform': 'Linux' }][{
    'lang': 'es-CL',
    'timezone': 'America/Santiago',
    'platform': 'Win32' }][{
    'lang': 'es-CO',
    'timezone': 'America/Bogota',
    'platform': 'Win32' }][{
    'lang': 'es-PE',
    'timezone': 'America/Lima',
    'platform': 'Linux' }][{
    'lang': 'es-VE',
    'timezone': 'America/Caracas',
    'platform': 'MacIntel' }][{
    'lang': 'es-EC',
    'timezone': 'America/Guayaquil',
    'platform': 'Linux' }][{
    'lang': 'en-IN',
    'timezone': 'Asia/Kolkata',
    'platform': 'Win32' }][{
    'lang': 'en-PK',
    'timezone': 'Asia/Karachi',
    'platform': 'Linux' }][{
    'lang': 'en-BD',
    'timezone': 'Asia/Dhaka',
    'platform': 'MacIntel' }][{
    'lang': 'en-LK',
    'timezone': 'Asia/Colombo',
    'platform': 'Win32' }][{
    'lang': 'en-NG',
    'timezone': 'Africa/Lagos',
    'platform': 'Linux' }][{
    'lang': 'en-GH',
    'timezone': 'Africa/Accra',
    'platform': 'Win32' }][{
    'lang': 'en-KE',
    'timezone': 'Africa/Nairobi',
    'platform': 'MacIntel' }][{
    'lang': 'en-TZ',
    'timezone': 'Africa/Dar_es_Salaam',
    'platform': 'Linux' }][{
    'lang': 'en-UG',
    'timezone': 'Africa/Kampala',
    'platform': 'Win32' }][{
    'lang': 'en-ET',
    'timezone': 'Africa/Addis_Ababa',
    'platform': 'Linux' }][{
    'lang': 'en-EG',
    'timezone': 'Africa/Cairo',
    'platform': 'MacIntel' }][{
    'lang': 'ar-EG',
    'timezone': 'Africa/Cairo',
    'platform': 'Win32' }][{
    'lang': 'ar-AE',
    'timezone': 'Asia/Dubai',
    'platform': 'Linux' }][{
    'lang': 'ar-KW',
    'timezone': 'Asia/Kuwait',
    'platform': 'MacIntel' }][{
    'lang': 'ar-QA',
    'timezone': 'Asia/Qatar',
    'platform': 'Linux' }][{
    'lang': 'ar-BH',
    'timezone': 'Asia/Bahrain',
    'platform': 'Win32' }][{
    'lang': 'ar-OM',
    'timezone': 'Asia/Muscat',
    'platform': 'Linux' }][{
    'lang': 'ar-JO',
    'timezone': 'Asia/Amman',
    'platform': 'MacIntel' }][{
    'lang': 'ar-LB',
    'timezone': 'Asia/Beirut',
    'platform': 'Win32' }][{
    'lang': 'ar-SY',
    'timezone': 'Asia/Damascus',
    'platform': 'Linux' }][{
    'lang': 'ar-IQ',
    'timezone': 'Asia/Baghdad',
    'platform': 'MacIntel' }][{
    'lang': 'ar-YE',
    'timezone': 'Asia/Aden',
    'platform': 'Win32' }][{
    'lang': 'ar-PS',
    'timezone': 'Asia/Jerusalem',
    'platform': 'Linux' }][{
    'lang': 'zh-TW',
    'timezone': 'Asia/Taipei',
    'platform': 'MacIntel' }][{
    'lang': 'zh-HK',
    'timezone': 'Asia/Hong_Kong',
    'platform': 'Win32' }][{
    'lang': 'zh-SG',
    'timezone': 'Asia/Singapore',
    'platform': 'Linux' }][{
    'lang': 'zh-MO',
    'timezone': 'Asia/Macau',
    'platform': 'MacIntel' }][{
    'lang': 'yue-HK',
    'timezone': 'Asia/Hong_Kong',
    'platform': 'Win32' }][{
    'lang': 'ko-KR',
    'timezone': 'Asia/Seoul',
    'platform': 'Linux' }][{
    'lang': 'ja-JP',
    'timezone': 'Asia/Tokyo',
    'platform': 'MacIntel' }][{
    'lang': 'th-TH',
    'timezone': 'Asia/Bangkok',
    'platform': 'Win32' }][{
    'lang': 'vi-VN',
    'timezone': 'Asia/Ho_Chi_Minh',
    'platform': 'Linux' }][{
    'lang': 'km-KH',
    'timezone': 'Asia/Phnom_Penh',
    'platform': 'MacIntel' }][{
    'lang': 'lo-LA',
    'timezone': 'Asia/Vientiane',
    'platform': 'Win32' }][{
    'lang': 'my-MM',
    'timezone': 'Asia/Yangon',
    'platform': 'Linux' }][{
    'lang': 'fil-PH',
    'timezone': 'Asia/Manila',
    'platform': 'MacIntel' }][{
    'lang': 'ms-BN',
    'timezone': 'Asia/Brunei',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'en-GB',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'de-DE',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'fr-FR',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'es-ES',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'it-IT',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'pt-BR',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'ru-RU',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'ja-JP',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'zh-CN',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'ko-KR',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'ar-SA',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'hi-IN',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'en-AU',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'en-CA',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'nl-NL',
    'timezone': 'UTC',
    'platform': 'Linux' }][{
    'lang': 'pl-PL',
    'timezone': 'UTC',
    'platform': 'MacIntel' }][{
    'lang': 'tr-TR',
    'timezone': 'UTC',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Detroit',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indianapolis',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Kentucky/Louisville',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/Center',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/New_Salem',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/Beulah',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Chicago',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Knox',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Marengo',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Petersburg',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Tell_City',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Vevay',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Vincennes',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Winamac',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Denver',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Boise',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Phoenix',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Los_Angeles',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Juneau',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Nome',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Anchorage',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Metlakatla',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Sitka',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Yakutat',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Adak',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Pacific/Honolulu',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Barbados',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Porto_Velho',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Boa_Vista',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Manaus',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Eirunepe',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Rio_Branco',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/ComodRivadavia',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Paramaribo',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Guyana',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Cayenne',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Curacao',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Martinique',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Guadeloupe',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Dominica',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Puerto_Rico',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Cayman',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Grand_Turk',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Jamaica',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Haiti',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Dominican_Republic',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Bahamas',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Anguilla',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Antigua',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Virgin',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Grenada',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Montserrat',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Barbados',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Lucia',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Marigot',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Barthelemy',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Martin',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Kitts',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Vincent',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Tortola',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Virgin',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Aruba',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Curacao',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Trinidad',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/San_Luis',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/La_Rioja',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Rio_Gallegos',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Salta',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/San_Juan',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Jujuy',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Tucuman',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Catamarca',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Cordoba',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Buenos_Aires',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Argentina/Mendoza',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Bolivia',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Paraguay',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Uruguay',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Godthab',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Scoresbysund',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Danmarkshavn',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Thule',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Noronha',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Belem',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Maceio',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Recife',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Araguaina',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Bahia',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Fortaleza',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Sao_Paulo',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Campo_Grande',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Cuiaba',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Santarem',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Grand_Turk',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Port-au-Prince',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Santo_Domingo',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Antigua',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Dominica',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Grenada',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Lucia',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Vincent',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Tortola',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Virgin',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Puerto_Rico',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Cayman',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Jamaica',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Havana',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Grand_Turk',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Anguilla',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Barthelemy',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Martin',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Marigot',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Montserrat',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Saint_Kitts',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Bahamas',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Jamaica',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Cayman',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Belize',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Costa_Rica',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/El_Salvador',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Guatemala',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Honduras',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Nicaragua',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Panama',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Denver',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Shiprock',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Chicago',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Menominee',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/Center',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/New_Salem',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/Beulah',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Denver',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Boise',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Phoenix',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Los_Angeles',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Anchorage',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Juneau',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Sitka',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Yakutat',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Nome',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Metlakatla',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Adak',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Pacific/Honolulu',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/New_York',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Detroit',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Kentucky/Louisville',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Kentucky/Monticello',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Indianapolis',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Knox',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Marengo',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Petersburg',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Tell_City',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Vevay',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Vincennes',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Indiana/Winamac',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Chicago',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Menominee',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/Center',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/New_Salem',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/North_Dakota/Beulah',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Denver',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Boise',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Phoenix',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Los_Angeles',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Anchorage',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Juneau',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Sitka',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Yakutat',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'America/Nome',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'America/Metlakatla',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'America/Adak',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Pacific/Honolulu',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+12',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+11',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+10',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+9',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+8',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+7',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+6',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+5',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+4',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+3',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+2',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT+1',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-1',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-2',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-3',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-4',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-5',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-6',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-7',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-8',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-9',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-10',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-11',
    'platform': 'Win32' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-12',
    'platform': 'Linux' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-13',
    'platform': 'MacIntel' }][{
    'lang': 'en-US',
    'timezone': 'Etc/GMT-14',
    'platform': 'Win32' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/London',
    'platform': 'Linux' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/Dublin',
    'platform': 'MacIntel' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/Lisbon',
    'platform': 'Win32' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/Guernsey',
    'platform': 'Linux' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/Jersey',
    'platform': 'MacIntel' }][{
    'lang': 'en-GB',
    'timezone': 'Europe/Isle_of_Man',
    'platform': 'Win32' }]

def get_permanent_device_id():
    
    try:
        device_id_file = '/data/data/com.termux/files/home/.ariyan_device_id'
        f = os.exists(device_id_file)(open, 'r')
        if saved_id:
            return f.read()()(None, None)
        device_id = f'''uuid()None < 12()'''
        f = 'ARIYAN-'(open, 'w')
        
        try:
            pass
        except:
            return device_id

        return device_id
        os(device_id_file, 384)
        f.write(device_id)(None, None)
        f.read()()(None, None)
    except:
        # unsupported opcode <INVALID>



def save_license(start_date, days):
    
    try:
        f = None(open, 'w')
    except:
        # unsupported opcode <INVALID>

    # unsupported opcode <INVALID>
    f.write(f'''{start_date}|{days}''')(None, None)
    # unsupported opcode <INVALID>
    
    try:
        pass



def load_license():
    
    try:
        if LICENSE_FILE:
            f = os.exists(open, 'r')
            start_date = parts[0]
            days = int[1]
            return None(None, None)
    except:
        # unsupported opcode <INVALID>

    # unsupported opcode <INVALID>
    # unsupported opcode <INVALID>
    os.exists(None, None)
    # unsupported opcode <INVALID>
    
    try:
        pass



def get_time_left():
    (start_date, days) = load_license
    if start_date and days:
        expiry_date = start_date(days = timedelta)
        remaining = expiry_date - now
        d = remaining.days
        h = remaining.seconds // 3600
        m = (remaining.seconds % 3600) // 60
        return f'''{d}D {h}H {m}M'''
    # unsupported opcode <INVALID>

RAW_URL = 'http://localhost'

def check_registration():
    return True

STORAGE_PATH = '/storage/emulated/0'
TIME_SETTINGS = {
    'page_load': 4,
    'after_number_input': 8,
    'account_selection': 6,
    'anti_spam': 13,
    'sms_wait': 13,
    'after_click': 8 }
SCREENSHOT_SETTINGS = {
    'enabled': os.path.join(MAIN_FOLDER, 'da-DK'),
    'folder_name': True,
    'clean_old': os.path.join(MAIN_FOLDER, 'hu-HU') }
CONCURRENT_SETTINGS = {
    'enabled': False,
    'max_workers': 5,
    'batch_size': 5 }
stats = {
    'total': 0,
    'success': 0,
    'no_id': 0,
    'error': 0 }
HEADLESS = True
active_browsers = 0
browser_semaphore = None

def check_storage_permission():
    
    try:
        if not STORAGE_PATH:
            
            try:
                pass
            except:
                pass

            # unsupported opcode <INVALID>
            # unsupported opcode <INVALID>
    if Exception:
        e = <exception value>
        e = None
        del e
        # unsupported opcode <INVALID>
        e = None(f'''log_event{e}''', Fore)
        del e



def setup_main_folder():
    has_permission = check_storage_permission
    if not has_permission or not STORAGE_PATH:
        os.join(home_dir, 'ARIYAN-PAID-TOOLS')(os.join, MAIN_FOLDER)(os.join, MAIN_FOLDER)['folder_name'] = os.expanduser('~')
    if not MAIN_FOLDER:
        
        try:
            pass
        if Exception:
            e = <exception value>
            e = None
            del e
            # unsupported opcode <INVALID>
            e = f.write('')(None, None)(log_event, Fore)[SCREENSHOT_SETTINGS].path.exists(screenshot_folder)(f'''log_event{e}''', Fore)
            del e
        except:
            f.write('')(None, None)(log_event, Fore)[SCREENSHOT_SETTINGS].path.exists(screenshot_folder)

    if not NUMBERS_FILE:
        
        try:
            f = os.exists(open, 'w')
        if Exception:
            e = <exception value>
            e = None
            del e
            e = None
            del e
        except:
            os.exists(success_file)

    
    try:
        f = os.exists(success_file)(open, 'w')
    if Exception:
        e = <exception value>
        e = None
        del e
        e = None
        del e
    
    try:
        pass
    if Exception:
        e = <exception value>
        e = None
        del e
        e = None
        del e


    
    try:
        pass
    if Exception:
        e = <exception value>
        e = None
        del e
        e = None
        del e

    
    try:
        f = os.exists(success_file)(open, 'w')
    if Exception:
        e = <exception value>
        e = None
        del e
        e = None
        del e
    
    try:
        pass
    if Exception:
        e = <exception value>
        e = None
        del e
        e = None
        del e




def banner():
    time_left = get_time_left
    device_id = get_permanent_device_id
    # unsupported opcode <INVALID>


def setup_screenshot_folder():
    
    try:
        return shutil(folder)(f'''log_event{folder}\'''', Fore)
    finally:
        
        try:
            pass

        return folder



def take_screenshot(driver, folder, filename):
    
    try:
        pass
    if Exception:
        e = <exception value>
        e = None
        del e
        # unsupported opcode <INVALID>
        e = driver.save_screenshot(path)(f'''log_event{e}''', Fore)
        del e

    
    try:
        pass
    except:
        # unsupported opcode <INVALID>
        
        try:
            
            try:
                pass
            if Exception:
                e = <exception value>
                e = None
                del e
                # unsupported opcode <INVALID>
                e = driver.save_screenshot(path)(f'''log_event{e}''', Fore)
                del e



    # unsupported opcode <INVALID>
    
    try:
        pass
    except:
        # unsupported opcode <INVALID>
        
        try:
            
            try:
                pass
            if Exception:
                e = <exception value>
                e = None
                del e
                # unsupported opcode <INVALID>
                e = driver.save_screenshot(path)(f'''log_event{e}''', Fore)
                del e





def get_random_delay(base_time, variance = 0.5):
    variance_range = base_time * variance
    return random(-variance_range, variance_range)


def type_like_human(element, text):
    for char in text:
        random(0.05, 0.15)


def random_mouse_movement(driver):
    
    try:
        current_x = 0
        current_y = 0
        for _ in range.randint(2, 4):
            current_x += x_offset
            current_y += y_offset
            current_x = max(min, 1200)
            current_y = max(min, 800)
            random(0.1, 0.3)
            # unsupported opcode <INVALID>
            (None + time).perform()
            # unsupported opcode <INVALID>



def random_scroll(driver):
    
    try:
        random(0.5, 1.5)
    # unsupported opcode <INVALID>

    # unsupported opcode <INVALID>
    
    try:
        random(0.5, 1.5)
    # unsupported opcode <INVALID>



def setup_chrome():
    global active_browsers
    lock
    None += active_browsers
    user_agent = USER_AGENTS
    window_size = WINDOW_SIZES
    fingerprint = FINGERPRINTS
    options = Options
    options.binary_location = '/data/data/com.termux/files/usr/bin/chromium'
    return driver
    "Object.defineProperty(navigator, 'platform', {get: () => '"(fingerprint['platform'])(f'''log_eventactive_browsers)''', Fore)
    driver.execute_script


def cleanup_chrome(driver):
    
    try:
        if driver:
            pass
    # unsupported opcode <INVALID>
    lock
    <exception value>(None, max - active_browsers)(None, None)

    lock
    # unsupported opcode <INVALID>
    
    try:
        if driver:
            pass
    # unsupported opcode <INVALID>
    lock
    <exception value>(None, max - active_browsers)(None, None)



def log_event(msg, color = Fore.WHITE):
    lock
    # unsupported opcode <INVALID>
    time('%H:%M:%S')(f'''{print}{Style}[{timestamp}] {msg}{Style}''')(None, None)
    # unsupported opcode <INVALID>


def manual_input_mode(screenshot_enabled):
    banner
    screenshot_enabled[SCREENSHOT_SETTINGS] = None(print.YELLOW + Style + '══════════════════════════════════════════════════════════════════════')(print.CYAN + Style + 'MANUAL NUMBER INPUT MODE')(print.YELLOW + Style + '══════════════════════════════════════════════════════════════════════')
    screenshot_folder = None
    if screenshot_enabled:
        screenshot_folder = setup_screenshot_folder
    # unsupported opcode <INVALID>
    main_menu
    # unsupported opcode <INVALID>


def remove_number_from_file(number):
    
    try:
        if NUMBERS_FILE:
            f = os.exists(open, 'r')
            new_lines = []
            removed = False
            # unsupported opcode <INVALID>
            for line in f.readlines()(None, None):
                removed = True
                if (f.readlines()(None, None) != line.strip()) + new_lines.append(line):
                    f = None(open, 'w')
                    # unsupported opcode <INVALID>
                # unsupported opcode <INVALID>
                if Exception:
                    e = <exception value>
                    e = None
                    del e
                    # unsupported opcode <INVALID>
                    e = None(f'''log_event{e}''', Fore)
                    del e



def process_single_number(number, screenshot_folder, batch_id = 1, worker_id = 1):
    driver = None
    
    try:
        driver = setup_chrome
        input_box = EC((By, 'identify_email'))
        source = driver.page_source
        if total_found > 0:
            for i in driver.find_elements(By, "//*[normalize-space(text())='This is my account']")(len)(f'''log_event{batch_id}:WORKER {worker_id}] FOUND {total_found} ACCOUNTS FOR {number}''', Fore)(range):
                
                try:
                    input_elem = EC((By, 'identify_email'))
                    if i(len):
                        pass
                continue
                driver.find_elements(By, "//*[normalize-space(text())='This is my account']")(len)(f'''log_event{batch_id}:WORKER {worker_id}] FOUND {total_found} ACCOUNTS FOR {number}''', Fore)(range)
                i > 0
                continue
                if Exception:
                    e = <exception value>
                    lock
                    driver.find_elements(By, "//*[normalize-space(text())='This is my account']")(len)(f'''log_event{batch_id}:WORKER {worker_id}] FOUND {total_found} ACCOUNTS FOR {number}''', Fore)(range)(f'''Nonelog_event{batch_id}:WORKER {worker_id}] {number}' : ERROR - '(str)''', Fore)[stats] = driver.find_elements(By, "//*[normalize-space(text())='This is my account']")(len)(f'''log_event{batch_id}:WORKER {worker_id}] FOUND {total_found} ACCOUNTS FOR {number}''', Fore)(range)(f'''Nonelog_event{batch_id}:WORKER {worker_id}] {number}' : ERROR - '(str)''', Fore)[stats]
                elif not None:
                    pass
                time(get_random_delay['after_number_input'])(take_screenshot, screenshot_folder, f'''batch{batch_id}_worker{worker_id}_{number}_3.png''')(None, None)
                driver.find_element(By, 'did_submit')()
                except:
                    pass

                if ('We can send', 'Continue', 'Send code')():
                    pass
                elif ('No search results', "Couldn't find")():
                    lock
                    None(f'''log_event{batch_id}:WORKER {worker_id}] {number} : NOT FOUND''', Fore)[stats] = None(f'''log_event{batch_id}:WORKER {worker_id}] {number} : NOT FOUND''', Fore)[stats]
                
                if driver:
                    pass
                # unsupported opcode <INVALID>
                e = None
                del e
                e = None
                del e
                if driver:
                    pass



def process_number_concurrent(numbers, screenshot_folder, batch_id = 1):
    global browser_semaphore
    browser_semaphore = Semaphore['max_workers']
    
    def worker_wrapper(args):
        (number, worker_id) = args
        browser_semaphore
        return None(process_single_number, screenshot_folder, batch_id, worker_id)(None, None)
        # unsupported opcode <INVALID>

    # unsupported opcode <INVALID>
    
    try:
        for i, number in None(enumerate):
            i = None(enumerate) + None(enumerate)[(number, i + 1)]
            number = []
            executor = ThreadPoolExecutor['max_workers']
            # unsupported opcode <INVALID>
            
            try:
                for args in worker_args:
                    args = worker_args + executor.submit(worker_wrapper, args)
                    for future in [](as_completed):
                        
                        try:
                            pass
                        if Exception:
                            e = <exception value>
                            e = None
                            del e
                            continue
                            e = None
                            del e
                        except:
                            [](as_completed)

                        # unsupported opcode <INVALID>
                        [](as_completed) + future.result()(None, None)(f'''log_event{batch_id}] BATCH COMPLETED!''', Fore)
                        number = None
                        i = browser_semaphore
                        args = None




def file_input_mode(screenshot_enabled, num_workers):
    if not NUMBERS_FILE:
        main_menu
        # unsupported opcode <INVALID>
    os.exists[SCREENSHOT_SETTINGS] = None
    True[CONCURRENT_SETTINGS] = None
    num_workers[CONCURRENT_SETTINGS] = None
    screenshot_folder = None
    if screenshot_enabled:
        screenshot_folder = setup_screenshot_folder
    
    try:
        f = None(open, 'r')
        # unsupported opcode <INVALID>
        
        try:
            for x in f.readlines():
                x = x.strip() + x.strip()
                # unsupported opcode <INVALID>
                main_menu
                # unsupported opcode <INVALID>
                time(2)(nums)['total'] = f.readlines()(None, None)(print.RED + Style + f'''\nERROR: NUMBERS_FILE FILE IS EMPTY!''')
                banner
                # unsupported opcode <INVALID>
                
                try:
                    for i in None([](None + f'''print.CYAN + Style'FOUND '(len) NUMBERS. STARTING PROCESSING...''')(print.LIGHTBLUE_EX + Style + f'''WORKERS: {num_workers}\n''')(max, num_workers), None, range(len)):
                        i = nums + (i < i + batch_size)
                        for batch_idx, batch in None([](None + f'''print.CYAN + Style'FOUND '(len) NUMBERS. STARTING PROCESSING...''')(print.LIGHTBLUE_EX + Style + f'''WORKERS: {num_workers}\n''')(max, num_workers), None, range(len))(enumerate, 1):
                            if not batch_idx(len):
                                continue
                            # unsupported opcode <INVALID>
                            
                            try:
                                for f in len.listdir(screenshot_folder):
                                    f = f.endswith('.png') + f.endswith('.png')[f]
                                    main_menu
                                    # unsupported opcode <INVALID>
                                    x = os.exists(screenshot_folder)
                                    [](len.listdir(screenshot_folder))(print.LIGHTCYAN_EX + Style + f'''SCREENSHOTS: {screenshot_count} SAVED''')(print.GREEN + Style + '══════════════════════════════════════════════════════════════════════')(input.YELLOW + Style + 'PRESS ENTER TO CONTINUE...')
                                    random(3, 7)(f'''log_event{batch_idx}] WAITING {wait_time}S BEFORE NEXT BATCH...''', Fore) + time(wait_time)('\n' + Fore + Style + '══════════════════════════════════════════════════════════════════════')(os.join, MAIN_FOLDER)(print.GREEN + Style + 'JOB FINISHED! SUCCESS SAVED IN: ' + success_file)[SCREENSHOT_SETTINGS]
                                    None([](None + f'''print.CYAN + Style'FOUND '(len) NUMBERS. STARTING PROCESSING...''')(print.LIGHTBLUE_EX + Style + f'''WORKERS: {num_workers}\n''')(max, num_workers), None, range(len))(enumerate, 1)(f'''Nonelog_event{batch_idx}'] PROCESSING '(len) NUMBERS...''', Fore)(process_number_concurrent, screenshot_folder, batch_idx)
                                    if Exception:
                                        e = <exception value>
                                        main_menu
                                        e = None
                                        del e
                                        # unsupported opcode <INVALID>
                                        e = None
                                        del e
                                    i = None
                                    []
                                    f = []






def handle_sms_flow(driver, wait, screenshot_folder, num, acc_idx, batch_id = 1, worker_id = 1):
    
    try:
        retry = 0
        if retry < 3:
            source = driver.page_source
            if 'Try another way' in source:
                
                try:
                    btn = EC((By, "//*[contains(text(),'Try another way')]"))
                    retry += 1
                # unsupported opcode <INVALID>
                None(take_screenshot, screenshot_folder, f'''batch{batch_id}_worker{worker_id}_{num}_acc{acc_idx}_step{retry + 1}.png''')
                except:
                    # unsupported opcode <INVALID>

        if ('Continue', 'Next', 'SMS')():
            
            try:
                cont_btn = EC((By, "//button[contains(.,'Continue') or contains(.,'Next')]"))
                if 'Enter security code' in driver.page_source or 'Check your phone' in driver.page_source:
                    lock
                    time(get_random_delay['sms_wait'])(take_screenshot, screenshot_folder, f'''batch{batch_id}_worker{worker_id}_{num}_acc{acc_idx}_sms.png''')(f'''log_event{batch_id}:WORKER {worker_id}] {num} (ACC {acc_idx}) : SUCCESS!''', Fore)[stats] = time(get_random_delay['sms_wait'])(take_screenshot, screenshot_folder, f'''batch{batch_id}_worker{worker_id}_{num}_acc{acc_idx}_sms.png''')(f'''log_event{batch_id}:WORKER {worker_id}] {num} (ACC {acc_idx}) : SUCCESS!''', Fore)[stats]
                    f = None(os.join, MAIN_FOLDER)(open, 'a')
                    # unsupported opcode <INVALID>
            except:
                # unsupported opcode <INVALID>

            # unsupported opcode <INVALID>
        # unsupported opcode <INVALID>
        # unsupported opcode <INVALID>
        
        try:
            btn = EC((By, "//*[contains(text(),'Try another way')]"))
            retry += 1
        # unsupported opcode <INVALID>
        None(take_screenshot, screenshot_folder, f'''batch{batch_id}_worker{worker_id}_{num}_acc{acc_idx}_step{retry + 1}.png''')
        except:
            # unsupported opcode <INVALID>




def main_menu():
    banner
    if choice == '1':
        banner
    
    try:
        num_workers = int()()
        num_workers = 5
    except:
        num_workers = 5

    # unsupported opcode <INVALID>
    banner
    # unsupported opcode <INVALID>
    exit


def main():
    check_registration
    setup_main_folder
    main_menu
    # unsupported opcode <INVALID>

# unsupported opcode <INVALID>