import requests
from colorama import init, Style, Fore
import os


def spam_webhook():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  init()
  print(f"{Fore.BLUE}Input Webhook URL to Spam: ",end='')
  HOOK_URL = input()
  print(f"{Fore.BLUE}What name should the webhook have?: ", end='')
  hook_username = input()
  print(f"{Fore.BLUE}Input Message to Spam: ", end='')
  message = input()
  print(f"{Fore.BLUE}How many times would you like to spam that (int)?: ", end='')
  times = int(input())
  hook_data = {
      "content" : f"{message}",
      "username" : f"{hook_username}"
  }
  once = 0
  print(Fore.GREEN + "Spamming now...")
  while once < times+1:
    requests.post(HOOK_URL, json = hook_data)
    once=once+1
