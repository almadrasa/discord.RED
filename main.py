#<---FILE_START--->


#<---imports start--->
import os
import sys

def install(package):
  print("Installing required package...")
  os.system(f"{sys.executable} -m pip install {package}")

try:
  import discum
except ModuleNotFoundError:
  print("Installing required package...")
  os.system(f"{sys.executable} -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
try:
  import asyncio
except ModuleNotFoundError:
  install("asyncio")
try:
  import colorama
  from colorama import Fore, Back, Style
  from colorama import init
except ModuleNotFoundError:
  install("colorama")
try:
  import time
except ModuleNotFoundError:
  install("time")
try:
  from base64 import b64encode as b64
  from base64 import b64decode
  import base64
except ModuleNotFoundError:
  install("base64")
try:
  import pyfiglet
except ModuleNotFoundError:
  install("pyfiglet")
try:
  from pyxtension.Json import Json
except ModuleNotFoundError:
  install("pyxtension")
try:
  from random import choice as ch
except ModuleNotFoundError:
  install("random")
try:
  from datetime import datetime
except ModuleNotFoundError:
  install("datetime")
try:
  import time
except ModuleNotFoundError:
  install("time")
try:
  import webbrowser
except ModuleNotFoundError:
  install("webbrowser")
try:
  import selenium
except:
  install("selenium")
try:
  import discord
except:
  install("discord.py-self")
  

import requests
from token_bruteforce import bruteforce_token
from token_login import tokenlogin
from userid_info import lookup
from hook_spammer import spam_webhook
from red_rpc import custom_rpc
from selfbot_red import red_start
from token_locker import ban_token

#<---imports end--->

#<---graphics setup--->
def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
clear()
init() # start colorama
print(Fore.RED) # set color red
print(Back.BLACK)
print(colorama.ansi.clear_screen())
print(Style.BRIGHT)
clear()
if os.name == 'nt':
  os.system("title dsc.RED")
else:
  pass # the system is running linux.

#<---end of graphics setup--->

#<--display pretty stuff start--->
def welcome():
  clear()
  print(Fore.RED + ".%%%%%....%%%%....%%%%...........%%%%%...%%%%%%..%%%%%..".center(os.get_terminal_size().columns))
  print(Fore.RED + ".%%..%%..%%......%%..%%..........%%..%%..%%......%%..%%.".center(os.get_terminal_size().columns))
  print(Fore.RED + ".%%..%%...%%%%...%%..............%%%%%...%%%%....%%..%%.".center(os.get_terminal_size().columns))
  print(Fore.RED + ".%%..%%......%%..%%..%%..........%%..%%..%%......%%..%%.".center(os.get_terminal_size().columns))
  print(Fore.RED + ".%%%%%....%%%%....%%%%.....%%....%%..%%..%%%%%%..%%%%%..".center(os.get_terminal_size().columns))
  print(Fore.RED + " ........................................................\n".center(os.get_terminal_size().columns))
  print(Fore.WHITE + "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n".center(os.get_terminal_size().columns))
  col_size = os.get_terminal_size().columns
  inp = "the discord cracking suite."
  print(Fore.RED + inp.center(col_size))
  print("\n\n\n")
welcome()
#<---display pretty stuff end--->

#<---options start--->
try:
  os.startfile("COMMANDS.txt") # tries open the commands file in its default program
except:
  FILE = open("COMMANDS.txt", "r")
  CMDSS = FILE.read()
  FILE.close()
  print(f"{Fore.MAGENTA}Uh Oh! You're on Linux, so you have to manually launch the commands. Go into this program's directory, and open \"COMMANDS.txt\" to view the usable commands!".center(os.get_terminal_size().columns)) # system is running linux, so we just tell them to manually open it.
#<---options end--->


#<---main code start--->
print("\n\n\n")
col_size = os.get_terminal_size().columns
num = round(col_size/4)
a = ">>  "
a2 = "".join([' ' for x in range(0, num)])
print(Fore.BLUE + a2 + a, end='')
inp = int(input())

if inp == 0:
  clear()
  exit(0)
if inp == 1:
  bruteforce_token()
if inp == 2:
  tokenlogin()
if inp == 3:
  lookup()
if inp == 4:
  spam_webhook()
if inp == 5:
  custom_rpc()
if inp == 6:
  red_start()
if inp == 7:
  ban_token()
#<---main code end--->


#<---FILE_END--->
