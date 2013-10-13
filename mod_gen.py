x = 7

for i in range(0, x):
	print "========================= state: ", i, "===================================="
	for j in range(0,10):
		print "Input:", j, "--->", int(str(i)+str(j)) % x
		print