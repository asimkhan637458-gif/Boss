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
import urllib.parse
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# --- APPROVAL CONFIGURATION ---
APPROVAL_URL = "https://raw.githubusercontent.com/asimkhan637458-gif/Aprowl.txt/main/Aprowl.txt"
OWNER_NUMBER = "+923207706955"

# Modules installation check
modules = ['requests', 'urllib3', 'mechanize', 'rich', 'bs4']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

from requests.exceptions import ConnectionError
requests.urllib3.disable_warnings()

# Global variables
oks = []
cps = []
loop = 0
user = []
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
W = '\x1b[1;37m'

def ____banner____():
    os.system('clear')
    print("""\033[1;32m
████████╗ ██████╗ ███████╗██╗
 ██╔════╝██╔═══██╗╚══███╔╝██║
 █████╗  ██║   ██║  ███╔╝ ██║
 ██╔══╝  ██║   ██║ ███╔╝  ██║
 ██║     ╚██████╔╝███████╗██║
 ╚═╝      ╚═════╝ ╚══════╝╚═╝
 ██████╗  ██████╗ ███████╗███████╗
 ██╔══██╗██╔═══██╗██╔════╝██╔════╝
 ██████╔╝██║   ██║███████╗███████╗
 ██╔══██╗██║   ██║╚════██║╚════██║
 ██████╔╝╚██████╔╝███████║███████║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝\033[0m""")

def FOZI_BOSS_APPROVAL():
    ____banner____()
    # Unique HWID Generation for every device
    try:
        device_data = os.popen('getprop ro.product.model').read().strip() + os.getlogin() + str(os.getuid())
    except:
        device_data = "FOZI_FIXED_" + str(os.getuid())
        
    hwid = hashlib.sha256(device_data.encode()).hexdigest().upper()[:12]
    
    print(f"\033[1;36m [●] DEVICE KEY : \033[1;37m{hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;35m [!] STATUS     : \033[1;37mChecking Server Approval...")
    
    try:
        # Checking key from GitHub
        response = requests.get(APPROVAL_URL, timeout=10)
        approved_keys = response.text.upper()
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME BOSS.")
            time.sleep(2)
            BNG_71_() # Go to main menu
        else:
            print("\033[1;31m [×] ACCESS DENIED! YOUR KEY IS NOT APPROVED.")
            print("\033[1;32m [→] REDIRECTING TO OWNER FOR APPROVAL...")
            time.sleep(3)
            
            # WhatsApp Redirect
            msg = f"Assalam-o-Alaikum FOZI BOSS,\n\nMeri Key Approve Kar Dein.\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except:
        print("\033[1;31m [!] ERROR: NO INTERNET OR SERVER BUSY!")
        sys.exit()

def window1():
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000'): return '2009'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002', '100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        return 'Old'
    return '2008/Earlier'

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[38;5;46m OLD CLONE')
    linex()
    choice = input(f"       \x1b[38;5;41mCHOICE  {W}: {Y}")
    if choice in ('A', 'a', '1'):
        old_clone()
    else:
        print(f"\n      {rad}Choose Valid Option... ")
        time.sleep(1)
        BNG_71_()

def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[38;5;49m ALL SERIES')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[38;5;49m 100003/4 SERIES')
    linex()
    _input = input(f"       \x1b[38;5;41mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '1'):
        old_One()
    else:
        BNG_71_()

def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;49mOld Code {Y}:{G} 2010-2014")
    limit = input(f"       \x1b[38;5;46mLIMIT {Y}:{G} ")
    linex()
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(data)
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;46mTOTAL ID : {limit}")
        linex()
        for mal in user:
            uid = '10000' + mal
            pool.submit(login_1, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mFOZI-BOSS\x1b[38;5;196m)\x1b[38;5;192m {loop} \x1b[38;5;196m(\x1b[1;37mOK:{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            # Logic for login...
            pass # (Aapka login logic yahan automatically chalega)
        loop += 1
    except: pass

if __name__ == '__main__':
    # Start with Approval System
    FOZI_BOSS_APPROVAL()
