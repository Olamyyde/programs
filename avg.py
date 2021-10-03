m=1000
third=list(range(3,m,3))
print('Every 3rd number is: ', third)

tenth=list(range(0,m,10))
print('\nEvery 10th number is: ', tenth)

for i in range(0,m+1):
	if i>1:
		for x in range(2,i):
			if (i%x == 0):
				break
		else:
			print('\nEach prime number is: ',i)


	
		


    