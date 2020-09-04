#!/bin/bash

CL='\033[1;32m'
NC='\033[0m'
echo -e "\n${CL}====================="
echo -e "[1]-${NC} Debian/Ubuntu"
echo -e "${CL}[2]-${NC} Arch Linux"
echo -e "${CL}[3]-${NC} Fedora"
echo -e "${CL}[4]-${NC} openSUSE\n"

read -p "// Select your OS: " osname
echo -e "${CL}=====================${NC}"

if [ $osname == 1 ]
then
    sudo apt install python3-pip -y
elif [ $osname == 2 ]
then
    sudo pacman -S python-pip -y
elif [ $osname == 3 ]
then
    sudo dnf install python3 -y
elif [ $osname == 4 ]
then
    sudo zypper install python3-pip -y
else
    echo "// Select a valid option!"
    exit
fi
pip3 install selenium &&
pip3 install explicit &&
python3 handleWdFile.py &&

echo -e "\n${CL}====================="
echo -e "${NC}        Done!"
echo -e "${CL}=====================${NC}"
