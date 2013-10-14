# Import DFA from Eppstein
from lib.Automata import *
from pprint import pprint


delta = {} 

x = int(input("Enter k: "))
# this is for a test
for i in range(0, x):
	for j in range(0,10):
		# delta['(' + str(i)+', '+str(j)+')' ] = set([int(str(i)+str(j)) % x, x+i])
		delta[(str(i), str(j))] = (str(int(str(i)+str(j)) % x), str(i)+'`')
for i in range(0, x):
	for j in range(0,10):
		delta[(str(i)+'`', str(j))] = (str(int(str(i)+str(j)) % x))
# pprint (delta)

N = LookupNFA(['0','1','2','3','4','5','6','7','8','9'], ['0'], delta, ['0', str(x)] )
pprint (delta)
N.asDFA().minimize().pprint()