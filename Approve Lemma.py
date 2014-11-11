# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Lemma Approver
# This code approves lemma based on morphology, etc.

# <codecell>

from generator import *

# <codecell>

tokens_remaining = to_check() # gets list of tokens to check

def update_tokens_remaining():
    global tokens_remaining
    tokens_remaining = to_check()
    
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

def token_search(s):
    return [t for t in tokens_remaining if re.search(s,t)]

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

ends_with(":t")

# <codecell>

mark_okay_lemmas(ends_with(':t'))
update_files()
print_stats()

# <codecell>

token_search("(\.s|\.z|\:t|:z)$")

# <codecell>

mark_okay_lemmas(token_search("(\.s|\.z|\:t|:z)$"))
print_stats()
update_files()

# <codecell>

mark_okay_lemmas(token_search("(\.s|\.z|:t|:z)-e$"))

# <codecell>

ends_with("'haa-e")

# <codecell>

to_add = []
for t in ends_with("'haa-e"):
    singular=t[0:-6]
    lemmas[t] = [singular]
    to_add.append(t)
    
    if singular in tokens_remaining:
        lemmas[singular] = [singular]
        to_add.append(singular)
        
    if singular+'-e' in tokens_remaining:
        lemmas[singular+'-e'] = [singular]
        to_add.append(singular+'-e')
for t in to_add: print t,lemmas[t]

# <codecell>

mark_okay_lemmas(to_add)

# <codecell>

print_stats()
update_files()
update_tokens_remaining()

# <codecell>

ii_e = ends_with('ii-e')
ii_e

# <codecell>

to_add = []
for x in ii_e:
    ii_e_root = x[:-2]
    lemmas[x] = [ii_e_root]
    to_add.append(x)
    if ii_e_root in tokens_remaining:
        lemmas[ii_e_root] = [ii_e_root]
        to_add.append(ii_e_root)
to_add,len(to_add)      

# <codecell>

mark_okay_lemmas(to_add)

# <codecell>

print_stats()

# <codecell>

update_files()

# <codecell>

print_stats()

# <codecell>

update_tokens_remaining()

# <codecell>

ends_with('))uu;n')

# <codecell>

ends_with('haa-e')

# <codecell>

[x[:-5] for x in ends_with('haa-e') if x in tokens_remaining]

# <codecell>

ends_with('haa-e')

# <codecell>

to_add=[]
for x in [x[:-2] for x in ends_with('-e') if x[:-2] in tokens_remaining]:
#    lemmas[x] = [x]
    lemmas[x+'-e'] = lemmas[x]
    to_add.append(x)
    to_add.append(x+'-e')
    print x, lemmas[x]

# <codecell>

mark_okay_lemmas(to_add)
print_stats()

# <codecell>

update_files()

# <codecell>

tokens_remaining

# <codecell>

[x+','+','.join(lemmas[x]) for x in search_tokens('-o-')]

# <codecell>

mark_okay_lemmas(search_tokens('o'))

# <codecell>

update_files()
print_stats()
update_tokens_remaining()

# <codecell>

[x for x in tokens_remaining if not(x in search_tokens('-'))]

# <codecell>

[x for x in tokens_remaining if x[-2:]==';n' and x[:-1]+'n' in tokens_remaining]

# <codecell>

mark_okay_lemmas(ends_with('-e'))

# <codecell>

print_stats()

# <codecell>

update_files()

# <codecell>

ends_with('ah')

# <codecell>

len(token_search('^be-'))

# <codecell>

update_files()

# <codecell>

ends_with('q')

# <codecell>

#mark_okay_lemmas(ends_with('q'))
update_tokens_remaining()
update_files()
print_stats()

# <codecell>

tokenize_re = re.compile(r"\-\-\-\-|\(\-e\)|\;rh|chh|\-o\-|\;dh|\;th|\;aa|aa|ch|\:z|\)\)|gh|\-e|th|ph|\:n|dh|\(\(|\:t|uu|\.z|au|\;s|\;r|zh|\;t|ai|\;z|\;x|ii|\;d|\;h|\;n|\-\-|bh|jh|\.s|kh|sh|\;g|\ |\(|\,|\:|b|d|f|h|j|l|n|p|r|t|v|z|\!|\'|\)|\-|\;|\?|\[|\]|a|e|g|i|k|m|o|q|s|u|y|.",
re.DOTALL)
def tokenize(s):
    return tokenize_re.findall(s)
tokenize('shaan')

# <codecell>

left_as_tokens = [tokenize(s) for s in tokens_remaining]

# <codecell>

[x for x in left_as_tokens if not x in  [t for t in left_as_tokens if len(t)>2 and t[-2]=='t' and t[-1] in ['aa','e','ii']]]

# <codecell>

[''.join(x) for x in left_as_tokens if '-' in x and x[-1]=='e']

# <codecell>

mark_okay_lemmas(ends_with('-e'))

# <codecell>

ends_with('ah')

# <codecell>

update_files()

# <codecell>

ends_with('ah')

# <codecell>

mark_okay_lemmas(ends_with('ah'))

# <codecell>

update_files()

# <codecell>


