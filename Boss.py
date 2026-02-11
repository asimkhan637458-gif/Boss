import os
import hashlib
import requests
import sys
import urllib.parse
import time

# --- CONFIGURATION ---
# Yaad rakhein: Link hamesha RAW wala hona chahiye
APPROVAL_URL = "https://raw.githubusercontent.com/asimkhan637458-gif/Aprowl.txt/main/Aprowl.txt"
OWNER_NUMBER = "+923207706955"

def FOZI_BOSS_APPROVAL():
    os.system('clear')
    # Unique HWID generation
    try:
        device_data = os.popen('getprop ro.product.model').read().strip() + os.getlogin() + str(os.getuid())
    except:
        device_data = "FOZI_DEVICE_" + str(os.getuid())
        
    hwid = hashlib.sha256(device_data.encode()).hexdigest().upper()[:12]
    
    print(f"\033[1;32m [●] YOUR KEY : {hwid}")
    print("\033[1;33m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        # GitHub se data fetch karna
        response = requests.get(APPROVAL_URL, timeout=15)
        # .strip() aur .upper() lagaya hai taake space ka masla na ho
        approved_keys = response.text.upper().strip()
        
        if hwid in approved_keys:
            print("\033[1;32m [✔] ACCESS GRANTED! WELCOME BOSS.")
            time.sleep(2)
        else:
            print("\033[1;31m [×] KEY NOT FOUND IN SERVER.")
            print("\033[1;36m [!] REDIRECTING TO WHATSAPP...")
            time.sleep(2)
            
            msg = f"Assalam-o-Alaikum FOZI BOSS, Approve My Key\nKey: {hwid}"
            encoded_msg = urllib.parse.quote(msg)
            os.system(f'xdg-open https://wa.me/{OWNER_NUMBER}?text={encoded_msg}')
            sys.exit()
            
    except:
        print("\033[1;31m [!] INTERNET ERROR OR SERVER BUSY!")
        sys.exit()

if __name__ == '__main__':
    FOZI_BOSS_APPROVAL()
    # Aapka BNG_71_() yahan se shuru hoga
