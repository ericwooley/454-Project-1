# Import DFA from Eppstein
from lib.Automata import *
from pprint import pprint


delta = {} 

x = int(input("Enter k: "))
# this is for a test
for i in range(0, x):
	delta[i] = {}
	for j in range(0,10):
		delta[i][j]=set([int(str(i)+str(j)) % x, x+i])
for i in range(0, x):
	delta[x+i] = {}
	for j in range(0,10):
		delta[x+i][j] = set([str(int(str(i)+str(j)) % x)])
pprint (delta)
N = LookupNFA("0123456789", set([0]), delta, set([0, x]) )
N.pprint()
