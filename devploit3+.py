#!/usr/bin/env python
############################################
# Devploit . Version 3.x - amped up
# Python version 3.7.3
# Based on Devploit - Information Gathering Tool
############################################
import urllib, datetime, socket
import sys, os, json
import time as t
from urllib.request import urlopen
from os import system, name
from requests import get
#==============================================================================================================
def WhatsMyIp():                                                                # get your IP address
  ip = get('https://api.ipify.org').text
  return(ip)
def clear():                                                                    # define our clear function
    if name == 'nt':
        _ = system('cls')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        t.sleep(4. / 100)
def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        t.sleep(1. / 100)
#==============================================================================================================
ip = WhatsMyIp()
banner = f'''
██████╗ ███████╗██╗   ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗██╔════╝██║   ██║██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║  ██║█████╗  ██║   ██║██████╔╝██║     ██║   ██║██║   ██║   
██║  ██║██╔══╝  ╚██╗ ██╔╝██╔═══╝ ██║     ██║   ██║██║   ██║   
██████╔╝███████╗ ╚████╔╝ ██║     ███████╗╚██████╔╝██║   ██║   
╚═════╝ ╚══════╝  ╚═══╝  ╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝ Real-4w version.
            Name   : Devploit for Python 3.7 running @ {ip}    
            Version: Real-4w                     
'''
print (banner)
def menu():
   print (f'''
-------------------------------------------------------
[x] Main Menu for {ip}
-------------------------------------------------------
0 - My IP               10 - IP-Locator 
1 - DNS Lookup*         11 - Traceroute*
2 - Whois Lookup*       12 - Host DNS Finder
3 - GeoIP Lookup*       13 - Reverse DNS Lookup*
4 - Subnet Lookup*      14 - Collection Email
5 - TCP Port Scanner*   15 - Install & Update
6 - Extract Links*      16 - Test Ping* 
7 - Zone Transfer*      17 - DNS (A) Record*
8 - HTTP Header*        18 - DNS Shared Servers*
9 - AS Lookup*          19 - Reverse IP Lookup*
99 - About me
100 - Exit
------------------------------------------------------
''')

slowprint("This is scripted for python version 3.7")
menu()

def ext():
  ex = input ('Continue/Exit :')
  if ex:
    if ex[0].upper() == 'E' :
      print ('[X]Exiting. Good-bye')
      exit()
    else :
      clear()
      print (banner)
      menu()
      select()
  else:
    clear()
    print (banner)
    menu()
    select()

def  select():
  try:
    joker = input("[x] Enter your option :")
    if joker == '0' :
      print(f"Your public IP address is {ip}")
      hostname = socket.gethostname()    
      IPAddr = socket.gethostbyname(hostname)    
      print(f"Your Computer Name is: {hostname}")    
      print(f"Your local IP address is: {IPAddr}")  
      ext()
    elif joker == '1':
      dz = input('[x] Enter Domain name :')
      whois = "https://api.hackertarget.com/dnslookup/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '2':
      dz = input('[x] Enter Domain name :')
      whois = "https://api.hackertarget.com/whois/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '3':
      dz = input('[x] Enter IP address :')
      whois = "https://api.hackertarget.com/geoip/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '4':
      dz = input('[x] Enter IP/ subnet mask :')
      whois = "https://api.hackertarget.com/subnetcalc/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '5':
      dz = input('[x] Enter IP address:')
      whois = "https://api.hackertarget.com/nmap/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '6':
      dz = input('[x] Enter website :')
      whois = "https://api.hackertarget.com/pagelinks/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '7':
      dz = input('[x] Enter Domain name :')
      whois = "https://api.hackertarget.com/zonetransfer/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '8':
      dz = input('[x] Enter complete URL :')
      whois = "https://api.hackertarget.com/httpheaders/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '9':
      dz = input('[x] Enter Domain name :')
      whois = "https://api.hackertarget.com/aslookup/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '10':
      print ("[x] Option is out of service\n")
      ext()
    elif joker == '11':
      dz = input('[x] Enter IP Address :')
      whois = "https://api.hackertarget.com/mtr/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '12':
      print ("[x] Option is out of service\n")
      ext()
    elif joker == '13':
      dz = input('[x] Enter IP address :')
      whois = "https://api.hackertarget.com/reversedns/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '14':
      print ("[x] Option is out of service\n")
      ext()
    elif joker == '15':
      print ("[x] Option is out of service\n")
      ext()
    elif joker == '16':
      dz = input('[x] Enter IP Address :')
      whois = "https://api.hackertarget.com/nping/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '17':
      dz = input('[x] Enter Domain name :')
      whois = "https://api.hackertarget.com/hostsearch/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '18':
      dz = input('[x] Enter name server :')
      whois = "https://api.hackertarget.com/findshareddns/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '19':
      dz = input('[x] Enter name server :')
      whois = "https://api.hackertarget.com/reverseiplookup/?q=" + dz
      dev = urlopen(whois).read()
      print ("[x] API Response :\n")
      print (dev.decode("utf-8"))
      ext()
    elif joker == '99':
      fastprint("------------------------------------------------------")
      fastprint("Name    : Devploit V3+")
      fastprint("------------------------------------------------------")
      fastprint("Version : 3.x")
      fastprint("------------------------------------------------------")
      fastprint("Author  : Real-4w")
      fastprint("------------------------------------------------------")
      ext() 
    elif joker == '100':
      print ("Good-bye!!")
    elif joker == "exit":
      print ("Good-bye!!")
    else:
      print ("Not in the menu. Please try again.")
      asd = input()
      select()
  except(KeyboardInterrupt):
    print ("\n[x] Intterupt -- Ctrl + C -- Exiting!!")
select()
