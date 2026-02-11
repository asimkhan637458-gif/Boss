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

# --- APPROVAL SYSTEM CONFIG ---
# Aapka GitHub RAW link yahan hona chahiye
APPROVAL_URL = "https://raw.githubusercontent.com/asimkhan637458-gif/Aprowl.txt/main/Aprowl.txt"
OWNER_NUMBER = "+923207706955"

def FOZI_BOSS_APPROVAL():
    os.system('clear')
    ____banner____()
    
    # Unique Hardware ID Generation
    try:
        device_id = str(os.getlogin()) + str(os.getuid())
    except:
        device_id = str(os.cpu_count()) + str(os.name)
        
    hwid = hashlib.sha256(device_id.encode()).hexdigest().upper()[:15]
    
    print(f'      \x1b[38;5;46m YOUR UNIQUE KEY : \x1b[1;37m{hwid}')
    linex()
    print('       \x1b[38;5;196m[!] STATUS : \x1b[1;37mChecking Server Approval...')
    
    try:
        # GitHub se data fetch karna
        response = requests.get(APPROVAL_URL).text
        if hwid in response:
            print('       \x1b[38;5;46m[✔] ACCESS GRANTED! WELCOME BOSS.')
            time.sleep(2)
        else:
            print('       \x1b[38;5;196m[×] KEY NOT APPROVED.')
            print(f'       \x1b[38;5;46m REDIRECTING TO OWNER FOR APPROVAL...')
            time.sleep(3)
            
            # WhatsApp Auto-Open with Dynamic Message
            msg = f"Assalam-o-Alaikum FOZI BOSS, Please Approve My Key: {hwid}"
            url_msg = urllib.parse.quote(msg)
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={url_msg}')
            sys.exit()
            
    except requests.exceptions.ConnectionError:
        print('       \x1b[38;5;196m[!] CHECK YOUR INTERNET CONNECTION.')
        sys.exit()

# --- PREVIOUS LOGO & SYSTEM ---
def ____banner____():
    if 'win' in sys.platform: os.system('cls')
    else: os.system('clear')
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

def linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# --- YAHAN SE AAPKA BAAKI CODE (login_1, login_2, old_clone) START HOGA ---
# (Apna purana cloning wala saara code yahan niche paste kar dein)

if __name__ == '__main__':
    FOZI_BOSS_APPROVAL() # Sab se pehle approval check
    # BNG_71_() # Phir main menu (Aapke main menu function ka naam)
