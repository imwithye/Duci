#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dict_reader import get_content_list
from word_parser import parse

if __name__ == "__main__":
  content_list = get_content_list()
  for content in content_list:
    word_list = parse(content["body"])
    for word in word_list:
      print word["word"]
