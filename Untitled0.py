# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv

verses = {} # dictionary of verses, e.g. 001.01.0

with open('input/verses.csv','r') as csvfile:
    versereader = csv.reader(csvfile)
    for row in versereader:
        (verse_id, input_string, real_scan) = row
        if not 'x' in verse_id: # skip ones with x (not in muravvaj divan)
            verses[verse_id] = input_string.strip()
# REMOVE Xs

# <codecell>

#tokens = {} by token in
tokens = {}
for k in verses.keys():
    print k
#    print 'k',k
    v_tokens = verses[k].split(' ')
    print 'tokens',tokens
    for id,t in enumerate(v_tokens):
        token_id = k+'.'+str(id).zfill(2)
        tokens[token_id] = t

# <codecell>

verses.keys()

# <codecell>


