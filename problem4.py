# Import DFA from Eppstein
from lib.Automata import *
import lib.Automata
from pprint import pprint
import numpy

def transition_counts(dfa, n):
	n = int(n)
	# length of the dfa
	sc = dfa.__len__()
	states = list(dfa.states())
	# matrix a[i][j] = the number of states between i and j
	# square matrix of size sc x sc
	a = numpy.zeros((sc, sc))
	#vector of final states 
	v = numpy.zeros((sc, 1))

	for i, s in enumerate(states):

		if(not dfa.isfinal(s)):
			v[i][0] = 1
		for j, states in enumerate(states):
			# number of transistions
			tc = 0
			t = 0
			while t < 10:
				if states == dfa.transition(s, str(t)):
					tc = tc + 1
				t = t + 1
			a[i][j] = tc
		pprint(a)

	# matrix multiplication, can't figure out why this isn't working
	# 
	m = numpy.dot(a, a)
	for i in range(1, n-1):
		m = numpy.dot(m, a) 
	res = numpy.dot(m, v)

	#pprint(res)
	return res


## from problem 3
delta = {} 

alpha = ['0','1','2','3','4','5','6','7','8','9']
x = int(input("Enter divisibility (k): "))

for i in range(0, x):
	for j in range(0,10):
		delta[(str(i), str(j))] = (str(int(str(i)+str(j)) % x), str(i+x))
for i in range(x, 2*x):
	for j in range(0,10):
		delta[(str(i), str(j))] = (str(int(str(i)+str(j)) % x))

N = LookupNFA(alpha, ['0'], delta, set(['0', str(x)] ))
#N.pprint()
#print "Number of states in the NFA: ", N.__len__(), "for divisibility: ", x
toMinDFA = MinimumDFA(DFAfromNFA(N))
print "Number of states in minimum dfa: ", toMinDFA.__len__()

# Now for problem 4
n = str(input("enter number of digits (n): "))
transition_counts(toMinDFA, n)
