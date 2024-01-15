
def ringing():
	for i in range(1,16):
		if i%3 == 0 :
			print('fizz')
		else:
			print(i)

if __name__=='__main__':
	print(ringing())
