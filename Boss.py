import os
import hashlib
import requests
import sys
import urllib.parse
import time

# --- UPDATED CONFIGURATION ---
# Maine aapke naye link ko RAW format mein convert kar diya hai
APPROVAL_URL = "https://raw.githubusercontent.com/asimkhan637458-gif/Aprowl.txt/main/Aprowl.txt"
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
    
    # Unique HWID Generation (Strict for every device)
    try:
        device_data = os.popen('getprop ro.product.model').read().strip() + os.getlogin() + str(os.getuid())
    except:
        device_data = "FOZI_FIXED_" + str(os.getuid())
        
    hwid = hashlib.sha256(device_data.encode()).hexdigest().upper()[:12]
    
    print(f"\033[1;36m [●] DEVICE KEY : \033[1;37m{hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;35m [!] STATUS     : \033[1;37mSyncing with Server...")
    
    try:
        # Live checking from GitHub Raw
        response = requests.get(APPROVAL_URL, timeout=10)
        approved_keys = response.text.upper()
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME BOSS.")
            time.sleep(2)
        else:
            print("\033[1;31m [×] ACCESS DENIED! KEY NOT APPROVED.")
            print("\033[1;32m [→] REDIRECTING TO OWNER ON WHATSAPP...")
            time.sleep(3)
            
            # WhatsApp Auto-Message
            msg = f"Assalam-o-Alaikum FOZI BOSS,\n\nMeri Key Approve Kar Dein.\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except requests.exceptions.RequestException:
        print("\033[1;31m [!] ERROR: NO INTERNET OR SERVER TIMEOUT!")
        sys.exit()

if __name__ == '__main__':
    FOZI_BOSS_APPROVAL()
    # Yahan se aapka purana cloning code BNG_71_() start hoga
    print("\033[1;32m [●] SCRIPT LOADING...")
