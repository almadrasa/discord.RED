import selenium
from selenium import webdriver
from colorama import Fore, init
from os import name
import os

def tokenlogin():
  init()
  if name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
  print(Fore.BLUE + "token: ", end='')
  token = input()
  script = '''
      const login = (token) => {
          setInterval(() => document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`, 50);
          setTimeout(() => location.reload(), 2500);
      };''' + f'login("{token}")'
  try:
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://discord.com/login")
    driver.execute_script(script)
  except:
    print(f"{Fore.RED}a fatal error ocurred. install the {Fore.BLUE}ChromeDriver (https://chromedriver.chromium.org/){Fore.RED} for your chrome browser version, move it to the directory this script is located in, and then try running this command again. if you have already done all of this, open a github issue.")
  return
