#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pypinyin, jieba

text = """
  摸鱼儿（淳熙己亥，自湖北漕移湖南，同官王正之置酒小山亭，为赋）
  更能消、几番风雨。匆匆春又归去。惜春长恨花开早，何况落红无数。春且住。见说道、天涯芳草迷归路。怨春不语。算只有殷勤，画檐蛛网，尽日惹飞絮。
  长门事，准拟佳期又误。蛾眉曾有人妒。千金纵买相如赋，脉脉此情谁诉。君莫舞。君不见、玉环飞燕皆尘土。闲愁最苦。休去倚危楼，斜阳正在，烟柳断肠处。
  """

def parse(text):
  re = []
  seg_list = jieba.cut(text.strip(), cut_all=True)
  spliter = ",".encode("utf-8")
  seg_strs = spliter.join(seg_list).encode("utf-8").split(",")
  for seg_s in seg_strs:
    seg_decode = seg_s.decode("utf-8")
    if len(seg_decode) < 2 or len(seg_decode) > 3:
      continue
    seg_dict = {
      u"word": seg_decode,
      u"pinyin": "".join(pypinyin.lazy_pinyin(seg_decode)),
      u"length": len(seg_decode)
    }
    re.append(seg_dict)
  return re

if __name__ == "__main__":
  word_list = parse(text)
  for word in word_list:
    print word[u"word"].encode("utf-8")
