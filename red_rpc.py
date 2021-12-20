import discord
import asyncio
from colorama import init, Fore, Back, Style
import os

def custom_rpc():
  client = discord.Client()
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  init()
  print(f"{Fore.BLUE}Your Token: ", end='')
  TOKEN = input()

  @client.event
  async def on_ready():
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')
    print(f"{Fore.BLUE}Status message: ", end='')
    STATUS = input()
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(STATUS))
    print(f"{Fore.RED}{client.user}'s status{Fore.MAGENTA} is now {Fore.BLUE}\"{STATUS}\"{Fore.MAGENTA}.")


  client.run(TOKEN)
