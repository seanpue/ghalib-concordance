# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
sys.path.append('graphparser')
import graphparser

# <codecell>

nagarip = graphparser.GraphParser('graphparser/settings/devanagari.yaml')

# <codecell>

print nagarip.parse('aakaa').output

# <codecell>

nagarip.old_parser.rules

# <codecell>

print nagarip.old_parser.parse('dil-e ')

# <rawcell>

#     nagarip.

# <codecell>

nagarip.old_parser.rules

# <codecell>


# <codecell>

urdup = graphparser.GraphParser('graphparser/settings/urdu.yaml')

# <codecell>

urdup.parse("she").output

# <codecell>

print urdup.parse("haa;n").output

# <codecell>

[r for r in urdup.rules if '-e' in r.tokens]

# <codecell>

urdup.parse('shaa-e')

# <codecell>

nodes =urdup.DG.nodes(data=True)#[n for n in urdup.DG.nodes(data=True) if '-e' in n['tokens']]

# <codecell>

type(nodes)

# <codecell>

for n in nodes:
    if 'token' in n[1]!=None:
#        print n[1]['token']
        if n[1]['token']=='y':
            print n
            print urdup.DG.in_edges(162)

# <codecell>

urdup.DG.node[129]

# <codecell>

urdup.DG.in_edges(162)

# <codecell>

urdup.parse('-e')

# <codecell>

urdup.tokenize('-e')

# <codecell>

urdup.DG.edges(data=True)

# <codecell>

urdup.DG.node[162]

# <codecell>


