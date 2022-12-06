import string
import random
import socket
import sys
import asyncio
import whois
import json

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

async def new_whois(domain):
  try:
    w = whois.whois(domain)
    if 'No match for' in w.text or 'Domain not found' in w.text:
        return f'{domain}, {DOMAIN_URL}{domain}'
  except:
    return None

      
async def run_all_whois(items):
  t = []
  for i in items:
    t.append(new_whois(i))
  return await asyncio.gather(*t)


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

def get_combos(i):
  if i[0] not in ['v','c']:
    raise ValueError(f'{i[0]} is not a valid type')
  
  if start != '':
    items = [start]
    return add_items(items, i)

  items = consonants if i[0] == 'c' else vowels
  return add_items(items, i[1:])



def get_consonant():
  return consonants[random.randint(0, len(consonants) -1)]

def get_vowel():
  return vowels[random.randint(0, len(vowels) -1)]

def get_ran_all():
  f = []
  for i in interp.split(','):
    for c in get_combos(i):
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
  x = asyncio.run(run_all_whois(a))
  for i in x:
    if(i is not None):
      print(i)

# f = open('cvc.json')
# words = json.load(f)

# x = asyncio.run(run_all_whois(words))
# for i in x:
#   if(i is not None):
#     print(i)

double_check()