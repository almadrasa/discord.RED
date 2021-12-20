#<---FILE_START--->


#<---imports start--->
import discum
import asyncio
import colorama
from colorama import Fore, Back, Style
from colorama import init
import os
import time
import asyncio
from base64 import b64encode as b64
from base64 import b64decode
import base64
from random import choice as ch
import requests
from token_bruteforce import bruteforce_token
from token_login import tokenlogin
from userid_info import lookup
from hook_spammer import spam_webhook
from red_rpc import custom_rpc
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
print(Fore.CYAN + "Available tools (input the number at the side):".center(os.get_terminal_size().columns))
print("\n\n")
print(Fore.BLUE + "Exit [0]".center(os.get_terminal_size().columns))
print("\n")
print(Fore.BLUE + "Token Bruteforcer [1]".center(os.get_terminal_size().columns))
print("\n")
print(Fore.BLUE + "Login With a Token [2]".center(os.get_terminal_size().columns))
print("\n")
print(Fore.BLUE + "UserID Lookup [3]".center(os.get_terminal_size().columns))
print("\n")
print(Fore.BLUE + "Webhook Spammer [4]".center(os.get_terminal_size().columns))
print("\n")
print(Fore.BLUE + "Custom Status Message [5]".center(os.get_terminal_size().columns))
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
#<---main code end--->


#<---FILE_END--->
