from goal import *
import time

b = True

while(True):
	with open('readme.txt') as f:
		lines = f.readlines()
		value = int(lines[0])
		b = True
		# print(value)
		if value == 1:
			while(b == True):
				movebase_clientA()
				b = False
		elif value == 2:
			while(b == True):
				movebase_clientB()
				b = False
		elif value == 3:
			while(b == True):
				movebase_clientC()
				b = False
		elif value == 4:
			while(b == True):
				movebase_clientD()
				b = False
		elif value == 0:
			while(b == True):
				movebase_clientHOME()
				b = False
		else:
			pass


	time.sleep(4)


