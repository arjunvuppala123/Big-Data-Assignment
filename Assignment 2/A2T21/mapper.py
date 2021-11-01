#!/usr/bin/env python3

import sys,json

def dot(a,b):
    val=0
    for x,y in zip(a,b):
        val+=x*y
    return val

def get_similarity(a,b):
    similarity=dot(a,b)/(dot(a,a)*dot(b,b))**0.5
    return similarity


sump={}
with open(sys.argv[1]) as v:
    for line in v:
        a,b=line.strip().split(',')
        a,b=int(a),float(b)
        sump[a]=[0.15,b]
with open(sys.argv[2]) as embed:
    vectors=json.load(embed)


for y in sys.stdin:
    page,pointers=y.strip().split('?')
    pointers=eval(pointers)
    contri=sump[int(page)][1]/len(pointers)
    from_vector=vectors[str(page)]
    M={i:0.85*contri*get_similarity(from_vector,vectors[str(i)]) for i in pointers}
    for i in M:
        if i not in sump:
            sump[i]=[0.15]
        sump[i][0]+=M[i]

for i in sorted(sump.keys(),key=lambda x:str(x)):
    print(i,sump[i][0],sep=',')
    del sump[i]
