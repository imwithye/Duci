#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pypinyin, jieba

def parse(text_list):
  re = []
  for text in text_list:
    seg_list = jieba.cut(text.strip(), cut_all=True)
    spliter = ",".encode("utf-8")
    seg_strs = spliter.join(seg_list).encode("utf-8").split(",")
    for seg_s in seg_strs:
      seg_decode = seg_s.decode("utf-8")
      if len(seg_decode) < 2 or len(seg_decode) > 3:
        continue
      seg_dict = {
        "word": seg_decode.encode("utf-8"),
        "pinyin": "".join(pypinyin.lazy_pinyin(seg_decode)).encode("utf-8"),
        "length": len(seg_decode)
      }
      re.append(seg_dict)
  return re
