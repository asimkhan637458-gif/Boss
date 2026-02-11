import os
import hashlib
import requests
import sys
import urllib.parse
import time

# --- SETTINGS ---
# Aapka GitHub RAW link maine add kar diya hai
APPROVAL_URL = "https://raw.githubusercontent.com/asimkhan637458-gif/Aprowl.txt/e8286a726e18ee631f4153c303455ade46274333/Aprowl.txt"
OWNER_NUMBER = "+923207706955"

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

def FOZI_BOSS_APPROVAL():
    ____banner____()
    # Unique HWID generation based on device name and login
    try:
        device_info = os.popen('getprop ro.product.model').read().strip() + os.getlogin()
    except:
        device_info = "DEVICE" + str(os.getuid())
        
    hwid = hashlib.sha256(device_info.encode()).hexdigest().upper()[:12]
    
    print(f"\033[1;32m [●] YOUR UNIQUE KEY : {hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        # GitHub se approval check karna
        response = requests.get(APPROVAL_URL)
        approved_keys = response.text
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME FOZI BOSS.")
            time.sleep(2)
        else:
            print("\033[1;31m [×] YOUR KEY IS NOT APPROVED!")
            print("\033[1;36m [!] REDIRECTING TO OWNER ON WHATSAPP...")
            time.sleep(3)
            
            # Auto WhatsApp message formatting
            msg = f"Assalam-o-Alaikum FOZI BOSS, Please Approve My Key\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            
            # Open WhatsApp
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except Exception as e:
        print("\033[1;31m [!] SERVER ERROR! Check your connection.")
        sys.exit()

# Script execution
if __name__ == '__main__':
    FOZI_BOSS_APPROVAL()
    # Yahan se aapka cloning wala BNG_71_() function start hoga
