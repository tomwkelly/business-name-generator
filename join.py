import json
import sys

root = sys.argv[1]

f = open('wordlist3.json')
words = json.load(f)
f2 = open('suffixes.json')
swords = json.load(f2)

def root_first(rword, lwords):
  wlist = []
  for i, letter in enumerate(rword):
      if i == 0:
          continue
      for word in lwords:
         pos = word.find(letter)
         if pos != -1 and pos != len(word) -1:
            w = rword[:i] + word[pos:]
            if w not in wlist:
               wlist.append(w)
  return wlist
     

def word_first(rword, lwords):
  wlist = []
  for i, letter in enumerate(rword):
      for word in lwords:
         pos = word.find(letter)
         if pos != -1 and pos != 0:
            w = word[:pos] + rword[i:]
            if w not in wlist:
               wlist.append(w)
  return wlist

def join_all_w():
   a = []
   for word in words:
      a += word_first(word, words)
   s = set(a)
   for i in s:
      if len(i) > 5:
        print(i)

def join_all_r():
   a = []
   for word in words:
      x = root_first(word, words)
      if x is not None:
        a += x
   s = set(a)
   for i in s:
      if len(i) > 5:
        print(i)

def join_all_w2(words1, words2):
   a = []
   for word in words1:
      a += word_first(word, words2)
   s = set(a)
   for i in s:
      if len(i) > 5:
        print(i)

def join_suffixes(suffixes, words):
   a = []
   for suffix in suffixes:
    l = suffix[0]
    for word in words:
       pos = word.find(l)
       if pos != -1 and pos != 0:
          w = word[:pos] + suffix[0:]
          if w not in a:
             a.append(w)
   for i in a:
      if len(i) > 5:
        print(i)
      
def straight_join(suffixes, words):
   for word in words:
      for suffix in suffixes:
         print(word + suffix)
        
straight_join(swords, words)   