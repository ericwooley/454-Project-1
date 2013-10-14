# Import DFA from Eppstein
from lib.Automata import *
from pprint import pprint


delta = {} 

x = int(input("Enter k: "))
# this is for a test
for i in range(0, x):
	for j in range(0,10):
		# delta['(' + str(i)+', '+str(j)+')' ] = set([int(str(i)+str(j)) % x, x+i])
		delta[(str(i), str(j))] = (str(int(str(i)+str(j)) % x), str(x+i))
# for i in range(0, x):
# 	delta[x+i] = {}
# 	for j in range(0,10):
# 		delta[x+i][j] = set([str(int(str(i)+str(j)) % x)])
pprint (delta)

N = LookupNFA("0123456789", set(['0']), delta, set([0, x]) )
N.pprint()