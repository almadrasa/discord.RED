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
  install("discum")
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

#<---imports end--->

#<---graphics setup--->
os.system('cls')
os.system('color 7') # set color to windows default
init() # start colorama
print(Back.BLACK)
print(colorama.ansi.clear_screen())
print(Style.BRIGHT)
os.system("title dsc.RED")

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
#<---end of graphics setup--->

#<--display pretty stuff start--->
def welcome():
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
os.startfile("COMMANDS.txt")
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
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
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
#<---main code end--->


#<---FILE_END--->
