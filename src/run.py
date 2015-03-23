#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dict_reader import get_content_list
from word_parser import parse

class WordList:
  def __init__(self):
    self.dict = {}

  def append(self, word):
    pinyin = word["pinyin"]
    if pinyin not in self.dict:
      self.dict[pinyin] = []
    self.dict[pinyin].append(word["word"])

  def rank(self):
    word_list = []
    for key, value in self.dict.iteritems():
      word_list.append((key, value))
    word_list = sorted(word_list, key=lambda word: len(word[1]), reverse=True)
    return word_list

def read(dict_file, spliter="<br>"):
  content_list = get_content_list(dict_file, spliter)
  words = WordList()
  for content in content_list:
    word_list = parse(content["body"])
    for word in word_list:
      words.append(word)
  word_rank = words.rank()
  for rank in word_rank:
    print("%-5d%-15s%s" % (len(rank[1]), rank[0], ",".join(rank[1])))

if __name__ == "__main__":
  read("xinqiji.txt")
  read("libai.txt", "<p>")
