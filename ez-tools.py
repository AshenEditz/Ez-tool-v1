#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════╗
║                    EZ TOOLS BY ASHEN EDITZ                    ║
║                   Contact: 0726962974                         ║
║              GitHub: github.com/asheneditz                   ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import socket
import requests
import hashlib
import base64
import json
import subprocess
import platform
from datetime import datetime

# Colors
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'

R = Colors.RED
G = Colors.GREEN
Y = Colors.YELLOW
B = Colors.BLUE
P = Colors.PURPLE
C = Colors.CYAN
W = Colors.WHITE
O = Colors.ORANGE
BOLD = Colors.BOLD
RESET = Colors.RESET

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"""{C}
    ╔═══════════════════════════════════════════════════════════════╗
    ║{R}  ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗{C}║
    ║{R}  ██╔════╝╚══███╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝{C}║
    ║{G}  █████╗    ███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗{C}║
    ║{G}  ██╔══╝   ███╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║{C}║
    ║{Y}  ███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║{C}║
    ║{Y}  ╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{C}║
    ╠═══════════════════════════════════════════════════════════════╣
    ║{W}                  ★ CODED BY: ASHEN EDITZ ★                    {C}║
    ║{W}                  ★ CONTACT: 0726962974 ★                      {C}║
    ║{W}                  ★ VERSION: 2.0 PREMIUM ★                     {C}║
    ╚═══════════════════════════════════════════════════════════════╝{RESET}
    """)

def loading_animation(text, duration=2):
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{C}[{animation[i % len(animation)]}] {text}{RESET}", end="")
        time.sleep(0.1)
        i += 1
    print(f"\r{G}[✓] {text} - Complete!{RESET}")

def type_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# ═══════════════════════════════════════════════════════════
#                    INFORMATION GATHERING
# ═══════════════════════════════════════════════════════════

