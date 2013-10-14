# Import DFA from Eppstein
from lib.Automata import *
import lib.Automata
from pprint import pprint


delta = {} 

x = int(input("Enter divisibility: "))
print ("generating nfa...")
# this is for a test
for i in range(0, x):
	for j in range(0,10):
		# delta['(' + str(i)+', '+str(j)+')' ] = set([int(str(i)+str(j)) % x, x+i])
		delta[(str(i), str(j))] = (str(int(str(i)+str(j)) % x), str(i+x))
for i in range(x, 2*x):
	for j in range(0,10):
		delta[(str(i), str(j))] = (str(int(str(i)+str(j)) % x))
# pprint (delta)

N = LookupNFA(['0','1','2','3','4','5','6','7','8','9'], ['0'], delta, set(['0', str(x)] ))
N.pprint()
print "Number of states in the NFA: ", N.__len__(), "for divisibility:", x 
check = str(input("enter a number to check it's near divisibility:"))
ret = N.__call__(check)
if(ret):
	print check, "is near divisble by", x
else:
	print check, "is not near divisble by", x
print "converting to DFA..."
toMinDFA = MinimumDFA(DFAfromNFA(N))
print "Number of states in minimum dfa: ", toMinDFA.__len__()

