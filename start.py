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
directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php', 'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php', 'shells.php', '1337.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y', 'yep'])
no = set(['no', 'n', 'nope', 'nop', 'N'])


def logo():
    print """
"""

############### MENU ###############
def menu():
    print("   {1}--Shell Checker")
    print("   {2}--Control Panel Finder")
    print("   {2}--Zip Files Finder")
    print("   {3}--Get server Info")
    choiceweb = raw_input("root@razvyy~# ")
    if choiceweb == "1":
        clearScr()
        shelltarget()
    if choiceweb == "2":
        clearScr()
        paneltarget()
    if choiceweb == "3":
        clearScr()
        zipiptarget()
    if choiceweb == "4":
        clearScr()
        getserverbannertarget()
    elif choiceweb == "":
        menu()
    else:
        menu()

############### SHELL CHECKER ###############
def grabuploadedlink(url):
    try:
        for dir in directories:
            currentcode = urllib.urlopen(url + dir).getcode()
            if currentcode == 200 or currentcode == 403:
                print "-------------------------"
                print "  [ + ] Found Directory :  " + str(url + dir) + " [ + ]"
                print "-------------------------"
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
                    print "  [ ! ] Found Shell :  " + str(upl + shell) + " [ ! ]"
                    print "-------------------------"
    except:
        pass

def shelltarget():
    print("Example: http://target.com")
    line = raw_input("Target: ")
    line = line.rstrip()
    grabuploadedlink(line)
    grabshell(line)

############### PANEL CHECKER ###############

def paneltarget():
    print("Example: http://target.com")
    line = raw_input("Target: ")
    line = line.rstrip()
    findPanels(line)

    def findPanels(line):
        """
        find panels from grabbed websites
        the attacker may do a lot of vulnerabilty
        tests on the admin area
        """
        print "[~] Finding admin panels"
        adminList = ['admin/', 'site/admin', 'admin.php/', 'up/admin/', 'central/admin/', 'whm/admin/', 'whmcs/admin/', 'support/admin/', 'upload/admin/', 'video/admin/', 'shop/admin/', 'shoping/admin/', 'wp-admin/', 'wp/wp-admin/', 'blog/wp-admin/', 'admincp/', 'admincp.php/', 'vb/admincp/', 'forum/admincp/', 'up/admincp/', 'administrator/',
                     'administrator.php/', 'joomla/administrator/', 'jm/administrator/', 'site/administrator/', 'install/', 'vb/install/', 'dimcp/', 'clientes/', 'admin_cp/', 'login/', 'login.php', 'site/login', 'site/login.php', 'up/login/', 'up/login.php', 'cp.php', 'up/cp', 'cp', 'master', 'adm', 'member', 'control', 'webmaster', 'myadmin', 'admin_cp', 'admin_site']
        clearScr()
        for site in line:
            for admin in adminList:
                try:
                    if urllib.urlopen(site + admin).getcode() == 200:
                        print " [*] Found admin panel -> ", site + admin
                except IOError:
                    pass

############## GETSERVERBANNER ###############
def getserverbannertarget():
    print("Example: http://target.com")
    line = raw_input("Target: ")
    line = line.rstrip()
    getServerBanner(line)

    def getServerBanner(line):
        """
        simply gets the server banner
        the attacker may benefit from it
        like getting the server side software
        """
        clearScr()
        try:
            s = 'http://' + line.serverip
            httpresponse = urllib.urlopen(s)
            print ' [*] Server header -> ', httpresponse.headers.getheader('server')
        except:
            pass

############### ZIP CHECKER ###############
def ziptarget():
    print("Example: http://target.com")
    line = raw_input("Target: ")
    line = line.rstrip()
    findZip(line)

    def findZip(line):
        """
        find zip files from grabbed websites
        it may contain useful informations
        """
        zipList = ['backup.tar.gz', 'backup/backup.tar.gz', 'backup/backup.zip', 'vb/backup.zip', 'site/backup.zip', 'backup.zip', 'backup.rar', 'backup.sql', 'vb/vb.zip', 'vb.zip', 'vb.sql', 'vb.rar',
                   'vb1.zip', 'vb2.zip', 'vbb.zip', 'vb3.zip', 'upload.zip', 'up/upload.zip', 'joomla.zip', 'joomla.rar', 'joomla.sql', 'wordpress.zip', 'wp/wordpress.zip', 'blog/wordpress.zip', 'wordpress.rar']
        clearScr()
        print "[~] Finding zip file"
        for site in line:
            for zip1 in zipList:
                try:
                    if urllib.urlopen(site + zip1).getcode() == 200:
                        print " [*] Found zip file -> ", site + zip1
                except IOError:
                    pass

        """
        find zip files from grabbed websites
        it may contain useful informations
        """
        zipList = ['backup.tar.gz', 'backup/backup.tar.gz', 'backup/backup.zip', 'vb/backup.zip', 'site/backup.zip', 'backup.zip', 'backup.rar', 'backup.sql', 'vb/vb.zip', 'vb.zip', 'vb.sql', 'vb.rar',
                   'vb1.zip', 'vb2.zip', 'vbb.zip', 'vb3.zip', 'upload.zip', 'up/upload.zip', 'joomla.zip', 'joomla.rar', 'joomla.sql', 'wordpress.zip', 'wp/wordpress.zip', 'blog/wordpress.zip', 'wordpress.rar']
        clearScr()
        print "[~] Finding zip file"
        for site in self.sites:
            for zip1 in zipList:
                try:
                    if urllib.urlopen(site + zip1).getcode() == 200:
                        print " [*] Found zip file -> ", site + zip1
                except IOError:
                    pass

############### CLEARSCR ###############
def clearScr():
    """
    Clear the screen in case of GNU/Linux or
    windows
    """
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
        time.sleep(0.25)
