#!/usr/bin/env python2.7

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
directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
os.system('clear')


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


os.system('clear')
os.system('clear')
yes = set(['yes', 'y', 'ye', 'Y', 'yep'])
no = set(['no', 'n', 'nope', 'nop', 'N'])
def logo():
    print """
"""

############### MENU ###############
def menu():
    print("   {1}--Directory Checker")
    print("   {2}--Scan Users")
    print("   {3}--Port Scan")
    choiceweb = raw_input("root@razvyy~# ")
    if choiceweb == "1":
        clearScr()
        shelltarget()
    if choiceweb == "2":
        clearScr()
        scanusers()
    if choiceweb == "3":
        clearScr()
        nmap()
    elif choiceweb == "":
        menu()
    else:
        menu()

############### DIRECTORIES CHECKER ###############
def grabuploadedlink(url):
    try:
        for dir in directories:
            currentcode = urllib.urlopen(url + dir).getcode()
            if currentcode == 200 or currentcode == 403:
                print "-------------------------"
                print "  [ + ] Found Directory :  " + str(url + dir) + " "
                upload.append(url + dir)
    except:
        pass


def grabshell(url):
    try:
        for upl in upload:
            for shell in shells:
                currentcode = urllib.urlopen(upl + shell).getcode()
                if currentcode == 200:
                    print "-------------------------"
                    print "  [ ! ] Found Shell :  " + str(upl + shell) + ""
    except:
        pass

def shelltarget():
    print("Example: http://target.com")
    line = raw_input("Target: ")
    line = line.rstrip()
    grabuploadedlink(line)
    grabshell(line)

############### SCAN USERA ###############
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
    os.system("apt install nmap > /dev/null & yum install apt > /dev/null & pkg install nmap > /dev/null")
    os.system("nmap " target)

############### CLEARSCR ###############
def clearScr():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

#####################################
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("Closing...\r"),
        time.sleep(1)
