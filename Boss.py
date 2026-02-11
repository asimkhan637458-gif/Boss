import os
import hashlib
import requests
import sys
import urllib.parse
import time

# --- CONFIGURATION ---
# Aapka GitHub RAW link
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
    
    # --- STRICT HWID GENERATION ---
    # Yeh logic har device ke liye unique key banaye ga
    try:
        # Device information aur unique system ID ka milap
        device_data = os.popen('getprop ro.product.model').read().strip() + os.getlogin() + str(os.getuid())
    except:
        device_data = "FOZI_FIXED_" + str(os.getuid())
        
    # Unique 12-digit key generate karna
    hwid = hashlib.sha256(device_data.encode()).hexdigest().upper()[:12]
    
    print(f"\033[1;36m [●] DEVICE KEY : \033[1;37m{hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[1;35m [!] STATUS     : \033[1;37mVerifying Online Access...")
    
    try:
        # GitHub server se live check
        # Timeout isliye taake agar internet slow ho to script hang na ho
        response = requests.get(APPROVAL_URL, timeout=10)
        approved_keys = response.text
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME BOSS.")
            time.sleep(2)
        else:
            # Agar key GitHub file mein nahi hai
            print("\033[1;31m [×] ACCESS DENIED! YOUR KEY IS NOT IN SERVER.")
            print("\033[1;32m [→] OPENING WHATSAPP FOR APPROVAL...")
            time.sleep(3)
            
            # WhatsApp message setup
            msg = f"Assalam-o-Alaikum FOZI BOSS,\n\nMeri Key Approve Kar Dein.\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            
            # WhatsApp redirect logic
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except requests.exceptions.RequestException:
        print("\033[1;31m [!] ERROR: INTERNET YA SERVER KA MASLA HAI!")
        sys.exit()

if __name__ == '__main__':
    # Yeh function ab lazmi har device par chale ga
    FOZI_BOSS_APPROVAL()
    
    # Iske niche aapka baki ka cloning code aayega
    print("\033[1;32m [●] SUCCESS: LOADING CLONING MODULES...")
