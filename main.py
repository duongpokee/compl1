import requests
import os
from pystyle import Colors, Colorate
import time
import random
from threading import Thread
from colorama import Fore, Back, Style




R = '\033[31m'
G = '\033[32m'
W = '\033[0m'

os.system('cls' if os.name == 'nt' else 'clear')

print(
    Colorate.Vertical(
      Colors.blue_to_purple, """
─────────────────────────────────────────────────
    █████████████████████████████████
    █▄─▄███▄─██─▄█▄─▀─▄█▄─██─▄█▄─▄▄▀█
    ██─██▀██─██─███▀─▀███─██─███─██─█
    ▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄█▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀
─────────────────────────────────────────────────
    """))

# nglusername = input(Colorate.Vertical(Colors.blue_to_purple, "Username: "))
# count = int(input(Colorate.Vertical(Colors.blue_to_purple, "Count: ")))
nglusername = input('Username: ')
count = 1000


def t1():
  while True:
    global nglusername, listmessage, count
    # A = 'Thread #' + str(random.choice(range(1, 1000))) + ' '
    A = 'Spaming... '
    value = 0
    notsend = 0
    while value < count:
      fileua = open("ua.txt", "r")
      ua = fileua.read().splitlines()
      lineua = len(open("ua.txt").readlines())
      fileua.close
      a = random.choice(range(1, lineua))
      ua = ua[int(a)]

      fileplat = open("plat.txt", "r")
      plat = fileplat.read().splitlines()
      lineplat = len(open("plat.txt").readlines())
      fileplat.close
      b = random.choice(range(1, lineplat))
      pl = plat[int(b)]

      filepx = open("proxies.txt", "r")
      px = filepx.read().splitlines()
      linepx = len(open("proxies.txt").readlines())
      filepx.close
      c = random.choice(range(1, linepx))
      px = px[int(c)]

      filedv = open("devices.txt", "r")
      dv = filedv.read().splitlines()
      linedv = len(open("devices.txt").readlines())
      filedv.close
      d = random.choice(range(1, linedv))
      dv = dv[int(d)]

      filems = open("messages.txt", "r", encoding='utf-8')
      ms = filems.read().splitlines()
      linems = len(open("messages.txt", encoding='utf-8').readlines())
      filems.close
      e = random.choice(range(1, linems))
      ms = ms[int(e)]

      proxies = {'http': 'px'}


      headers = {
        'Host': 'ngl.link',
        'sec-ch-ua':
        '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        # 'user-agent':
        # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'user-agent': ua,
        # 'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform': pl,
        'origin': 'https://ngl.link',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://ngl.link/{nglusername}',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
      }

      data = {
        'username': f'{nglusername}',
        'question': f'{ms}',
        'deviceId': f'{dv}',
        'gameSlug': '',
        'referrer': '',
      }

      response = requests.post('https://ngl.link/api/submit',
                       headers=headers,
                       data=data,
                       proxies=proxies)

      if response.status_code == 200:
        notsend = 0
        value += 1
        print(Fore.BLUE + A + ms + '->'+ G + px + "[+]" + W + "Send =>" + G + "{}".format(value) + W)
      else:
        notsend += 1
        print(Fore.RED + A + ms + '->'+ R + px + "[-]" + W + "Not Send")
      if notsend == 10:
        print(Fore.RED + A + ms + '->'+ R + px + "[!]" + W + "Wait 15 Seconds")
        time.sleep(15)
        notsend = 0
    pass

try:
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
  # r1 = Thread(target=t1).start()
except:
  print("End.")