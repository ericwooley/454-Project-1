from pprint import pprint


delta = {}

x = int(input("Enter k: "))
# this is for a test
for i in range(0, x):
	delta[str(i)] = {}
	delta[str(i)]['transitions'] = {}
	delta[str(i)]['Accepting'] = False
	for j in range(0,10):
		delta[str(i)]['transitions'][str(j)]=set([str(int(str(i)+str(j)) % x), str(i)+'`'])
for i in range(0, x):
	delta[str(i)+'`'] = {}
	delta[str(i)+'`']['transitions'] = {}
	delta[str(i)+'`']['Accepting'] = False
	for j in range(0,10):
		delta[str(i)+'`']['transitions'][str(j)] = set(str(int(str(i)+str(j)) % x))

delta['0']['Accepting'] = True
delta['0`']['Accepting'] = True
pprint(delta)