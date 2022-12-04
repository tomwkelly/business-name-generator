import string
import random
import socket
import subprocess

DOMAIN_URL='https://domains.google.com/registrar/search?searchTerm='

def domain_free(domain):
  command = "whois {} | grep -e 'No match for domain' -e 'Domain not found'".format(domain)
  whois_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
  return whois_output.returncode == 0

all_letters = list(string.ascii_lowercase)
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in all_letters if x not in vowels]
endings = ['.io', '.com']

def get_consonant():
  return consonants[random.randint(0, len(consonants) -1)]

def get_vowel():
  return vowels[random.randint(0, len(vowels) -1)]

def get_ran_all():
  f = []
  for c in consonants:
    for v in vowels:
        for e in endings:
          x = 'ma' + c + v + e
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
  for i in a:
    if domain_free(i):
      print(i, f'{DOMAIN_URL}{i}')

double_check()