import random
import json
import sys

f = open('wordlist.json')
words = json.load(f)
f2 = open('suffixes.json')
suffixes = json.load(f2)
max = 200

vowels = ['a', 'e', 'i', 'o', 'u']
def gen():
  for x, word in enumerate(words):
      for i, letter in enumerate(word):
          if letter in vowels:
              w = list(word)
              w[i] = vowels[random.randint(0, len(vowels) -1)]
              word = "".join(w)
    
      print(word)

def suff():
    a = []
    count = 0
    for x, word in enumerate(words):
      if count > max:
         break
      count += 1
      for i, letter in enumerate(word):
          if letter in vowels:
            for suffix in suffixes:
               w = word[:i] + suffix
               if w not in a and len(w) > 5:
                  a.append(w)
    for i in a:
       print(i)
          

suff()