def ip_tracker():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        🌐 IP ADDRESS TRACKER 🌐        {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    ip = input(f"{G}[+] Enter IP Address: {W}")
    loading_animation("Tracking IP Address")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{C}╔═══════════════════════════════════════╗")
            print(f"║{Y}           IP INFORMATION               {C}║")
            print(f"╠═══════════════════════════════════════╣")
            print(f"║{G} IP Address  : {W}{data.get('query', 'N/A'):<21}{C}║")
            print(f"║{G} Country     : {W}{data.get('country', 'N/A'):<21}{C}║")
            print(f"║{G} Region      : {W}{data.get('regionName', 'N/A'):<21}{C}║")
            print(f"║{G} City        : {W}{data.get('city', 'N/A'):<21}{C}║")
            print(f"║{G} ZIP Code    : {W}{data.get('zip', 'N/A'):<21}{C}║")
            print(f"║{G} Latitude    : {W}{str(data.get('lat', 'N/A')):<21}{C}║")
            print(f"║{G} Longitude   : {W}{str(data.get('lon', 'N/A')):<21}{C}║")
            print(f"║{G} Timezone    : {W}{data.get('timezone', 'N/A'):<21}{C}║")
            print(f"║{G} ISP         : {W}{data.get('isp', 'N/A')[:21]:<21}{C}║")
            print(f"║{G} Organization: {W}{data.get('org', 'N/A')[:21]:<21}{C}║")
            print(f"╚═══════════════════════════════════════╝{RESET}")
        else:
            print(f"{R}[✗] Failed to track IP address!{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def phone_lookup():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}       📱 PHONE NUMBER LOOKUP 📱        {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
        
        phone = input(f"{G}[+] Enter Phone Number (with country code): {W}")
        loading_animation("Looking up phone number")
        
        parsed = phonenumbers.parse(phone)
        
        print(f"\n{C}╔═══════════════════════════════════════╗")
        print(f"║{Y}        PHONE INFORMATION               {C}║")
        print(f"╠═══════════════════════════════════════╣")
        print(f"║{G} Valid       : {W}{phonenumbers.is_valid_number(parsed):<21}{C}║")
        print(f"║{G} Country     : {W}{geocoder.description_for_number(parsed, 'en'):<21}{C}║")
        print(f"║{G} Carrier     : {W}{carrier.name_for_number(parsed, 'en'):<21}{C}║")
        print(f"║{G} Timezone    : {W}{str(timezone.time_zones_for_number(parsed))[:21]:<21}{C}║")
        print(f"╚═══════════════════════════════════════╝{RESET}")
        
    except ImportError:
        print(f"{R}[!] Installing phonenumbers module...{RESET}")
        os.system('pip install phonenumbers')
        print(f"{G}[✓] Please run the tool again!{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def whois_lookup():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         🔍 WHOIS LOOKUP 🔍             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    domain = input(f"{G}[+] Enter Domain Name: {W}")
    loading_animation("Fetching WHOIS data")
    
    try:
        import whois
        w = whois.whois(domain)
        
        print(f"\n{C}╔═══════════════════════════════════════╗")
        print(f"║{Y}         WHOIS INFORMATION              {C}║")
        print(f"╠═══════════════════════════════════════╣{RESET}")
        print(f"{G}Domain Name    : {W}{w.domain_name}")
        print(f"{G}Registrar      : {W}{w.registrar}")
        print(f"{G}Creation Date  : {W}{w.creation_date}")
        print(f"{G}Expiration Date: {W}{w.expiration_date}")
        print(f"{G}Name Servers   : {W}{w.name_servers}")
        print(f"{G}Emails         : {W}{w.emails}")
        print(f"{C}╚═══════════════════════════════════════╝{RESET}")
        
    except ImportError:
        os.system('pip install python-whois')
        print(f"{G}[✓] Module installed! Please run again.{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def website_info():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}      🌐 WEBSITE INFORMATION 🌐         {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    url = input(f"{G}[+] Enter Website URL: {W}")
    if not url.startswith('http'):
        url = 'https://' + url
    
    loading_animation("Gathering website information")
    
    try:
        response = requests.get(url, timeout=10)
        ip = socket.gethostbyname(url.replace('https://', '').replace('http://', '').split('/')[0])
        
        print(f"\n{C}╔═══════════════════════════════════════╗")
        print(f"║{Y}       WEBSITE INFORMATION              {C}║")
        print(f"╠═══════════════════════════════════════╣{RESET}")
        print(f"{G}URL           : {W}{url}")
        print(f"{G}IP Address    : {W}{ip}")
        print(f"{G}Status Code   : {W}{response.status_code}")
        print(f"{G}Server        : {W}{response.headers.get('Server', 'N/A')}")
        print(f"{G}Content-Type  : {W}{response.headers.get('Content-Type', 'N/A')}")
        print(f"{G}Response Time : {W}{response.elapsed.total_seconds()}s")
        print(f"{C}╚═══════════════════════════════════════╝{RESET}")
        
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

# ═══════════════════════════════════════════════════════════
#                      NETWORK TOOLS
# ═══════════════════════════════════════════════════════════

def port_scanner():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         🔓 PORT SCANNER 🔓             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    target = input(f"{G}[+] Enter Target IP/Domain: {W}")
    start_port = int(input(f"{G}[+] Enter Start Port: {W}"))
    end_port = int(input(f"{G}[+] Enter End Port: {W}"))
    
    print(f"\n{Y}[*] Scanning ports {start_port} to {end_port}...{RESET}\n")
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"{G}[✓] Port {port} is OPEN{RESET}")
            sock.close()
        except:
            pass
    
    print(f"\n{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}           SCAN RESULTS                 {C}║")
    print(f"╠═══════════════════════════════════════╣")
    print(f"║{G} Target      : {W}{target:<21}{C}║")
    print(f"║{G} Open Ports  : {W}{len(open_ports):<21}{C}║")
    print(f"║{G} Ports       : {W}{str(open_ports)[:21]:<21}{C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def ping_host():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}           📡 PING HOST 📡              {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    host = input(f"{G}[+] Enter Host/IP: {W}")
    count = input(f"{G}[+] Number of pings (default 4): {W}") or "4"
    
    print(f"\n{Y}[*] Pinging {host}...{RESET}\n")
    
    if platform.system().lower() == 'windows':
        os.system(f'ping -n {count} {host}')
    else:
        os.system(f'ping -c {count} {host}')
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def dns_lookup():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}          🔎 DNS LOOKUP 🔎              {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    domain = input(f"{G}[+] Enter Domain: {W}")
    loading_animation("Resolving DNS")
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n{C}╔═══════════════════════════════════════╗")
        print(f"║{Y}          DNS RESULTS                   {C}║")
        print(f"╠═══════════════════════════════════════╣")
        print(f"║{G} Domain      : {W}{domain:<21}{C}║")
        print(f"║{G} IP Address  : {W}{ip:<21}{C}║")
        print(f"╚═══════════════════════════════════════╝{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def my_ip():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}           🌍 MY IP INFO 🌍             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    loading_animation("Fetching your IP information")
    
    try:
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        
        print(f"\n{C}╔═══════════════════════════════════════╗")
        print(f"║{Y}        YOUR IP INFORMATION             {C}║")
        print(f"╠═══════════════════════════════════════╣")
        print(f"║{G} IP Address  : {W}{data.get('query', 'N/A'):<21}{C}║")
        print(f"║{G} Country     : {W}{data.get('country', 'N/A'):<21}{C}║")
        print(f"║{G} Region      : {W}{data.get('regionName', 'N/A'):<21}{C}║")
        print(f"║{G} City        : {W}{data.get('city', 'N/A'):<21}{C}║")
        print(f"║{G} ISP         : {W}{data.get('isp', 'N/A')[:21]:<21}{C}║")
        print(f"║{G} Timezone    : {W}{data.get('timezone', 'N/A'):<21}{C}║")
        print(f"╚═══════════════════════════════════════╝{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

# ═══════════════════════════════════════════════════════════
#                     SECURITY TOOLS
# ═══════════════════════════════════════════════════════════

def password_generator():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}      🔐 PASSWORD GENERATOR 🔐          {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    import string
    
    length = int(input(f"{G}[+] Password Length: {W}"))
    count = int(input(f"{G}[+] Number of Passwords: {W}"))
    
    include_upper = input(f"{G}[+] Include Uppercase? (y/n): {W}").lower() == 'y'
    include_numbers = input(f"{G}[+] Include Numbers? (y/n): {W}").lower() == 'y'
    include_symbols = input(f"{G}[+] Include Symbols? (y/n): {W}").lower() == 'y'
    
    chars = string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    
    print(f"\n{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        GENERATED PASSWORDS             {C}║")
    print(f"╠═══════════════════════════════════════╣{RESET}")
    
    for i in range(count):
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"{G}[{i+1}] {W}{password}")
    
    print(f"{C}╚═══════════════════════════════════════╝{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def hash_generator():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        🔒 HASH GENERATOR 🔒            {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    text = input(f"{G}[+] Enter Text to Hash: {W}")
    
    print(f"\n{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}           HASH RESULTS                 {C}║")
    print(f"╠═══════════════════════════════════════╣{RESET}")
    print(f"{G}MD5    : {W}{hashlib.md5(text.encode()).hexdigest()}")
    print(f"{G}SHA1   : {W}{hashlib.sha1(text.encode()).hexdigest()}")
    print(f"{G}SHA256 : {W}{hashlib.sha256(text.encode()).hexdigest()}")
    print(f"{G}SHA512 : {W}{hashlib.sha512(text.encode()).hexdigest()}")
    print(f"{C}╚═══════════════════════════════════════╝{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def hash_cracker():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         🔓 HASH CRACKER 🔓             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    hash_input = input(f"{G}[+] Enter Hash: {W}")
    wordlist = input(f"{G}[+] Enter Wordlist Path (or press Enter for default): {W}")
    
    if not wordlist:
        wordlist = "/data/data/com.termux/files/usr/share/wordlists/rockyou.txt"
    
    # Detect hash type
    hash_len = len(hash_input)
    if hash_len == 32:
        hash_type = "MD5"
        hash_func = hashlib.md5
    elif hash_len == 40:
        hash_type = "SHA1"
        hash_func = hashlib.sha1
    elif hash_len == 64:
        hash_type = "SHA256"
        hash_func = hashlib.sha256
    else:
        print(f"{R}[✗] Unknown hash type!{RESET}")
        input(f"\n{Y}[Press Enter to continue...]{RESET}")
        return
    
    print(f"\n{Y}[*] Detected hash type: {hash_type}")
    print(f"[*] Starting crack...{RESET}\n")
    
    try:
        with open(wordlist, 'r', errors='ignore') as f:
            for line in f:
                word = line.strip()
                if hash_func(word.encode()).hexdigest() == hash_input.lower():
                    print(f"\n{G}[✓] PASSWORD FOUND: {W}{word}{RESET}")
                    input(f"\n{Y}[Press Enter to continue...]{RESET}")
                    return
        print(f"{R}[✗] Password not found in wordlist!{RESET}")
    except FileNotFoundError:
        print(f"{R}[✗] Wordlist not found!{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def base64_encoder_decoder():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}      📝 BASE64 ENCODER/DECODER 📝      {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{G}[1] Encode")
    print(f"[2] Decode{RESET}\n")
    
    choice = input(f"{Y}[?] Select Option: {W}")
    text = input(f"{G}[+] Enter Text: {W}")
    
    if choice == '1':
        result = base64.b64encode(text.encode()).decode()
        print(f"\n{G}[✓] Encoded: {W}{result}{RESET}")
    elif choice == '2':
        try:
            result = base64.b64decode(text.encode()).decode()
            print(f"\n{G}[✓] Decoded: {W}{result}{RESET}")
        except:
            print(f"{R}[✗] Invalid Base64 string!{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

# ═══════════════════════════════════════════════════════════
#                   SOCIAL MEDIA TOOLS
# ═══════════════════════════════════════════════════════════

def instagram_info():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}       📸 INSTAGRAM INFO 📸             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    username = input(f"{G}[+] Enter Instagram Username: {W}")
    loading_animation("Fetching Instagram info")
    
    try:
        url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(f"\n{G}[✓] Account exists: @{username}")
            print(f"[*] Profile URL: https://www.instagram.com/{username}/{RESET}")
        else:
            print(f"{R}[✗] Account not found or private!{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def github_info():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         🐙 GITHUB INFO 🐙              {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    username = input(f"{G}[+] Enter GitHub Username: {W}")
    loading_animation("Fetching GitHub info")
    
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        data = response.json()
        
        if 'login' in data:
            print(f"\n{C}╔═══════════════════════════════════════╗")
            print(f"║{Y}         GITHUB INFORMATION             {C}║")
            print(f"╠═══════════════════════════════════════╣{RESET}")
            print(f"{G}Username    : {W}{data.get('login', 'N/A')}")
            print(f"{G}Name        : {W}{data.get('name', 'N/A')}")
            print(f"{G}Bio         : {W}{data.get('bio', 'N/A')}")
            print(f"{G}Location    : {W}{data.get('location', 'N/A')}")
            print(f"{G}Public Repos: {W}{data.get('public_repos', 'N/A')}")
            print(f"{G}Followers   : {W}{data.get('followers', 'N/A')}")
            print(f"{G}Following   : {W}{data.get('following', 'N/A')}")
            print(f"{G}Created At  : {W}{data.get('created_at', 'N/A')}")
            print(f"{G}Profile URL : {W}{data.get('html_url', 'N/A')}")
            print(f"{C}╚═══════════════════════════════════════╝{RESET}")
        else:
            print(f"{R}[✗] User not found!{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

# ═══════════════════════════════════════════════════════════
#                    UTILITY TOOLS
# ═══════════════════════════════════════════════════════════

def system_info():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        💻 SYSTEM INFORMATION 💻        {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    loading_animation("Gathering system information")
    
    print(f"\n{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         SYSTEM INFORMATION             {C}║")
    print(f"╠═══════════════════════════════════════╣{RESET}")
    print(f"{G}Platform    : {W}{platform.system()}")
    print(f"{G}Platform Ver: {W}{platform.version()}")
    print(f"{G}Architecture: {W}{platform.machine()}")
    print(f"{G}Hostname    : {W}{socket.gethostname()}")
    print(f"{G}Processor   : {W}{platform.processor()}")
    print(f"{G}Python Ver  : {W}{platform.python_version()}")
    print(f"{G}Current Time: {W}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{C}╚═══════════════════════════════════════╝{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def termux_setup():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         📦 TERMUX SETUP 📦             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{G}[1] Update & Upgrade Termux")
    print(f"[2] Install Basic Packages")
    print(f"[3] Install Python Packages")
    print(f"[4] Install Hacking Tools")
    print(f"[5] Install All")
    print(f"[0] Back{RESET}\n")
    
    choice = input(f"{Y}[?] Select Option: {W}")
    
    if choice == '1':
        os.system('pkg update -y && pkg upgrade -y')
    elif choice == '2':
        packages = "git python python-pip wget curl nmap hydra"
        os.system(f'pkg install {packages} -y')
    elif choice == '3':
        os.system('pip install requests phonenumbers python-whois colorama')
    elif choice == '4':
        os.system('pkg install nmap hydra sqlmap -y')
    elif choice == '5':
        os.system('pkg update -y && pkg upgrade -y')
        os.system('pkg install git python python-pip wget curl nmap hydra -y')
        os.system('pip install requests phonenumbers python-whois colorama')
    
    print(f"\n{G}[✓] Setup completed!{RESET}")
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def youtube_downloader():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}      📺 YOUTUBE DOWNLOADER 📺          {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    url = input(f"{G}[+] Enter YouTube URL: {W}")
    
    print(f"\n{G}[1] Download Video (MP4)")
    print(f"[2] Download Audio (MP3){RESET}\n")
    
    choice = input(f"{Y}[?] Select Option: {W}")
    
    try:
        if choice == '1':
            os.system(f'yt-dlp -f best {url}')
        elif choice == '2':
            os.system(f'yt-dlp -x --audio-format mp3 {url}')
        print(f"\n{G}[✓] Download completed!{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}")
        print(f"[!] Try: pkg install yt-dlp{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def text_to_speech():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        🔊 TEXT TO SPEECH 🔊            {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    text = input(f"{G}[+] Enter Text: {W}")
    
    try:
        os.system(f'termux-tts-speak "{text}"')
        print(f"{G}[✓] Speaking...{RESET}")
    except:
        print(f"{R}[✗] Install Termux:API app and run: pkg install termux-api{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def qr_generator():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        📱 QR CODE GENERATOR 📱         {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    data = input(f"{G}[+] Enter Data for QR Code: {W}")
    filename = input(f"{G}[+] Enter Filename (without extension): {W}")
    
    try:
        import qrcode
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{filename}.png")
        print(f"\n{G}[✓] QR Code saved as {filename}.png{RESET}")
    except ImportError:
        os.system('pip install qrcode[pil]')
        print(f"{G}[✓] Module installed! Please run again.{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def calculator():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}          🔢 CALCULATOR 🔢              {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{G}[+] Enter mathematical expression")
    print(f"[+] Example: 2+2, 10*5, 100/4, 2**10")
    print(f"[+] Type 'exit' to go back{RESET}\n")
    
    while True:
        expr = input(f"{Y}>>> {W}")
        if expr.lower() == 'exit':
            break
        try:
            result = eval(expr)
            print(f"{G}= {result}{RESET}\n")
        except Exception as e:
            print(f"{R}[✗] Error: {e}{RESET}\n")

def file_encryptor():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        🔐 FILE ENCRYPTOR 🔐            {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{G}[1] Encrypt File")
    print(f"[2] Decrypt File{RESET}\n")
    
    choice = input(f"{Y}[?] Select Option: {W}")
    filepath = input(f"{G}[+] Enter File Path: {W}")
    password = input(f"{G}[+] Enter Password: {W}")
    
    try:
        from cryptography.fernet import Fernet
        key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
        cipher = Fernet(key)
        
        with open(filepath, 'rb') as f:
            data = f.read()
        
        if choice == '1':
            encrypted = cipher.encrypt(data)
            with open(filepath + '.encrypted', 'wb') as f:
                f.write(encrypted)
            print(f"\n{G}[✓] File encrypted: {filepath}.encrypted{RESET}")
        elif choice == '2':
            decrypted = cipher.decrypt(data)
            with open(filepath.replace('.encrypted', ''), 'wb') as f:
                f.write(decrypted)
            print(f"\n{G}[✓] File decrypted!{RESET}")
    except ImportError:
        os.system('pip install cryptography')
        print(f"{G}[✓] Module installed! Please run again.{RESET}")
    except Exception as e:
        print(f"{R}[✗] Error: {e}{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def wifi_scanner():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}         📶 WIFI SCANNER 📶             {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{Y}[*] Scanning for WiFi networks...{RESET}\n")
    
    try:
        os.system('termux-wifi-scaninfo')
    except:
        print(f"{R}[✗] Install Termux:API app and run: pkg install termux-api{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def device_info():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}        📱 DEVICE INFORMATION 📱        {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{Y}[*] Fetching device information...{RESET}\n")
    
    try:
        print(f"{C}=== Battery Info ==={RESET}")
        os.system('termux-battery-status')
        print(f"\n{C}=== Device Info ==={RESET}")
        os.system('termux-telephony-deviceinfo')
    except:
        print(f"{R}[✗] Install Termux:API app and run: pkg install termux-api{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def send_sms():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}          📱 SEND SMS 📱                {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    number = input(f"{G}[+] Enter Phone Number: {W}")
    message = input(f"{G}[+] Enter Message: {W}")
    
    try:
        os.system(f'termux-sms-send -n {number} "{message}"')
        print(f"\n{G}[✓] SMS sent successfully!{RESET}")
    except:
        print(f"{R}[✗] Install Termux:API app and run: pkg install termux-api{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def location_tracker():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}       📍 LOCATION TRACKER 📍           {C}║")
    print(f"╚═══════════════════════════════════════╝{RESET}\n")
    
    print(f"{Y}[*] Getting location...{RESET}\n")
    
    try:
        os.system('termux-location')
    except:
        print(f"{R}[✗] Install Termux:API app and run: pkg install termux-api{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

def about():
    banner()
    print(f"{C}╔═══════════════════════════════════════╗")
    print(f"║{Y}             ABOUT EZ TOOLS             {C}║")
    print(f"╠═══════════════════════════════════════╣")
    print(f"║                                       ║")
    print(f"║{G}  Developer  : ASHEN EDITZ             {C}║")
    print(f"║{G}  Contact    : 0726962974              {C}║")
    print(f"║{G}  Version    : 2.0 PREMIUM             {C}║")
    print(f"║{G}  GitHub     : github.com/ashen-editz  {C}║")
    print(f"║                                       ║")
    print(f"║{W}  EZ TOOLS is a comprehensive toolkit  {C}║")
    print(f"║{W}  for Termux with multiple features    {C}║")
    print(f"║{W}  for information gathering, network   {C}║")
    print(f"║{W}  analysis, security testing, and      {C}║")
    print(f"║{W}  utility functions.                   {C}║")
    print(f"║                                       ║")
    print(f"║{R}  DISCLAIMER: For educational purposes {C}║")
    print(f"║{R}  only. Use responsibly and legally.   {C}║")
    print(f"║                                       ║")
    print(f"╚═══════════════════════════════════════╝{RESET}")
    
    input(f"\n{Y}[Press Enter to continue...]{RESET}")

# ═══════════════════════════════════════════════════════════
#                       MAIN MENU
# ═══════════════════════════════════════════════════════════

def main_menu():
    while True:
        banner()
        print(f"""
{C}╔═══════════════════════════════════════════════════════════════╗
║{Y}                     📋 MAIN MENU 📋                            {C}║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  {G}[01]{W} IP Tracker          {G}[02]{W} Phone Lookup                  ║
║  {G}[03]{W} WHOIS Lookup        {G}[04]{W} Website Info                  ║
║  {G}[05]{W} Port Scanner        {G}[06]{W} Ping Host                     ║
║  {G}[07]{W} DNS Lookup          {G}[08]{W} My IP Info                    ║
║  {G}[09]{W} Password Generator  {G}[10]{W} Hash Generator                ║
║  {G}[11]{W} Hash Cracker        {G}[12]{W} Base64 Encode/Decode          ║
║  {G}[13]{W} Instagram Info      {G}[14]{W} GitHub Info                   ║
║  {G}[15]{W} System Info         {G}[16]{W} Termux Setup                  ║
║  {G}[17]{W} YouTube Downloader  {G}[18]{W} Text to Speech                ║
║  {G}[19]{W} QR Code Generator   {G}[20]{W} Calculator                    ║
║  {G}[21]{W} File Encryptor      {G}[22]{W} WiFi Scanner                  ║
║  {G}[23]{W} Device Info         {G}[24]{W} Send SMS                      ║
║  {G}[25]{W} Location Tracker    {G}[26]{W} About                         ║
║                                                               ║
║  {R}[00]{W} Exit                                                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{RESET}
        """)
        
        choice = input(f"{Y}[?] Select Option: {W}")
        
        options = {
            '01': ip_tracker, '1': ip_tracker,
            '02': phone_lookup, '2': phone_lookup,
            '03': whois_lookup, '3': whois_lookup,
            '04': website_info, '4': website_info,
            '05': port_scanner, '5': port_scanner,
            '06': ping_host, '6': ping_host,
            '07': dns_lookup, '7': dns_lookup,
            '08': my_ip, '8': my_ip,
            '09': password_generator, '9': password_generator,
            '10': hash_generator,
            '11': hash_cracker,
            '12': base64_encoder_decoder,
            '13': instagram_info,
            '14': github_info,
            '15': system_info,
            '16': termux_setup,
            '17': youtube_downloader,
            '18': text_to_speech,
            '19': qr_generator,
            '20': calculator,
            '21': file_encryptor,
            '22': wifi_scanner,
            '23': device_info,
            '24': send_sms,
            '25': location_tracker,
            '26': about,
            '00': exit, '0': exit
        }
        
        if choice in options:
            if choice in ['00', '0']:
                print(f"\n{G}[✓] Thank you for using EZ TOOLS by ASHEN EDITZ!")
                print(f"[*] Contact: 0726962974{RESET}\n")
                sys.exit(0)
            options[choice]()
        else:
            print(f"{R}[✗] Invalid option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Interrupted by user{RESET}")
        print(f"{G}[*] Thank you for using EZ TOOLS by ASHEN EDITZ!{RESET}\n")
        sys.exit(0)
