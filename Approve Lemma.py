# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Lemma Approver
# This code approves lemma based on morphology, etc.

# <codecell>

from generator import *

# <codecell>

tokens_remaining = to_check() # gets list of tokens to check

def ends_with(s):
    out = []
    for t in tokens_remaining:
        i = 0-len(s)
        if t[i:]==s:
            out.append(t)
    return out

def print_ends_with(s):
    tokens =ends_with(s)
    print ', '.join(ends_with(s))

def mark_okay_lemmas(are_okay):

    assert type(are_okay)==list
    for t in are_okay:
        okay_lemmas[t] = lemmas[t]

# <codecell>

print_ends_with('uu')

# <codecell>

mark_okay_lemmas(ends_with('uu'))

# <codecell>

update_files()

# <codecell>

print_stats()

# <codecell>


