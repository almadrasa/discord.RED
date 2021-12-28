#<---IMPORTS--->
import os
import sys
import requests
import json

def install(package):
  os.system(f"{sys.executable} -m pip install {package}")
try:
  import discum
except ModuleNotFoundError:
  print("installing required package...")
  os.system(f"{sys.executable} -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum")
try:
  from colorama import init, Fore, Back, Style
except ModuleNotFoundError:
  install("colorama")
try:
  import pyfiglet
except ModuleNotFoundError:
  install("pyfiglet")
try:
  from pyxtension.Json import Json
except ModuleNotFoundError:
  install("pyxtension")
try:
  import datetime
except ModuleNotFoundError:
  install("datetime")
try:
  import time
except ModuleNotFoundError:
  install("time")
try:
  import random
except ModuleNotFoundError:
  install("random")
try:
  import webbrowser
except ModuleNotFoundError:
  install("webbrowser")


#<---FUNCTION START--->
def red_start():
  # defining clear function
  def clear():
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')

  # aesthetics startup
  init()
  os.system('title sb.RED')
  print(f"{Style.BRIGHT}")
  print(f"{Back.BLACK}")
  clear()

  # auth file checks
  print(f"{Fore.RED}Gathering auth file...")
  try:
    f_read1 = open("red_token.txt", "r")
    a = f_read1.read()
    f_read1.close()
    print(f"{Fore.BLUE}Auth gathered, token is \"{a}\"")
  except:
    print(f"{Fore.YELLOW}Auth file gathering failed. Create a file named red_token.txt and store your token inside, then start Red again.")
    exit(0)

  # token validity checking
  print(f"{Fore.RED}Testing auth...")
  discord = 'https://discordapp.com/api/users/@me'
  headers = {"Authorization":f"{a}"}
  x = requests.get(discord, headers=headers)
  if int(x.status_code) == 401:
    print(f"{Fore.YELLOW}The provided token is invalid. Fill red_token.txt with a valid token, and then start Red again.")
    exit(0)
  else:
    print(f"{Fore.BLUE}Provided token is valid, continuing Red startup.")

  # hook file checks
  print(f"{Fore.RED}Gathering response hook...")
  try:
    f_read2 = open("red_hook.txt", "r")
    b = f_read2.read()
    f_read2.close()
    print(f"{Fore.BLUE}Hook gathered, URL is \"{b}\"")
  except:
    print(f"{Fore.YELLOW}Hook file gathering failed. Create a file named red_hook.txt and store your webhook inside, then start Red again.")
    exit(0)

  # hook validity checking
  print(f"{Fore.RED}Testing hook status...")
  hook_data = {
        "content" : f"Webhook Status-Code Test",
        "avatar_url" : "https://cdn.discordapp.com/attachments/876658708149571595/922628304735961148/unknown.png",
        "username" : "Red Calibration Sequence"
    }
  y = requests.post(b, json=hook_data)
  if int(y.status_code) == 400:
    print(f"{Fore.YELLOW}The webhook URL located in red_hook.txt is invalid. Replace it with a valid discord webhook, then Red can run.")
    exit(0)
  else:
    print(f"{Fore.BLUE}Hook is valid, continuing Red's startup.")

  # assigning globals
  try:
    USER_TOKEN = a
    RESPONSE_HOOK = b
    me = None
    bot = discum.Client(token=USER_TOKEN,log=False)
    def respond_with(str):
      hook_data = {
        "content" : f"<@{bot.gateway.session.user['id']}>\n{str}",
        "avatar_url" : "https://cdn.discordapp.com/attachments/876658708149571595/922628304735961148/unknown.png",
        "username" : "Red"
       }
      requests.post(RESPONSE_HOOK, json=hook_data)


    def embed_with(str1, str2):
      hook_data = {
        "content" : f"<@{bot.gateway.session.user['id']}>",
        "avatar_url" : "https://cdn.discordapp.com/attachments/876658708149571595/922628304735961148/unknown.png",
        "username" : "Red"
    }
      hook_data["embeds"] = [{
           "title" : f"{str1}",
           "description" : f"{str2}",
           "timestamp": f"{datetime.datetime.utcnow()}"
      }]
      requests.post(RESPONSE_HOOK, json=hook_data)


    def embed_with_author(str1, str2, str3):
      hook_data = {
        "content" : f"<@{bot.gateway.session.user['id']}>",
        "avatar_url" : "https://cdn.discordapp.com/attachments/876658708149571595/922628304735961148/unknown.png",
        "username" : "Red"
    }
      hook_data["embeds"] = [{"description" : f"{str2}", "title" : f"{str1}", "timestamp": f"{datetime.datetime.utcnow()}", "thumbnail": { "url": f"{str3}" } }]
      requests.post(RESPONSE_HOOK, json=hook_data)

    def msg_delete(chanid, msgid):
      useragents = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.10 (like Gecko) (Kubuntu)', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a']
      USERAGENT = random.choice(useragents)
      DATA = {"User-Agent": f"{USERAGENT}", "Authorization": f"{USER_TOKEN}"}
      requests.delete(f'https://discord.com/api/v9/channels/{chanid}/messages/{msgid}', headers=DATA)


    @bot.gateway.command
    def onready(resp):
      if resp.event.ready_supplemental: #ready_supplemental is sent onready
        user = bot.gateway.session.user
        username = user['username']
        discrim = user['discriminator']
        me = f"{username}#{discrim}"
        clear()
        def welcome():
          print(Fore.RED + "          $$\\           $$$$$$$\\  $$$$$$$$\\ $$$$$$$\\  ".center(os.get_terminal_size().columns))
          print(Fore.RED + "           $$ |          $$  __$$\\ $$  _____|$$  __$$\\ .".center(os.get_terminal_size().columns))
          print(Fore.RED + " $$$$$$$\\ $$$$$$$\\      $$ |  $$ |$$ |      $$ |  $$ |".center(os.get_terminal_size().columns))
          print(Fore.RED + "$$  _____|$$  __$$\\     $$$$$$$  |$$$$$\\    $$ |  $$ |".center(os.get_terminal_size().columns))
          print(Fore.RED + " \\____$$\\ $$ |  $$ |    $$ |  $$ |$$ |      $$ |  $$ |".center(os.get_terminal_size().columns))
          print(Fore.RED + "$$$$$$$  |$$$$$$$  |$$\\ $$ |  $$ |$$$$$$$$\\ $$$$$$$  |".center(os.get_terminal_size().columns))
          print(Fore.RED + " \_______/ \_______/ \__|\__|  \__|\________|\_______/ \n".center(os.get_terminal_size().columns))
          print(Fore.WHITE + "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n".center(os.get_terminal_size().columns))
          col_size = os.get_terminal_size().columns
          inp = "the only selfbot you'll ever need."
          print(Fore.RED + inp.center(col_size))
          print("\n\n\n")
          print(Fore.BLUE)
          print(f"Red is up and running;\n".center(col_size))
          print(Fore.RED)
          print(f"run \"r.help\" in discord for a list of usable commands.".center(col_size))
          print("\n\n")
          print("(CTRL + C AT ANY TIME TO STOP RED)".center(col_size))
        welcome()
        embed_with("Red is up and running!", f"Logged in as `{me}`")
    @bot.gateway.command
    def onmsg(resp):
      if resp.event.message:
          msg = resp.parsed.auto()
          channel = msg['channel_id']
          username = msg['author']['username']
          discrim = msg['author']['discriminator']
          author = f"{username}#{discrim}"
          content = str(msg['content'])
          if msg['author']['id'] != bot.gateway.session.user['id']:
            pass


          elif content == "r.help":
            bot.deleteMessage(msg['channel_id'], msg['id'])
            webbrowser.open('https://13-05.github.io/dsc.red/commands', new=2)


          elif content == "r.ping":
            try:
              msg_delete(msg['channel_id'], msg['id'])
              lat = bot.gateway.latency
              ping = str({round(lat * 1000)}).replace("{", "")
              ping = ping.replace("}", "")
              ping = ping + "ms"
              embed_with("Current Ping:", ping)
            except:
              msg_delete(msg['channel_id'], msg['id'])
              embed_with("Uh Oh!", "An error ocurred! Wait about thirty seconds and then try running `r.ping` again.")


          elif content == "r.servinfo":
            msg_delete(msg['channel_id'], msg['id'])
            guilds = bot.getGuilds().json()
            g = next((g for g in guilds if g['id'] == msg['guild_id']), {})
            memb_ct = int(bot.gateway.session.guild(msg['guild_id']).memberCount)
            serv_name = g['name']
            descr = bot.gateway.session.guild(msg['guild_id']).description
            ownr = str(bot.gateway.session.guild(msg['guild_id']).owner)
            x = requests.get(f'https://discordid.13-05.repl.co/api/{ownr}')
            j = Json(x.text)
            a = bot.gateway.session.guild(msg['guild_id']).icon
            embed_with_author(f"{serv_name}'s Stats", f"Member count: {memb_ct}\nServer Description: {descr}\nOwner: {j.user.tag}", f"https://cdn.discordapp.com/icons/{msg['guild_id']}/{a}")


          elif content == "r.dadjoke":
            msg_delete(msg['channel_id'], msg['id'])
            useragents = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.10 (like Gecko) (Kubuntu)', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a']
            USERAGENT = random.choice(useragents)
            data = {"User-Agent": USERAGENT, "Accept": "text/plain"}
            r = requests.get('https://icanhazdadjoke.com/', headers=data)
            embed_with("Dad Joke", r.text)


          elif content.startswith("r.ascii"):
            msg_delete(msg['channel_id'], msg['id'])
            to_convert = content[7:]
            converted = pyfiglet.figlet_format(to_convert, font="stop")
            respond_with(f"```{converted}```")


          elif content == "r.crypto":
            msg_delete(msg['channel_id'], msg['id'])
            u = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD')
            v = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
            w = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
            embed_with("Current Crypto Prices", "Monero: $" + str(u.text).replace('{"USD":', '').replace('}', '') + f" USD\nBitcoin: $" + str(v.text).replace('{"USD":', '').replace('}', '') + " USD\nEthereum: $" + str(w.text).replace('{"USD":', '').replace('}', '') + " USD")


          elif content == "r.nuke":
            msg_delete(msg['channel_id'], msg['id'])
            def spam_message(chanid, message, times):
              once = 0
              while once < times+1:
                bot.sendMessage(chanid, message)
                once=once+1
            guilds = bot.getGuilds().json()
            g = next((g for g in guilds if g['id'] == msg['guild_id']), {})
            embed_with("Check the Console", "The channel nuke is awaiting confirmation.")
            print(f"{Fore.RED}Are you sure you'd like to nuke " + g['name'] + f"? This action may result in your account's {Fore.YELLOW}termination{Fore.RED}.\n\nY/N: ", end='')
            choiceof = input()
            if choiceof.lower() == "y":
              print(f"{Fore.GREEN}Alright, Red's nuking it now.")
              embed_with("Channel Nuke Status", f"The nuke was started, Red's nuking {g['name']} now.")
              spam_message(msg['channel_id'], "<@" + bot.gateway.session.guild(msg['guild_id']).owner + ">", 1000)

            if choiceof.lower() == "n":
              print(f"{Fore.BLUE}Alright, Red won't nuke that channel.")
              embed_with("Channel Nuke Status", "The nuke was aborted.")


          elif content == "r.disc-hacks":
            msg_delete(msg['channel_id'], msg['id'])
            embed_with("Looking for ways to exploit Discord?", "Well, I have a github repository [here](https://github.com/13-05/disc-python-hacks) that exposes all of Discord's weaknesses. Enjoy!")

          elif content.startswith("r.userinfo"):
            msg_delete(msg['channel_id'], msg['id'])
            usr = content[10:]
            inf = requests.get(f'https://discordid.13-05.repl.co/api/{usr}')
            full = Json(inf.text)
            created = int(full.user.createdTimestamp)/1000.0
            time_obj = datetime.datetime.fromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S.%f')
            embed_with_author(f"{full.user.tag}'s Stats", f"Username: {full.user.tag}\nBot?: {full.user.bot}\nCreated at: {time_obj}", f"{full.user.displayAvatarURL}")


          elif content.startswith("r.howgay"):
            msg_delete(msg['channel_id'], msg['id'])
            embed_with_author("How gay are you?", f"<@{msg['author']['id']}> is {random.randint(1,100)}% gay", "https://cdn.discordapp.com/attachments/888810718206492692/918226176370176080/giphy_1.gif")

          elif content.startswith("r.8ball"):
            msg_delete(msg['channel_id'], msg['id'])
            question = content[7:]
            OUTPUTS = ['Maybe, just wait and see.', 'Definitely not.', 'Yes.']
            choice = random.choice(OUTPUTS)
            embed_with_author(f"{question}", f"{choice}", "https://raw.githubusercontent.com/13-05/discord.RED/main/images/8ball.webp")


          elif content == "r.advice":
            msg_delete(msg['channel_id'], msg['id'])
            useragents = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.10 (like Gecko) (Kubuntu)', 'Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a']
            USERAGENT = random.choice(useragents)
            req = requests.get('https://api.adviceslip.com/advice')
            adv = json.loads(req.text)
            embed_with_author("A Little Advice...", f"{adv['slip']['advice']}", "https://raw.githubusercontent.com/13-05/discord.RED/main/images/fortune-cookie.png")


          elif content.startswith("r.ghostping"):
            uid = content[11:].replace(' ', '')
            msg_delete(msg['channel_id'], msg['id'])
            EXCUSES = ['yo', 'hey!', 'im so bored', 'wsp', ':flushed:', 'lol', 'nice']
            MSG = f"""{random.choice(EXCUSES)} ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ <@{uid}>"""
            bot.sendMessage(msg['channel_id'], MSG)


  except:
    print(f"{Fore.YELLOW}Auth gathering and hook gathering failed, make sure red_token.txt and red_hook.txt are both present in the current directory, then start Red again.")
    exit(0)

  # attempt to startup red
  clear()
  print(f"{Fore.RED}Starting up Red...")
  try:
    bot.gateway.run()
  except:
    print(f"{Fore.YELLOW}There was an error starting up {Fore.RED}Red{Fore.YELLOW}.")
