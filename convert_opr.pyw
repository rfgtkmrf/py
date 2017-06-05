from random import *
import time
import json

f = open('udovl.txt','r')
a = f.readlines()
f.close()
dd = len(a)
idq = [] 
for i in range(dd):
    if a[i][0] == '#': idq.append(i)

qts = []

dd = len(idq) 
q = []  

for i in range(dd):
    q.append(a[idq[i]][1:-1])
    quest = {
    'numq': i,
    'question': q[i]
    }
    qts.append(quest)        

#print(qts)
f = open('udovl.q','w')
json.dump(qts, f)
f.close()

qts = ''

f = open('udovl.q','r')
qts = json.load(f)
f.close()
for qqq in qts:
    print(int(qqq['numq'])+1,'.',qqq['question'])
    print()
