import discord
import asyncio
from colorama import init, Fore, Style
import os

def lookup():
  file = open("bot_token.txt", "r")
  bot_token = file.read()
  file.close()
  init()
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  print(Fore.BLUE + "ID to lookup: ",end='')
  id = input()
  isbot = None
  client=discord.Client()

  @client.event
  async def on_ready():
    username_and_discrim = await client.fetch_user(id)
    username = str(username_and_discrim)[:-5]
    length = len(str(username_and_discrim))-5
    discrim = str(username_and_discrim)[str(username_and_discrim).find("#")+1:].split()[0]
    if username_and_discrim.bot == True:
      isbot = True
    if username_and_discrim.bot == False:
      isbot = False
    when = username_and_discrim.created_at
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')
    print(f"ID: {id}")
    print(f"Username: {username}")
    print(f"Discriminator: {discrim}")
    print(f"Bot?: {isbot}")
    print(f"Created At: {when}")

  client.run(bot_token)
