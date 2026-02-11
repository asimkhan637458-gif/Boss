import os
import hashlib
import requests
import sys
import urllib.parse
import time

# --- CONFIGURATION ---
# Aapki GitHub file ka RAW link
APPROVAL_URL = "https://raw.githubusercontent.com/asimkhan637458-gif/Aprowl.txt/e8286a726e18ee631f4153c303455ade46274333/Aprowl.txt"
OWNER_NUMBER = "+923207706955"

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
    
    # Har device ki unique key generator (Isay koi bypass nahi kar sakta)
    try:
        # Device model aur login name ko mila kar key banana
        device_data = os.popen('getprop ro.product.model').read().strip() + os.getlogin() + str(os.getuid())
    except:
        device_data = "FOZI_DEVICE_" + str(os.getuid())
        
    # Unique 12 digit key
    hwid = hashlib.sha256(device_data.encode()).hexdigest().upper()[:12]
    
    print(f"\033[1;36m [●] DEVICE KEY : \033[1;37m{hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;35m [!] STATUS : \033[1;37mVerifying Access...")
    
    try:
        # Direct GitHub se check karna (Koi local bypass file nahi)
        response = requests.get(APPROVAL_URL, timeout=10)
        approved_keys = response.text
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME BOSS.")
            time.sleep(2)
        else:
            print("\033[1;31m [×] YOUR DEVICE IS NOT APPROVED!")
            print("\033[1;32m [→] REDIRECTING TO FOZI BOSS FOR KEY...")
            time.sleep(3)
            
            # Auto message for WhatsApp
            msg = f"Assalam-o-Alaikum FOZI BOSS,\n\nMera Device Approve Nahi Hai.\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            
            # WhatsApp Redirect
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except requests.exceptions.RequestException:
        print("\033[1;31m [!] SERVER DOWN OR NO INTERNET!")
        sys.exit()

# Main logic
if __name__ == '__main__':
    # Yeh function ab har baar chale ga, koi bhi device ho
    FOZI_BOSS_APPROVAL()
    
    # Iske niche aapka cloning wala BNG_71_() ya baaki code aayega
    print("\033[1;32m [●] SCRIPT STARTED SUCCESSFULLY...")
