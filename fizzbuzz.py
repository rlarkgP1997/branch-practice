
def ringing():
	for i in range(1,16):
		if (i%3==0) and (i%5==0) :
			print('fizzbuzz')
		elif i%3 == 0:
			print('fizz')
		elif i%5 == 0:
			print('buzz')
		else:
			print(i)

if __name__=='__main__':
	print(ringing())
