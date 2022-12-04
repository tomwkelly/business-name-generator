import string
import random
import socket
import subprocess
import sys
import asyncio

DOMAIN_URL='https://domains.google.com/registrar/search?searchTerm='

all_letters = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in all_letters if x not in vowels]
endings = ['.io']

interp = sys.argv[1]

start = sys.argv[2] if len(sys.argv) > 2 else ''

if len(sys.argv) > 3:
  for x in sys.argv[3]:
    if x in vowels:
      vowels.remove(x)
    elif x in consonants:
      consonants.remove(x)


async def run_whois(domain):
    command = "whois {} | grep -e 'No match for domain' -e 'Domain not found'".format(domain)
    proc = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    await proc.communicate()
    
    if proc.returncode == 0:
      print(domain, f'{DOMAIN_URL}{domain}')

      
async def run_all_whois(items):
  t = []
  for i in items:
    t.append(run_whois(i))
  await asyncio.gather(*t)


def add_consonants(items):
  x = []
  for i in items:
    for c in consonants:
      x.append(i + c)
  return x

def add_vowels(items):
  x = []
  for i in items:
    for v in vowels:
      x.append(i + v)
  return x

def add_items(items, type):
  if type == '':
    return items
  
  t = type[0]

  if t == 'c':
    return add_items(add_consonants(items), type[1:])
  if t == 'v':
    return add_items(add_vowels(items), type[1:])
  
  raise ValueError(f'{t} is not a valid type')

def get_combos():
  if interp[0] not in ['v','c']:
    raise ValueError(f'{interp[0]} is not a valid type')
  
  if start != '':
    items = [start]
    return add_items(items, interp)

  items = consonants if interp[0] == 'c' else vowels
  return add_items(items, interp[1:])



def get_consonant():
  return consonants[random.randint(0, len(consonants) -1)]

def get_vowel():
  return vowels[random.randint(0, len(vowels) -1)]

def get_ran_all():
  f = []
  for c in get_combos():
    for e in endings:
      x = c + e
      if(check_available(x)):
        f.append(x)
  print('Sock complete, checking:', f)
  return f

def check_available(domain):
  try:
    socket.gethostbyname(domain)
    return False
  except socket.gaierror:
    return True
  

def double_check():
  a = get_ran_all()
  asyncio.run(run_all_whois(a))

      


double_check()