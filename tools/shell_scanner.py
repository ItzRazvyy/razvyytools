#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
################
import os      #
import sys     #
import urllib2 #
import re      #
################

if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass

#Colors
color = {"blue": "\033[94m", "red": "\033[91m", "green": "\033[92m", "white": "\033[0m", "yellow": "\033[93m"}

def gscan(): #Global scan
        global url
        global coneccion_url 
        rela =[] #relationship
        avai =[] #available
        redi =[] #redirect

        with open('tools/wordlist.txt','r') as f:
                lines = f.readlines()
                for line in lines:
                        try:
                                coneccion_url = url + line
                                r = urllib2.Request(coneccion_url)
                                r.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6')#UserAgent
                                r.add_unredirected_header('Referer', 'http://www.google.com/')
                                req = urllib2.urlopen(r)
                                resp = req.read()
                                if req.getcode()==200:
                                        print '\n\033[1;32mFOUND: \033[1;m' + coneccion_url, #Found
                                        rela.append(coneccion_url+str(len(resp)))
                                else:
                                        print '\n\033[1;32mREDIRECTION: \033[1;m' + coneccion_url, #Redirection
                                        redi.append(coneccion_url) 
                        except urllib2.HTTPError as e:
                                if e.code == 401:
                                        print '\n\033[1;32mSUSPICION: \033[1;m' + coneccion_url, #Possible suspicion
                                        avai.append(coneccion_url)
                                elif e.code == 404:
                                        print color['red'] + '-\033[1;m' + color['white'],
                                elif e.code == 503:
                                        print '\033[1;31mx\033[1;m' + coneccion_url, #Not Found
                                else:
                                        print '\n\033[1;32mREDIRECTION: \033[1;m' + coneccion_url, #Redirection
                                        redi.append(coneccion_url)                                   
                print '\n'
                print  color['blue'] + "[!]" + " " + color['green'] + "Result" + color['white']
                if rela:
                        print color['blue'] + "[>]" + " " + color['yellow'] + "Possible malicious files\n" + color['white']
                        for relas in rela:
                                print color['red'] + "\t" + color['white'] + relas,
                        print color['blue'] + '\n================================================================' + color['white']
                if avai:
                        print color['blue'] + "[+]" + " " + color['yellow'] + "Possible detected Shell\n" + color['white']
                        for avais in avai:
                                print avais,
                        print color['blue'] + '\n==================================================================' + color['white']
                if redi:
                        print "Statements of other income"
                        for redis in redi:
                                print redis,
                        print color['blue'] + '\n===================================================================' + color['white']
def validate():
        global url
        url = raw_input("Enter a website: ")
        print color['green'] + "Loaded 3458 wordlist\n" + color['white'],
        print color['blue'] + "Start Scanning...\n" + color['white']
        if url.endswith("/"):  
                pass 
        else:
                url = url + "/"
        if re.match('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)',url): #regexp
                pass
        else:
                validate()
            
def clearScr():
        os.system('clear')
        os.system('cls')

if __name__ == "__main__":
        try:
            validate()
            gscan()
            validate()
        except KeyboardInterrupt:
          pass
        except Exception as e:
                print color['red'] + "Error: " + color['white'] + "%s" % e 