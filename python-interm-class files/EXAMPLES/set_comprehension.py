#!/usr/bin/env python

import re

with open("../DATA/mary.txt") as mary_in:
    s = {w.lower()  for ln in mary_in  for w in re.split(r'\W+', ln) if w} #<1>
print(s)

# A set only includes unique items, so you end up with one instance of every word in the text.