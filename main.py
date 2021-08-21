#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import argparse
import os
import time
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
#import requests
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
##########################

############### CLEARSCR ###############
def clearScr():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
     
clearScr()     

def menu():
    print ("""
MIT License

Copyright (c) 2021

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")

yes = set(['yes', 'y', 'ye', 'Y', 'yep', 'Yes', 'YES'])
no = set(['no', 'n', 'nope', 'nop', 'N', 'NO', 'No'])
color = {"blue": "\033[94m", "red": "\033[91m", "green": "\033[92m", "white": "\033[0m", "yellow": "\033[93m"}
 
############### MENU ###############
def menu():
    print ""
    print "\t\t------------------" + color['blue'] + "RazvyyTools" + color['white'] + "----------------"
    print "\t\tx             Developed by: Razvyy          x"
    print "\t\tx  https://github.com/ItzRazvyy/razvyytools x"
    print "\t\t---------------------------------------------"
    print ""
    print("   {1}--Shell Scanner")
    print("   {2}--Scan Users")
    print("   {3}--Port Scan")
    print("   {0}--Update")
    choiceweb = raw_input("root@localhost~# ")
    if choiceweb == "1":
        clearScr()
        shelltarget()
    if choiceweb == "2":
        clearScr()
        scanusers()
    if choiceweb == "3":
        clearScr()
        nmap()
    elif choice == "0":
        clearScr()
        update()
    elif choiceweb == "":
        menu()
        clearScr()
    else:
        clearScr()
        menu()

############### DIRECTORIES CHECKER ###############
def shelltarget():
    os.system("python tools/shell_scanner.py /dev/null 2>&1")
    os.system("python2 tools/shell_scanner.py /dev/null 2>&1")
    os.system('clear')
    os.system('cls')
        
############### UPDATE ###############
def update():
    print ("This Tool is Only Available for Linux and Similar Systems.")
    choiceupdate = raw_input("Continue? Y/N: ")
    if choiceupdate in yes:
        os.system("git clone https://github.com/ItzRazvyy/razvyytools.git")
        os.system("cd razvyytools && sudo bash ./update.sh")

############### TIMER ###############
    def timer():
        now = time.localtime(time.time())
        return time.asctime(now)
        
############### SCAN USERS ###############
def scanusers():
    site = raw_input('Enter a website: ')
    try:
        users = site
        if 'http://www.' in users:
            users = users.replace('http://www.', '')
        if 'http://' in users:
            users = users.replace('http://', '')
        if '.' in users:
            users = users.replace('.', '')
        if '-' in users:
            users = users.replace('-', '')
        if '/' in users:
            users = users.replace('/', '')
        while len(users) > 2:
            print users
            resp = urllib2.urlopen(
                site + '/cgi-sys/guestbook.cgi?user=%s' % users).read()

            if 'invalid username' not in resp.lower():
                print "\tFound -> %s" % users
                pass

            users = users[:-1]
    except:
        pass
        
def nmap():
    target = raw_input("Enter a target: ")
    os.system("apt install nmap -y > /dev/null 2>&1 & yum install nmap -y > /dev/null 2>&l")
    os.system("nmap %s" % target)
    choicebacktomenu = raw_input("Back to menu? Y/N: ")
    if choicebacktomenu in yes:
        menu()
    if choicebacktomenu in no:
            exit()

#####################################
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("Closing...\r"),
        time.sleep(1)