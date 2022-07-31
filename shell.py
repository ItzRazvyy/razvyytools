#!/usr/bin/python3

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time
global starttime

class shellScanner():

    def __init__(self):
        self.scan()
        
    def scan(self):
        parser = argparse.ArgumentParser(prog="shell.py", description="Simple Find Shell in Website")
        parser.add_argument("-u", dest="domain", help="Your url")
        parser.add_argument("-w", dest="wordlist", help="Your wordlist")
        args = parser.parse_args()
        if not args.domain:
            sys.exit(f"Usage: shell.py -u example.com -w wordlist.txt")
        if not args.wordlist:
            sys.exit(f"Usage: shell.py -u example.com -w wordlist.txt")
            
        # handle url website format
        site = args.domain
        print("Start Crawling...")
        time.sleep(2)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("Upss, Wordlist Not Found!")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("Wordlist Can\'t Close!")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #list to hold the results we find
        found = []
        # respon code
        resp_codes = {403 : "403 forbidden", 401 : "401 unauthorized"}
        # loop with join pathlist
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("[{0}]".format(time.strftime("%H:%M:%S")),"Found:",""+psx)
                    found.append(url)
                    
                except HTTPError as e:
                    if e.code == 404:
                        print("[{0}]".format(time.strftime("%H:%M:%S")),"Error:",""+psx)
                    else:
                        print("[{0}]".format(time.strftime("%H:%M:%S")),"Info :",""+psx,"Status: ",resp_codes[e.code])
                        
                except URLError as e:
                    sys.exit("[!] No Internet Connection!")
                except Exception as er:
                    print("[?] Your Internet Connection is unstable!")
                    print("[!] Exiting...")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("[?] CTRL+C Detected")
                print("[!] Exiting...")
                time.sleep(2)
                exit()
        if found:
            print("[+] Results Found:")
            print("\n".join(found))
            print("[?] Time Elasped: %.2f Seconds" % float(time.time()-starttime))
        else:
            print("[!] Could not find any shell backdoor")
            print("[?] Time Elasped: %.2f Seconds" % float(time.time()-starttime))
                
    def banner():
        info = """"""
        return info
    print(banner())
                
if __name__ == '__main__':
    shellScanner()