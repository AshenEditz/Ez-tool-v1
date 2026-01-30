#!/bin/bash

# EZ TOOLS Installer by ASHEN EDITZ
# Contact: 0726962974

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║  ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗║"
echo "║  ██╔════╝╚══███╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝║"
echo "║  █████╗    ███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗║"
echo "║  ██╔══╝   ███╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║║"
echo "║  ███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║║"
echo "║  ╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝║"
echo "║                                                               ║"
echo "║                 INSTALLER BY ASHEN EDITZ                      ║"
echo "║                    Contact: 0726962974                        ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

sleep 2

echo -e "${YELLOW}[*] Starting EZ TOOLS Installation...${NC}"
sleep 1

# Update packages
echo -e "${GREEN}[+] Updating package lists...${NC}"
pkg update -y > /dev/null 2>&1
echo -e "${GREEN}[✓] Package lists updated!${NC}"

# Upgrade packages
echo -e "${GREEN}[+] Upgrading packages...${NC}"
pkg upgrade -y > /dev/null 2>&1
echo -e "${GREEN}[✓] Packages upgraded!${NC}"

# Install required packages
echo -e "${GREEN}[+] Installing required packages...${NC}"
pkg install python -y > /dev/null 2>&1
pkg install python-pip -y > /dev/null 2>&1
pkg install git -y > /dev/null 2>&1
pkg install wget -y > /dev/null 2>&1
pkg install curl -y > /dev/null 2>&1
pkg install nmap -y > /dev/null 2>&1
pkg install termux-api -y > /dev/null 2>&1
echo -e "${GREEN}[✓] Packages installed!${NC}"

# Install Python modules
echo -e "${GREEN}[+] Installing Python modules...${NC}"
pip install requests > /dev/null 2>&1
pip install phonenumbers > /dev/null 2>&1
pip install python-whois > /dev/null 2>&1
pip install colorama > /dev/null 2>&1
pip install qrcode > /dev/null 2>&1
pip install pillow > /dev/null 2>&1
pip install cryptography > /dev/null 2>&1
echo -e "${GREEN}[✓] Python modules installed!${NC}"

# Make script executable
echo -e "${GREEN}[+] Setting up permissions...${NC}"
chmod +x ez-tools.py
echo -e "${GREEN}[✓] Permissions set!${NC}"

# Create shortcut command
echo -e "${GREEN}[+] Creating shortcut command...${NC}"
cp ez-tools.py $PREFIX/bin/ez-tools
chmod +x $PREFIX/bin/ez-tools
echo -e "${GREEN}[✓] Shortcut created!${NC}"

echo ""
echo -e "${CYAN}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║${GREEN}           EZ TOOLS INSTALLED SUCCESSFULLY!                   ${CYAN}║${NC}"
echo -e "${CYAN}╠═══════════════════════════════════════════════════════════════╣${NC}"
echo -e "${CYAN}║                                                               ║${NC}"
echo -e "${CYAN}║${YELLOW}  Run the tool using:                                         ${CYAN}║${NC}"
echo -e "${CYAN}║${WHITE}    • python ez-tools.py                                       ${CYAN}║${NC}"
echo -e "${CYAN}║${WHITE}    • ez-tools                                                 ${CYAN}║${NC}"
echo -e "${CYAN}║                                                               ║${NC}"
echo -e "${CYAN}║${GREEN}  Developer: ASHEN EDITZ                                       ${CYAN}║${NC}"
echo -e "${CYAN}║${GREEN}  Contact: 0726962974                                          ${CYAN}║${NC}"
echo -e "${CYAN}║                                                               ║${NC}"
echo -e "${CYAN}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""
