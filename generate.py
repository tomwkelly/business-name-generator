import random
import json
import sys

f = open('wordlist2.json')
words = json.load(f)
first_len = 3
second_len = 3

def get_word():
  first = words[random.randint(0, len(words))]
  second = words[random.randint(0, len(words))]
  if len(first) < first_len or len(second) < second_len:
    return get_word()
  f = first[:first_len]
  s = second[-second_len:]
  f = f.replace(' ', '')
  s = s.replace(' ', '')
  f = f.replace('.', '')
  s = s.replace('.', '')
  f = f.replace('&', '')
  s = s.replace('&', '')
  f = f.replace('\'', '')
  s = s.replace('\'', '')
  return f.capitalize() + s.lower()

if len(sys.argv) == 4:
  first_len = int(sys.argv[2])
  second_len = int(sys.argv[3])

if len(sys.argv) > 1:
  for i in range(int(sys.argv[1])):
    print(get_word())
else:
  print(get_word())

