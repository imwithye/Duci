#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def get_content_list(dict_file):
  input = os.path.join(os.path.dirname(os.path.realpath(__file__)), dict_file)
  content_file = open(input)
  content = content_file.read().decode("utf-8")
  content_file.close()
  content_list = content.split("<br>")
  re = []
  for content_item in content_list:
    content_item = content_item.strip()
    content_split = content_item.splitlines()
    title = content_split[0].strip().encode("utf-8")
    body = []
    for i in range(1, len(content_split)):
      body.append(content_split[i].strip().encode("utf-8"))
    re.append({"title": title, "body": body})
  return re
